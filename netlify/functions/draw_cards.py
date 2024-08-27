import json
import os
from PIL import Image
from tarot_logic import draw, SIMPLE_READINGS, makeImgList

def handler(event, context):
    query_string = event['queryStringParameters']
    spread_id = query_string.get('spread', '1card')
    reading = next((r for r in SIMPLE_READINGS if r.id == spread_id), SIMPLE_READINGS[0])
    
    cards_facing = draw(reading.numcards)
    card_images = makeImgList(cards_facing)
    
    image_paths = []
    for i, img in enumerate(card_images):
        image_path = f'/tmp/{spread_id}_{i}.png'
        img.save(image_path)
        image_paths.append(image_path)
    
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps({
            'cards': [{'name': card.name, 'image': f'/.netlify/functions/serve_image?path={path}'} for card, path in zip([card for card, _ in cards_facing], image_paths)]
        })
    }
