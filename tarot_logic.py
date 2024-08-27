import random
from PIL import Image
from models import Card, Deck, MajorMinor, Facing, SIMPLE_READINGS
from os import path

def draw(n: int, chosenDeck: Deck = SIMPLE_READINGS[0].imgfunc, invert=True, majorminor: MajorMinor = MajorMinor.BOTH):
    cards = []
    if majorminor == MajorMinor.BOTH:
        cards = chosenDeck.all_cards
    elif majorminor == MajorMinor.MAJOR_ONLY:
        cards = chosenDeck.major_cards
    elif majorminor == MajorMinor.MINOR_ONLY:
        cards = chosenDeck.minor_cards

    if n < 1 or n > len(cards):
        raise ValueError(f"Number of cards must be between 1 and {len(cards)}")

    hand = random.sample(cards, n)

    return [
        (
            (card, Facing.UPRIGHT)
            if not invert
            else (card, random.choice((Facing.UPRIGHT, Facing.REVERSED)))
        )
        for card in hand
    ]

def makeImgList(cards):
    imgarray = []
    for card, facing in cards:
        newcard = Image.open(card.image_path).convert("RGBA")
        if facing == Facing.REVERSED:
            newcard = newcard.rotate(180, expand=True)
        imgarray.append(newcard)
    return imgarray
