# Yahoo Finance web-scraper.
# Buggy and needs work

"""
Scrape basic stock data (current price, 52-week high/low) from Yahoo Finance
using `requests` + `BeautifulSoup`.

Flow:
    1. Keep a small list of "packaged" symbols to offer the user.
    2. Ask the user to enter their own symbol or get a random one from the list.
    3. Build the quote URL, send a GET request (with a browser-like header).
    4. Parse the returned HTML and pull out the price and 52-week range.
    5. Print the results.
"""

# ---- Standard library --------------------------------------------------------
import random

# ---- Third-party (install with: pip install requests beautifulsoup4) ---------
import requests
from bs4 import BeautifulSoup

# "Packaged" symbols we can offer when the user doesn't want to type their own.
SYMBOL_LIST = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "META"]

# Yahoo returns 404/429 for header-less scripted requests, so we present a
# browser-like User-Agent.
HEADERS = {"User-Agent": "Mozilla/5.0"}

# Network requests should never hang forever; cap every call at 10 seconds.
REQUEST_TIMEOUT = 10


def choose_symbol():
    """Return an uppercase, whitespace-stripped stock symbol chosen by the user.

    The user can either type their own symbol (option 1) or receive a random
    one from SYMBOL_LIST. A `while` loop handles the "is this correct?" retry so
    we don't recurse (recursion here would re-print the welcome banner each time).
    """
    print("Welcome to the stock price checker")

    choose_method = input(
        "Would you like to use a packaged symbol or choose your own?\n"
        "Select 1 to enter your own symbol, press any other key to get one "
        "from the list.\n"
    )

    # --- User wants to enter their own symbol --------------------------------
    if choose_method == "1":
        print("Great! We'll get details on the stock you'd like to check.")

        # Loop until the user confirms the symbol they typed.
        while True:
            # .upper() normalises case ("aapl" -> "AAPL"); .strip() drops any
            # stray spaces the user may have entered.
            symbol = input("Enter a stock symbol: ").upper().strip()
            print(f"You entered: {symbol}")

            confirm = input("Is this the correct symbol? (y/n): ").lower().strip()
            if confirm == "y":
                return symbol
            print("No problem, let's try again.")

    # --- Otherwise, pick a random symbol from the list -----------------------
    symbol = random.choice(SYMBOL_LIST)
    print(f"Cool, we've selected {symbol} to check.")
    return symbol


def get_stock_data(symbol):
    """Fetch the raw HTML for a symbol's Yahoo Finance quote page.

    Returns the page HTML as a string, or None if the request failed (bad
    symbol, network error, rate-limited, etc.).
    """
    url = f"https://finance.yahoo.com/quote/{symbol}"

    try:
        response = requests.get(url, headers=HEADERS, timeout=REQUEST_TIMEOUT)
        # Raise an exception for 4xx/5xx responses so we handle them in one place.
        response.raise_for_status()
    except requests.RequestException as error:
        # RequestException is the base class for *all* requests errors
        # (timeouts, connection errors, HTTP errors), so one except covers them.
        print(f"Could not fetch data for '{symbol}': {error}")
        return None

    return response.text


def parse_stock_data(html):
    """Extract the current price and 52-week high/low from the page HTML.

    Returns a dict like {"price": ..., "week_52_high": ..., "week_52_low": ...}.
    Any field we can't locate is set to None rather than crashing, so a single
    layout change doesn't take down the whole parse.
    """
    soup = BeautifulSoup(html, "html.parser")

    # Current price. We match on the stable `id` ("qsp-price") instead of the
    # hashed class string, since the id survives Yahoo redesigns much longer.
    price_tag = soup.find("span", id="qsp-price")

    # The 52-week range is exposed via a `data-field` attribute on the quote
    # summary table. These attribute names are far more stable than class names.
    high_tag = soup.find("fin-streamer", {"data-field": "fiftyTwoWeekHigh"})
    low_tag = soup.find("fin-streamer", {"data-field": "fiftyTwoWeekLow"})

    # Guard every lookup: `.text` on a missing (None) tag would raise, so we
    # only read `.text` when the tag was actually found.
    return {
        "price": price_tag.text if price_tag else None,
        "week_52_high": high_tag.text if high_tag else None,
        "week_52_low": low_tag.text if low_tag else None,
    }


def main():
    """Tie the pieces together: choose a symbol, fetch, parse, and print."""
    symbol = choose_symbol()

    html = get_stock_data(symbol)
    if html is None:
        # get_stock_data already printed the reason; nothing more to do.
        return

    data = parse_stock_data(html)

    print(f"\nResults for {symbol}:")
    # `or "N/A"` gives a readable fallback when a field couldn't be scraped.
    print(f"  Price:         {data['price'] or 'N/A'}")
    print(f"  52-week high:  {data['week_52_high'] or 'N/A'}")
    print(f"  52-week low:   {data['week_52_low'] or 'N/A'}")


# Only run main() when executed directly (not when imported as a module). This
# lets other files reuse get_stock_data / parse_stock_data without side effects.
if __name__ == "__main__":
    main()
