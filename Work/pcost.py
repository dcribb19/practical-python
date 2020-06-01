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
        for line in f:
            line = line.split(',')
            try:
                total_cost += float(line[1]) * float(line[2])
            except ValueError:
                print('Warning: could not convert string to float')
                if len(line[1]) == 0:
                    print('Shares is empty.')
                elif len(line[2]) == 0:
                    print('Price is empty.')
    
    print('Total cost:', round(total_cost, 2))


def portfolio_cost_csv(filename):
    'Use csv module to print total cost of portfolio.'
    total_cost = 0
    with open(cwd + filename, 'rt') as f:
        rows = csv.reader(f)
        # take headers out with next()
        next(rows)
        for row in rows:
            total_cost += float(row[1]) * float(row[2])
        
    print('Total cost:', round(total_cost, 2))


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

portfolio_cost_csv(filename)
