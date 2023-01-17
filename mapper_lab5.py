#!/usr/bin/env python
"""mapper.py"""

import sys


def perform_map():

    correct_year = '2020'

    payment_type_dict = {1: 'Credit card',
                         2: 'Cash',
                         3: 'No charge',
                         4: 'Dispute',
                         5: 'Unknown',
                         6: 'Voided trip'}

    for line in sys.stdin:
        line = line.strip()
        values = line.split(',')

        try:
            payment_name = payment_type_dict[int(values[9]) if int(values[9]) != 0 else 5]
            tip_amount = float(values[13])
            month = values[1][:7]
        except ValueError:
            continue

        if values[0] == 'VendorID' or values[1][:4] != correct_year:
            pass
        else:
            print('%s\t%s\t%s\t%s' % (payment_name, month, tip_amount, 1))


if __name__ == '__main__':
    perform_map()
