#####1####
user_name = input('Enter name : ')
user_age = input('your age : ')
user_street = input('your street : ')
user_city = input('your city : ')
user_country = input('your country : ')
#####2####
msg = f'''"Name: {user_name}"
"Age: {user_age}"
"Adress: {user_street},{user_city},{user_country}"'''
print(msg)
#####3####
user_age = int(user_age) -5
msg2 = f'''("Hello {{{user_name}}}, Your age is {(user_age)} Years Old,
Your Address is {user_street}, {user_city}, {user_country}.")'''
print(msg2)
#####4####
print(type(user_name),end=" ")
print(type(user_name))
print(type(user_city),end=" ")
print(type(user_country))
print(type(user_street))
####5#####
msg3 = f'''("Hello '{user_name}', How Are You? \\ """ Your Age Is "{user_age}"" + And Your Country Is: {user_country})'''
print(msg3)
####6####
msg4 = f'''("Hello '{user_name}', How Are You? \\ """ \n Your Age Is "{user_age}"" + And \n Your Country Is: {user_country})'''
print(msg4)

#####7####
name = 'Doaa Reem'
print('First letter is ' + '"' + (name[0]) + '"')
print('Third letter is ' + '"' + (name[2]) + '"')
print('Last letter is ' + '"' + (name[-1]) + '"')
#####8####
print((name[6:]))
print((name[0:5]))
print((name.upper()[2:3])+ (name[3:7]))
print((name[-1:4:-1]))
print((name[0:5:2]) + ((name[5:8:2])))
#####9#####
name_2 = "$&$&Mohammed$&$&"
print(name_2.strip('$&'))
######10###
message = "i 7% python & i 7% GSG with zakaria "
print(message.replace('7%', 'love'))
####11####
a ="hhh jjj"
b ="ola mohammed"
print(a.title())
print(a.capitalize())
print(b.title())
print(b.capitalize())
####13###
first_name = "Ola"
print('*********'+ first_name)
print('*********'+ first_name +'********')
print(first_name +'*******')
#####14###
name_one = "HaLA"
name_two = "shaHD"
print((name_one.upper()).capitalize())
print(((name_two[0:3]).upper()) +((name_two[3:]).lower()))
print(name_one.lower())
print(name_two.upper())
#####15####
print(name_one == name_one.upper())
print(name_two == name_two.lower())
#####16###
print(name_two == name_two.capitalize())
print(name_two ==(name_two[0:3] +((name_two[3:]).upper())))
#####17####
msg = "I Love Python And Although I Love GSG with Zakaria"
msg=msg.lower()
print(msg.count("love"))
#####18####
name3 = "Zakaria"
name3.find("r")