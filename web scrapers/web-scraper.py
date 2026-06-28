# Import libraries and modules
import requests
from bs4 import BeautifulSoup as bsup
import os
import sys

# Import relevant files and their data
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'imports')))
from sud.sud.imports.sud_import_daily import training_stocks

def symbol():
	for i in training_stocks:
		ticker = i
	return ticker

# Fetch the webpage content
def info_source(ticker):
	content = requests.get(f'https://finance.yahoo.com/quote/{ticker}/')  # Get the URL
	return content.text

# Collect the 52-week high
def fifty2_high(content):
	fifty2_week_high = bsup(content.content, 'html.parser')  # Format the data value
	fifty2_week_high = fifty2_week_high.find('li', class_='yf-11uk5vd')
	if fifty2_week_high:
		fin_streamer = fifty2_week_high.find('fin-streamer', {'data-field': 'regularMarketPreviousClose'})
		if fin_streamer:
			data_value = fin_streamer['data-value']
			print(f"Data Value: {data_value}")
		else:
			print("fin-streamer tag with the specified data-field not found")
	else:
		print("li tag with the specified class not found")
	return fifty2_week_high, fin_streamer
