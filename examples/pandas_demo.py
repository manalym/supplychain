#!/usr/bin/env python3
"""
Simple pandas demo:
- create a DataFrame
- show basic stats
- compute derived column (revenue)
- group and aggregate
- save output CSVpip
"""

import pandas as pd


def main():
    data = {
        'product': ['A', 'B', 'A', 'C', 'B', 'A'],
        'region': ['North', 'South', 'East', 'West', 'North', 'East'],
        'units': [10, 15, 7, 12, 9, 4],
        'price': [2.5, 3.0, 2.5, 4.0, 3.0, 2.5],
    }

    df = pd.DataFrame(data)
    print('DataFrame:')
    print(df)

    print('\nSummary stats:')
    print(df.describe(include='all'))

    # derived column
    df['revenue'] = df['units'] * df['price']
    print('\nWith revenue:')
    print(df)

    # group and aggregate
    print('\nGroup by product (sum units and revenue):')
    grouped = df.groupby('product').agg({'units': 'sum', 'revenue': 'sum'}).reset_index()
    print(grouped)

    # filter example
    print('\nFilter: products with total units > 10')
    totals = df.groupby('product')['units'].sum()
    print(totals[totals > 10])

    # save result
    out = 'examples/output_summary.csv'
    grouped.to_csv(out, index=False)
    print(f"\nSaved grouped summary to {out}")


if __name__ == '__main__':
    main()
