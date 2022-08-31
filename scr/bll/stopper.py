# Standard modules
import json
from binance.spot import Spot

# Custom modules
from scr.be.credential import bncCred
from scr.bll.order import ordertrade

class stopper:
    def __init__(self, jm) -> None:
        self.jmanual = jm

    def setLimit(self) -> None:
        _cred = bncCred()
        _client = Spot(key=_cred.apiKey, secret=_cred.secret)
        _symbol = self.jmanual.get('symbola') + self.jmanual.get('symbolb')
        _or_stopper = self.jmanual.get('stopper')
        _avg_price = float(_client.avg_price(symbol=_symbol).get('price'))
        print(_avg_price)
        if _avg_price < _or_stopper:
            _ordertrade = ordertrade()
            _ordertrade.sellordertrade(self.jmanual)
        if (_avg_price * 0.99) > self.jmanual.get('stopper'):
            self.jmanual['stopper'] = round(_avg_price * 0.99, 2)
            with open('files/manual.json', 'w') as jmanual:
                json.dump(self.jmanual, jmanual,  indent=4)




