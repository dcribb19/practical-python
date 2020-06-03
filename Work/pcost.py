# pcost.py
#
# Exercise 1.27
import csv
import sys
cwd = 'C:/Users/danie/python_projects/practical-python/Work/'


def portfolio_cost(filename):
    'filename must be in cwd'
    total_cost = 0
    with open(cwd + filename, 'rt') as f:
        # remove headers to get to the data using next()
        next(f)
        for row_num, row in enumerate(f, start=1):
            row = row.split(',')
            try:
                total_cost += float(row[1]) * float(row[2])
            except ValueError:
                print(f'Row {row_num}: Bad row: {row}')
    
    print('Total cost:', round(total_cost, 2))


def portfolio_cost_csv(filename):
    'Use csv module to print total cost of portfolio.'
    total_cost = 0
    with open(cwd + filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row_num, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                total_cost += nshares * price
            except ValueError:
                print(f'Row {row_num}: Bad row: {row}')
        
    print('Total cost:', round(total_cost, 2))


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
