# The following script creates 2 progress in the terminal.
# The code can be reformatted for use with an actual application.

# import libraries required for both examples.
import time

# Version 1
# Import the progress bar utility 'tqdm' https://pypi.org/project/tqdm/
from tqdm import tqdm

# Create a loop with which to iterate over.
for i in tqdm(range(100)):  # Use a range of 100 iterations.
    time.sleep(0.1)  # Simulate a time-consuming task.
    # Or some other set of tasks to iterate over.


# Version 2

# Import required libraries.
import multiprocessing  # This library allows us to parallelize multiple tasks.

from tqdm import tqdm  # This is the progress bar utility.


# Here we create a 'Pool' of worker processes.
def process_data(data):  # Use the parameter 'data'
    # Simulate some work using the same loop method as before
    # Include iterable = range and desc = Process name
    for i in tqdm(
        range(len(data)), desc=f"Process {multiprocessing.current_process().name}"
    ):
        pass


if __name__ == "__main__":
    # Example data to be used by our processes.
    data = [
        range(100),
        range(200),
        range(150),
    ]

    # Define the process such that creation and desctuction of processes is handled.
    # Use `map` method to apply `process_data` function to each item in the `data` iterable.
    with multiprocessing.Pool() as pool:
        pool.map(process_data, data)
