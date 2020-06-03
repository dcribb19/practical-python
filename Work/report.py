# report.py
#
# Exercise 2.4
import csv

def read_portfolio(filename):
    'returns list of dictionaries with stock name, shares, and prices'
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        types = [str, int, float]
        for row in rows:
            record = {name : func(val) for name, func, val in zip(headers, types, row)}
            portfolio.append(record)
    return portfolio


def read_prices(filename):
    'returns a dictionary of stock names and values'
    prices = {}
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        for row in rows:
            if len(row) == 2:
                prices[row[0]] = float(row[1])
    return prices


def gain_loss(portfolio, prices):
    'calculate total gain/loss of portfolio'
    total_cost = 0.0
    current_value = 0.0

    for s in portfolio:
        total_cost += s['shares'] * s['price']
        if s['name'] in prices.keys():
            current_value += s['shares'] * prices[s['name']]
        else:
            current_value += s['shares'] * s['price']
    gain_loss = current_value - total_cost
    print('Current Value', current_value, 'Gain/Loss', round(gain_loss, 2))


def make_report(portfolio, prices):
    'return list of tuples with name, shares, current_price, and change'
    holdings = []
    for s in portfolio:
        holdings.append((s['name'], s['shares'], prices[s['name']],
                         prices[s['name']] - s['price']
                        )
                       )

    return holdings


def print_report(report):
    'print formatted table of report'
    headers = ('Name', 'Shares', 'Price', 'Change')
    sep = ''
    print(f'{headers[0]:>10} {headers[1]:>10} {headers[2]:>10} {headers[3]:>10}')
    print(f'{sep:-^10} {sep:-^10} {sep:-^10} {sep:-^10}')
    for name, shares, price, change in report:
        print(f'{name:>10} {shares:>10d} {price:>10.2f} {change:>10.2f}')
