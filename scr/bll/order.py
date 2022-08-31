# Standard modules
import json
from binance.spot import Spot

# Custom modules
from scr.be.credential import bncCred

class ordertrade:
    def __init__(self) -> None:
        pass
    
    def sellordertrade(self, jm):
        print("lo vendi!")
        _cred = bncCred()
        _client = Spot(key=_cred.apiKey, secret=_cred.secret)
        _symbol = jm.get('symbola') + jm.get('symbolb')
        if jm.get('user') == "backtest":
            _time = _client.time()
            _pricesell = float(_client.avg_price(symbol=_symbol).get('price'))
            _cqq = round(_pricesell * float(jm.get('buy').get('origQty')), 6)
            _orderSell = {
                "symbol": _symbol,
                "orderId": -1,
                "orderListId": -1,
                "clientOrderId": "backtest",
                "transactTime": _time.get('serverTime'),
                "price": "0.00000000",
                "origQty": str(jm.get('buy').get('origQty')),
                "executedQty": str(jm.get('buy').get('executedQty')),
                "cummulativeQuoteQty": str(_cqq),
                "status": "FILLED",
                "timeInForce": "GTC",
                "type": "MARKET",
                "side": "SELL",
                "strategyId": -1,
                "strategyType": -1
            }
        else:
            #_orderSell = _client.new_order(symbol=_symbol, type='MARKET', side='SELL', quantity = float(jm.get('buy').get('origQty')))
            print("ufff vendi!!")
            pass
        jm['pricesell'] = _pricesell
        jm['sell'] = _orderSell
        with open('files/manual.json', 'w') as jmanual:
            json.dump(jm, jmanual,  indent=4)

