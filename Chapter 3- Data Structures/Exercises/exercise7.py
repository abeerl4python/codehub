list=['UK','Switzerland','Turkey','Qatar','Pakistan']

print(list)
#list in alphabetical order
print('\n',sorted(list))
print(list)

#list in reverse alphabetical order
print('\n',sorted(list,reverse=True))
print(list)

#Using reverse() to change the order of your list.
list.reverse()
print('\n',list)

#Using reverse() to change the order of your list back to original
list.reverse()
print('\n',list)

#Using sort() to change your list so it’s stored in alphabetical order.
list.sort()
print('\n',list)

#Using sort() to change your list so it’s stored in reverse alphabetical order.
list.sort(reverse=True)
print('\n',list)