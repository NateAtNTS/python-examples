import os
import pathlib
import csv

# pip3 install python-dotenv
from dotenv import load_dotenv
load_dotenv()
# print(os.getenv("MY_SAMPLE_VARIABLE"))

# get the base path of the project
BASE_PATH = pathlib.Path(__file__).parent.absolute()

books = [
    'LOTR',
    'Foundation',
    'WingFeather Saga',
    "Chronicles of Narnia",
    "The Green Ember Series",
    "The Mysterious Benedict Society"
]

my_tuple = (10, 20, 30, 40)

# Get a list of names from CSV
names_csv_file = open(str(BASE_PATH) + "/names.csv", "r")
names_csv = csv.reader(names_csv_file)
names = []
row_count = 0
cell_count = 0
for row in names_csv:
    for cell in row:
        if cell_count != 0:  # for this list, I do not include the column name which is first in the list
            names.append(cell)
        cell_count = cell_count + 1

dividing_line = "-----------------------------------------------------"
