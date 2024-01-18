pets=[]

pet={
    ' owners name':'Stefan',
    'name':'Bruno'
}
pets.append(pet)

pet={
    'owners name':'Eric',
    'name':'Mars'
}
pets.append(pet)

pet={
    'owners name':'Elena',
    'name':'Tiger'
}
pets.append(pet)

for pet in pets:
    print( 'Heres what I know about', pet['name'],':')
    for x,y in pet.items():
     print(x,':',str(y))
