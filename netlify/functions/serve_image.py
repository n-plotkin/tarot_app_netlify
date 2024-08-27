import base64
from pathlib import Path

def handler(event, context):
    query_string = event['queryStringParameters']
    image_path = query_string.get('path', '')

    if not Path(image_path).exists():
        return {
            'statusCode': 404,
            'body': 'Image not found'
        }

    with open(image_path, 'rb') as image_file:
        image_data = base64.b64encode(image_file.read()).decode('utf-8')

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'image/png',
            'Cache-Control': 'max-age=3600'
        },
        'body': image_data,
        'isBase64Encoded': True
    }
