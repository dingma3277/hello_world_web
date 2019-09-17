from sys import argv

prompt = '> '
age = input("How old are you? \n" + prompt)
print(age)

script, first, second, third = argv
print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third


