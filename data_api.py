import boto3
from boto3.dynamodb.conditions import Key

def query_date(ticker, start_date, end_date):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('StockData')

    response = table.query(
        KeyConditionExpression=Key('ticker').eq(ticker) & Key('timestamp').between(start_date, end_date)
    )
    return response['Items']

if __name__ == '__main__':
    response = query_date('TSLA', '0', '1592767038.463692')
    print(response)
