#!/usr/bin/python

import argparse

# EX: prices = [1050, 270, 1540, 3800, 2]


def find_max_profit(prices):
    max_prof_current = prices[1] - prices[0]
    min_price_current = min(prices[0], prices[1])

    if len(prices) > 2:
        for x in range(2, len(prices)):
            if prices[x] - min_price_current > max_prof_current:
                max_prof_current = prices[x] - min_price_current
            if prices[x] < min_price_current:
                min_price_current = prices[x]

    return max_prof_current


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an      integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}     .".format(profit=find_max_profit(args.integers), prices=args.integers))
