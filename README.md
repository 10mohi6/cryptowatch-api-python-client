# cryptowatch-client

[![PyPI version](https://badge.fury.io/py/cryptowatch-client.svg)](https://badge.fury.io/py/cryptowatch-client)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

cryptowatch-client is a python client library for [cryptowatch public market rest api](https://cryptowat.ch/docs/api)


## Installation

    $ pip install cryptowatch-client

## Usage

```python
from cryptowatch_client import Client

client = Client(timeout=30)
response = client.get_allowance()
print(response.status_code, response.json())


client.get_allowance() # GET /
client.get_assets() # GET /assets
client.get_assets(asset='btc') # GET /assets/btc
client.get_pairs() # GET /pairs
client.get_pairs(pair='ethbtc') # GET /pairs/ethbtc
client.get_exchanges() # GET /exchanges
client.get_exchanges(exchange='kraken')  # GET /exchanges/kraken
client.get_markets() # GET /markets
client.get_markets(exchange='kraken') # GET /markets/kraken
client.get_markets(exchange='gdax', pair='btcusd') # GET /markets/gdax/btcusd
client.get_markets_price(exchange='gdax', pair='btcusd') # GET /markets/gdax/btcusd/price
client.get_markets_summary(exchange='gdax', pair='btcusd') # GET /markets/gdax/btcusd/summary
client.get_markets_trades(exchange='gdax', pair='btcusd') # GET /markets/gdax/btcusd/trades
client.get_markets_trades(exchange='gdax', pair='btcusd', limit=100, since=1481663244) # GET /markets/gdax/btcusd/trades
client.get_markets_orderbook(exchange='gdax', pair='btcusd') # GET /markets/gdax/btcusd/orderbook
client.get_markets_ohlc(exchange='gdax', pair='btcusd') # GET /markets/gdax/btcusd/ohlc
client.get_markets_ohlc(exchange='gdax', pair='btcusd', before=1481663244, after=1481663244, periods='60,180,108000') # GET /markets/gdax/btcusd/ohlc
client.get_markets_prices() # GET /markets/prices
client.get_markets_summaries() # GET /markets/summaries
```

## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request