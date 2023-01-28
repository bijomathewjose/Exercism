DAYS={1: 'first',2: 'second', 3: 'third', 4: 'fourth', 
      5: 'fifth', 
      6: 'sixth', 
      7: 'seventh', 
      8: 'eighth', 
      9: 'ninth', 10: 'tenth', 11: 'eleventh', 12: 'twelfth'}
HAPPENS=[
    '',
    'two Turtle Doves, ',
    'three French Hens, ',
    'four Calling Birds, ',
    'five Gold Rings, ',
    'six Geese-a-Laying, ',
    'seven Swans-a-Swimming, ',
    'eight Maids-a-Milking, ',
    'nine Ladies Dancing, ',
    'ten Lords-a-Leaping, ',
    'eleven Pipers Piping, ',
    'twelve Drummers Drumming, '
]
def recite(start_verse, end_verse):
    return [one(i) for i in range(start_verse, end_verse+1)]
    pass
def one(verse):
    print(verse)
    header="On the "+DAYS[verse]+" day of Christmas my true love gave to me: "
    last="and a Partridge in a Pear Tree." if verse!=1 else "a Partridge in a Pear Tree."
    print(f"{header}{''.join(HAPPENS[verse-1::-1])}{last}")
    return f"{header}{''.join(HAPPENS[verse-1::-1])}{last}"
