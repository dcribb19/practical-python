# report.py
#
# Exercise 2.4
import csv
from fileparse import parse_csv

def read_portfolio(filename: str) -> list:
    '''
    Read a stock portfolio csv file into a list of dictionaries
    with keys name, shares, and price'
    '''
    with open(filename) as f:
        portfolio = parse_csv(f, select=['name', 'shares', 'price'], types=[str, int, float])
    return portfolio


def read_prices(filename: str) -> list:
    'returns a list of dicts of stock names and values from a csv file'
    with open(filename) as f:
        prices = dict(parse_csv(f, types=[str, float], has_headers=False))
    return prices


def make_report(portfolio: list, prices: dict) -> list:
    'return list of tuples with name, shares, current_price, and change'
    holdings = [(s['name'], s['shares'], prices[s['name']], prices[s['name']] - s['price']) for s in portfolio]
    return holdings


def print_report(report: list) -> str:
    'print formatted table of report'
    headers = ('Name', 'Shares', 'Price', 'Change')
    sep = ''
    print(f'{headers[0]:>10} {headers[1]:>10} {headers[2]:>10} {headers[3]:>10}')
    print(f'{sep:-^10} {sep:-^10} {sep:-^10} {sep:-^10}')
    for name, shares, price, change in report:
        print(f'{name:>10} {shares:>10d} {price:>10.2f} {change:>10.2f}')


def portfolio_report(portfolio_file, prices_file):
    'print report given a portfolio csv file and prices csv file'
    portfolio = read_portfolio(portfolio_file)
    prices = read_prices(prices_file)
    report = make_report(portfolio, prices)
    print_report(report)


def main(list):
    'print report given a portfolio csv file and prices csv file'
    portfolio = read_portfolio(list[1])
    prices = read_prices(list[2])
    report = make_report(portfolio, prices)
    print_report(report)


if __name__ == '__main__':
    import sys
    main(sys.argv)
    