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
        self.high = None
        self.low = None
        self.volume = None
        self.close = None
        self.open = None
        self.date = None
        self.time = None
        self.last_time = None
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
    def set_high(self, high):
        self.high = high
    def set_low(self, low):
        self.low = low
    def set_volume(self, volume):
        self.volume = volume
    def set_close(self, close):
        self.close = close
    def set_open(self, open):
        self.open = open
    def set_date(self, date):
        self.date = date
    def set_time(self, time):
        self.time = time
    def upload(self):
        if self.last == None or self.last_size == None or self.last_time == None or self.bid == None or self.bid_size == None or self.ask == None or self.ask_size == None:
            return

        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('SPY')
        line = {
                'uuid': str(uuid.uuid4()),
                'date': str(self.date),
                'time': str(self.time),
                'last': str(self.last),
                'last_size': str(self.last_size),
                'bid': str(self.bid),
                'bid_size': str(self.bid_size),
                'ask': str(self.ask),
                'ask_size': str(self.ask_size)
                }
        print(line)
        table.put_item(Item=line)


