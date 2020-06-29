import boto3
from boto3.dynamodb.conditions import Key

def query_date(ticker, start_date, end_date, last_key=None):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('RawStockData')

    if last_key is None:
        response = table.query(
            KeyConditionExpression=Key('ticker').eq(ticker) & Key('timestamp').between(start_date, end_date)
        )
    else:
        response = table.query(
            KeyConditionExpression=Key('ticker').eq(ticker) & Key('timestamp').between(start_date, end_date),
            ExclusiveStartKey=last_key
        )

    items = response['Items'] if response['Count'] > 0 else []
    if "LastEvaluatedKey" in response:
            items.extend(query_date(ticker, start_date, end_date, last_key=response["LastEvaluatedKey"]))

    return items
