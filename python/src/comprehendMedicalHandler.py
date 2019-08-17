import boto3


def comprehendMedicalHandler(event, context):
    try:
        print("boto3 version:"+boto3.__version__)
        client = boto3.client(service_name='comprehendmedical', region_name='us-east-1')
        print("event:", event)
        print("text: ", event["Text"])
        result = client.detect_entities(Text=event["Text"])
        return {
          "isBase64Encoded": "boolean",
          "statusCode": "200",
          "headers": {"Accept": "application/json", "Content-Type": "application/json"},
          "body": result
        }
    except Exception:
        print('Exception Caught:', Exception)
        return {
            "isBase64Encoded": "boolean",
            "statusCode": "500",
            "headers": {"Accept": "application/json", "Content-Type": "application/json"},
            "body": Exception
        }
