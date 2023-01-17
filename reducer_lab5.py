#!/usr/bin/env python
"""reducer.py"""

import sys


def perform_reduce():

    current_key = None
    current_count = 0
    current_tip_amount = 0
    #print('Payment type,Month,Tips average amount')

    for line in sys.stdin:
        line = line.strip()
        payment_type, month, tip_amount, count = line.split('\t')
        #print('values')
        #print(month, payment_type, tip_amount, count)
        #print('//////')

        try:
            count = int(count)
            tip_amount = float(tip_amount)
        except ValueError:
            continue

        key = payment_type + ';' + month
        #print('key ',key)

        #??????
        if current_key is None:
            current_key = key
        month, payment_type = current_key.split(';')


        if current_key == key:
            current_count += 1
            current_tip_amount += abs(tip_amount)
        else:
            try:
                print('{0},{1},{2}'.format(payment_type, month, current_tip_amount / current_count))
                #print('\n')
            except ZeroDivisionError:
                pass

            current_count = 0
            current_tip_amount = 0
            current_key = key

    try:
        #print('\n')
        print('{0},{1},{2}'.format(payment_type, month, current_tip_amount / current_count))
    except ZeroDivisionError:
        pass


if __name__ == '__main__':
    perform_reduce()
