string = 'You have entered a wrong domain'
str_list = []

for i in string.split():
    str_list.append(i)

str_list.reverse()
print(str_list)

connected_str = ''
for i in str_list:
    connected_str += i + ' '
print(connected_str)