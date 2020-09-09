import os
import time

def follow(file):
    with open(file) as lines:
        for line in lines:
            yield line

def filematch(lines, substr):
    for line in lines:
        if substr in line:
            yield line

def filematch(lines, substr):
    for line in lines:
        if substr in line:
            yield line
                
if __name__ == '__main__':
    import report
    portfolio = report.read_portfolio('Data/portfolio.csv')
    
    for line in follow('Data/stocklog.csv'):
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if name in portfolio:
            print(f'{name:>10s} {price:>10.2f} {change:>10.3f}')
