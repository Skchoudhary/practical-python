class FormatError(Exception):
    pass

class TableFormatter:

    def headings(self, headers):
        '''
        Emit the table headings.
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit the single row of table data.
        '''
        raise NotImplementedError()
    
class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text format
    '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()

class CSVTableFormatter(TableFormatter):
    '''
    Output portfolio data in CSV format.
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))

class HTMLTableFormatter(TableFormatter):
    '''
    OUTPUT  portfolio data in HTML format
    '''
    def headings(self, headers):
        print('<tr>', end='')
        for heading in headers:
            print(f'<th>{heading}</th>', end='')
        print('</tr>')

    def row(self, rowdata):
        print('<tr>', end='')
        for data in rowdata:
            print(f'<td>{data}</td>', end='')
        print('</tr>')

        
def create_formatter(fmt):
    
    # Print it out
    if fmt == 'txt':
        formatter = TextTableFormatter()
    elif fmt == 'csv':
        formatter = CSVTableFormatter()
    elif fmt == 'html':
        formatter = HTMLTableFormatter()
    else:
        raise FormatError(f'Unknown format {fmt}')
    
    return formatter

def print_table(reportdata, attr, formatter):
    
    formatter.headings(attr)
    for data in reportdata:
        rowdata = [str(getattr(data, head)) for head in attr]
        formatter.row(rowdata)

