import requests

class CoinbaseApi(object):

    def _clean(self, list):
        return [item[0:2] for item in list]

    def _flatten(self, book):
        return [item for sublist in book for item in sublist]

    def _sort_book(self, list, type):
        reverse_bool =  True if type == 'bids' else False 
        return sorted(list, key=lambda x: float(x[0]), reverse = reverse_bool)

    def _request(self, endpoint):
        try:
            response = requests.get(endpoint)
            if response.status_code != 200:
                print("Something went wrong, bad response")
            response_dict = response.json()
        except:
            print("Something went wrong")
        return response_dict



    def get_bitcoin_quote(self):
        coinbase_endpoint = 'https://api.pro.coinbase.com/products/BTC-USD/book?level=2'

        all_asks_list = []
        all_bids_list = []
        response_dict = self._request(coinbase_endpoint)
        all_asks_list.append(self._clean(response_dict['asks']))
        all_bids_list.append(self._clean(response_dict['bids']))

        sorted_all_asks_list = self._sort_book(self._flatten(all_asks_list), 'asks')
        sorted_all_bids_list = self._sort_book(self._flatten(all_bids_list), 'bids')
        
        return {'ask' : max(sorted_all_asks_list[1]) , 'bid' : max(sorted_all_bids_list[1])}