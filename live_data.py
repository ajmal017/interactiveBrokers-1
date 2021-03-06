from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from decimal import Decimal
import datetime
import threading
import time
import json
from stock_line import StockLine

class IBapi(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)
        self.lines = {}

    def nextValidId(self, orderId):
        print("nextValidOrderId:", orderId)

    def tickSize(self, reqId, tickType, size):
        super().tickSize(reqId, tickType, size)
        if reqId not in self.lines:
            self.lines[reqId] = StockLine()
        self.lines[reqId].set_date(datetime.date.today())
        self.lines[reqId].set_time(datetime.datetime.now().time())

        if tickType == 0:
            print("bid size: " + str(size))
            self.lines[reqId].set_bid_size(size)
            self.lines[reqId].upload()
        elif tickType == 3:
            print("ask size: " + str(size))
            self.lines[reqId].set_ask_size(size)
            self.lines[reqId].upload()
        elif tickType == 5:
            print("last size: " + str(size))
            self.lines[reqId].set_last_size(size)
            self.lines[reqId].upload()


    def tickPrice(self, reqId, tickType, price, attrib):
        super().tickPrice(reqId, tickType, price, attrib)
        if reqId not in self.lines:
            self.lines[reqId] = StockLine()
        self.lines[reqId].set_date(datetime.date.today())
        self.lines[reqId].set_time(datetime.datetime.now().time())

        if tickType == 1:
            print("bid: " + str(price))
            self.lines[reqId].set_bid(price)
            self.lines[reqId].upload()
        elif tickType == 2:
            print("ask: " + str(price))
            self.lines[reqId].set_ask(price)
            self.lines[reqId].upload()
        elif tickType == 4:
            print("last: " + str(price))
            self.lines[reqId].set_last(price)
            self.lines[reqId].upload()
        elif tickType == 8:
            print("volume: " + str(price))
            self.lines[reqId].set_volume(price)
            self.lines[reqId].upload()

    def tickString(self, reqId, tickType, value):
        super().tickString(reqId, tickType, value)
        if reqId not in self.lines:
            self.lines[reqId] = StockLine()
        if tickType == 45:
            print("last timestamp: " + value)
            self.lines[reqId].set_last_time(value)
        #elif tickType == 84:
        #    print("last exchange: " + value)


def run_loop():
    app.run()

app = IBapi()
app.connect('127.0.0.1', 7498, 123)
api_thread = threading.Thread(target=run_loop, daemon=True)
api_thread.start()
time.sleep(1)

contract = Contract()
contract.symbol = 'TSLA'
contract.secType = 'STK'
contract.exchange = 'SMART'
contract.currency = 'USD'
contract.PrimaryExch = 'ISLAND'

app.reqMarketDataType(2)
reqId = 0
#while True:
app.reqMktData(reqId, contract, '', False, False, [])
    #time.sleep(20)
    #app.cancelMktData(reqId)
    #reqId += 1
#app.disconnect()

