sandwich_orders=['chicken','beef','turkey','veggies']
finished_sandwiches=[]

while sandwich_orders:
 sandwich_made=sandwich_orders.pop()
 print('I made your',sandwich_made,'sandwich.')
 finished_sandwiches.append(sandwich_made)

print("\n")
for x in finished_sandwiches:
    print(x, 'sandwich was made.')