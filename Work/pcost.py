# pcost.py
#
# Exercise 1.27
import csv
from report import read_portfolio


def portfolio_cost(filename):
    'Use csv module to print total cost of portfolio.'
    total_cost = 0
    portfolio = read_portfolio(filename)
    for s in portfolio:
        total_cost += s.cost
    print('Total cost:', round(total_cost, 2))


def main(list):
    'print total cost of portfolio'
    portfolio_cost(list[1])


if __name__ == '__main__':
    import sys
    main(sys.argv)
    