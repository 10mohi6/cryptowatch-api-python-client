# coding: utf-8
import requests

class Client():

	def __init__(self, **kwargs):
		self.origin = kwargs.get('origin', 'https://api.cryptowat.ch')
		self.timeout = kwargs.get('timeout', None)

	def _request(self, path, headers=None, method='GET', params=None):
		uri = '{0}{1}'.format(self.origin, path)
		res = requests.get(uri, headers=headers, timeout=self.timeout, params=params)

		return res

	def get_allowance(self, **kwargs):
		path = ''

		data = self._request(path)

		return data

	def get_assets(self, **kwargs):
		path = '/assets'
		params = kwargs
		if len(params) > 0:
			path += '/{0}'.format(params['asset'])

		data = self._request(path)

		return data

	def get_pairs(self, **kwargs):
		path = '/pairs'
		params = kwargs
		if len(params) > 0:
			path += '/{0}'.format(params['pair'])

		data = self._request(path)

		return data

	def get_exchanges(self, **kwargs):
		path = '/exchanges'
		params = kwargs
		if len(params) > 0:
			path += '/{0}'.format(params['exchange'])

		data = self._request(path)

		return data

	def get_markets(self, **kwargs):
		path = '/markets'
		params = kwargs
		if len(params) > 0:
			if 'exchange' in params:
				path += '/{0}'.format(params['exchange'])
				if 'pair' in params:
					path += '/{0}'.format(params['pair'])

		data = self._request(path)

		return data

	def get_markets_price(self, **kwargs):
		params = kwargs
		path = '/markets/{0}/{1}/price'.format(params['exchange'], params['pair'])

		data = self._request(path)

		return data

	def get_markets_summary(self, **kwargs):
		params = kwargs
		path = '/markets/{0}/{1}/summary'.format(params['exchange'], params['pair'])

		data = self._request(path)

		return data

	def get_markets_trades(self, **kwargs):
		params = kwargs
		path = '/markets/{0}/{1}/trades'.format(params['exchange'], params['pair'])

		data = self._request(path, params=params)

		return data

	def get_markets_orderbook(self, **kwargs):
		params = kwargs
		path = '/markets/{0}/{1}/orderbook'.format(params['exchange'], params['pair'])

		data = self._request(path)

		return data

	def get_markets_ohlc(self, **kwargs):
		params = kwargs
		path = '/markets/{0}/{1}/ohlc'.format(params['exchange'], params['pair'])

		data = self._request(path, params=params)

		return data

	def get_markets_prices(self, **kwargs):
		path = '/markets/prices'

		data = self._request(path)

		return data

	def get_markets_summaries(self, **kwargs):
		path = '/markets/summaries'

		data = self._request(path)

		return data
