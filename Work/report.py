# report.py
#
# Exercise 2.4
import csv
from fileparse import parse_csv
import stock
import tableformat

def read_portfolio(filename: str) -> list:
    '''
    Read a stock portfolio from a file into a list of dictionaries
    with keys name, shares, and price. Then, return list of Stock objects.
    '''
    with open(filename) as f:
        # parse lines into a list of dicts
        portfolio = parse_csv(f, select=['name', 'shares', 'price'], types=[str, int, float])
    # make list of Stock instances from list of dicts
    portfolio = [stock.Stock(p['name'], p['shares'], p['price']) for p in portfolio]
    return portfolio


def read_prices(filename: str) -> dict:
    'returns a dict of stock names and values from a csv file'
    with open(filename) as f:
        prices = dict(parse_csv(f, types=[str, float], has_headers=False))
    return prices


def make_report(portfolio: list, prices: dict) -> list:
    'return list of tuples with name, shares, current_price, and change'
    report = [(s.name, s.shares, prices[s.name], prices[s.name] - s.price) for s in portfolio]
    return report


def print_report(report: list, formatter):
    '''
    print formatted table of report from a list of
    (name, shares, price, change) 
    '''
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in report:
        row_data = [name, str(shares), f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(row_data)


def portfolio_report(portfolio_file, prices_file, fmt='txt'):
    ''''
    print report given a portfolio and price data files
    '''
    # Read data files
    portfolio = read_portfolio(portfolio_file)
    prices = read_prices(prices_file)
    
    # Create the report data
    report = make_report(portfolio, prices)

    # Print it out
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)


def main(list):
    'print report given a portfolio csv file and prices csv file'
    portfolio = read_portfolio(list[1])
    prices = read_prices(list[2])
    report = make_report(portfolio, prices)
    formatter = tableformat.create_formatter(list[3])
    print_report(report, formatter)


if __name__ == '__main__':
    import sys
    main(sys.argv)
