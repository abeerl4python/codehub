sandwich_orders=['pastrami','chicken','beef','pastrami','turkey','veggies','pastrami']
finished_sandwiches=[]

print("We're sorry, out of pastrami today.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
 sandwich_made=sandwich_orders.pop()
 print('I made your',sandwich_made,'sandwich.')
 finished_sandwiches.append(sandwich_made)

print("\n")
for x in finished_sandwiches:
    print(x, 'sandwich was made.')