# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(lines, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse a csv file into a list of records
    '''
    if select and not has_headers:
        raise RuntimeError('select argument requires column headers')

    rows = csv.reader(lines, delimiter=delimiter)

    # Read the file headers
    if has_headers:
        headers = next(rows)

    # If a column selector was given, find indices of the specified columns.
    # Also narrow the set of headers used for resulting dictionaries
    if select:
        indices = [headers.index(colname) for colname in select]
        headers = select
    else:
        indices = []

    records = []
    for row_num, row in enumerate(rows, start=1):
        if not row:     # skips rows with no data
            continue
        # Filter the row if specific columns were selected
        if indices:
            row = [row[index] for index in indices]
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if silence_errors:
                    continue
                else:
                    print(f'Row {row_num}: Coundn\'t convert {row}')
                    print(f'Row {row_num}: Reason', e)
        if has_headers:
            # Make a dictionary
            record = dict(zip(headers, row))
            records.append(record)
        else:
            record = tuple(row)
            records.append(record)

    return records