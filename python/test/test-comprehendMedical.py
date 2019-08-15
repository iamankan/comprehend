import boto3
client = boto3.client(service_name='comprehendmedical', region_name='us-east-2')
doc = """
cerealx 84 mg daily
"""
result = client.detect_entities(Text= doc)
print(result)
entities = result['Entities'];
for entity in entities:
    print('Entity', entity)