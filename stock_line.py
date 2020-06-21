import boto3
import uuid

class StockLine():
    def __init__(self):
        self.bid = None
        self.ask = None
        self.last = None
        self.bid_size = None
        self.ask_size = None
        self.last_size = None
        self.volume = None
        self.timestamp = None
        self.last_time = None
        self.ticker = None
    def set_ticker(self, ticker):
        self.ticker = ticker
    def set_last_time(self, last_time):
        self.last_time = last_time
    def set_bid(self, bid):
        self.bid = bid
    def set_ask(self, ask):
        self.ask = ask
    def set_last(self, last):
        self.last = last
    def set_bid_size(self, bid_size):
        self.bid_size = bid_size
    def set_ask_size(self, ask_size):
        self.ask_size = ask_size
    def set_last_size(self, last_size):
        self.last_size = last_size
    def set_volume(self, volume):
        self.volume = volume
    def set_timestamp(self, timestamp):
        self.timestamp = timestamp
    def upload(self):
        #if self.last == None or self.last_size == None or self.last_time == None or self.bid == None or self.bid_size == None or self.ask == None or self.ask_size == None:
        #    return

        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('StockData')
        line = {
                'uuid': str(uuid.uuid4()),
                'ticker': str(self.ticker),
                'timestamp': str(self.timestamp),
                'last': str(self.last),
                'last_size': str(self.last_size),
                'bid': str(self.bid),
                'bid_size': str(self.bid_size),
                'ask': str(self.ask),
                'ask_size': str(self.ask_size)
                }
        print(line)
        table.put_item(Item=line)


