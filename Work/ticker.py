# ticker.py

from follow import follow
import report
import csv
import tableformat


def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]
        
def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str,float,float])
    rows = make_dicts(rows, ['name','price','change'])
    return rows

    return rows

def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def filter_symbols(rows, names):
    for row in rows:
        if row['name'] in names:
            yield row

def ticker(portfolio_data, logfile, fmt):
    portfolio = report.read_portfolio(portfolio_data)
    rows = parse_stock_data(follow(logfile))
    rows = filter_symbols(rows, portfolio)
    formatter = tableformat.create_formatter(fmt)
    formatter.headings(['Name','Shares','Change'])
    for row in rows:
        formatter.row([ row['name'], f"{row['price']:0.2f}", f"{row['change']:0.2f}"] )


        
