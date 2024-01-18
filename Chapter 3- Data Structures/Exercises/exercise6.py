list=['Elena','Stefan','Caroline']
print(list[0],",You are invited to dinner!")
print(list[1],",You are invited to dinner!")
print(list[2],",You are invited to dinner!")

print('\nSorry,',list[2],"can't come to dinner.")

#Inserting a new guest
del list[2]
list.insert(2,'Belle')

#print the invitations again
print('\n',list[0],",You are invited to dinner!")
print(list[1],",You are invited to dinner!")
print(list[2],",You are invited to dinner!")

#Oh no, we have space for only two persons
print('\n','Sorry,We have space for only two people')

#Remove guests from the list

list.pop(-3)
print('Sorry,',list[0],'We have space for only two people')



#Invite the two people
print('\n',list[1],'You are still invited to dinner.')
print(list[0],'You are still invited to dinner.')

del list[1]
del list[0]


print(list)       

