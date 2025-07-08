import sys

asset_id = sys.argv[1]
prices = app(f'prices {asset_id} | head').stdout
indicators = app(f'indicators {asset_id} | head').stdout

print(f'\nRecent data for Asset {asset_id}\n')
print(prices, indicators)
