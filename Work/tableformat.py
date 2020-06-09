# tableformat.py

class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headings.
        '''
        raise NotImplementedError()


    def row(self, row_data):
        '''
        Emit a single row of table data.
        '''
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text format.
    '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ') * len(headers))

    
    def row(self, row_data):
        for r in row_data:
            print(f'{r:>10s}', end=' ')
        print()


class CSVTableFormatter(TableFormatter):
    '''
    Output portfolio data in csv format.
    '''
    def headings(self, headers):
        print(','.join(headers))

    
    def row(self, row_data):
        print(','.join(row_data))


class HTMLTableFormatter(TableFormatter):
    '''
    Output portfolio data in HTML format.
    '''
    def headings(self, headers):
        print(headers)
        h = '<tr>'
        for header in headers:
            h += '<th>' + header + '</th>'
        h += '</tr>'
        print(h)
    

    def row(self, row_data):
        print('<tr><td>' + row_data[0] + '</td>'
              + '<td>' + row_data[1] + '</td>'
              + '<td>' + row_data[2] + '</td>'
              + '<td>' + row_data[3] + '</td></tr>'
             )


class FormatError(Exception):
    pass


def create_formatter(name):
    if name == 'txt':
        return TextTableFormatter()
    elif name == 'csv':
        return CSVTableFormatter()
    elif name == 'html':
        return HTMLTableFormatter()
    else:
        raise FormatError(f'Unknown table format {name}')


def print_table(data, col_names: list, formatter):
    '''
    Print formatted table of user-specified attributes of a list of arbitrary objects.
    '''
    formatter.headings(col_names)
    for d in data:
        row_data = [str(getattr(d, col_name)) for col_name in col_names]
        formatter.row(row_data)
