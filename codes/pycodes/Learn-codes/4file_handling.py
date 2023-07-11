import random   #random module>> random func
f_name = input('Type the file name: ')
f = open(f_name) # "r" omitted as it's the default
f_content = f.read()



#print(f_content)
print(type(f_content))


f_content_list = f_content.split("\n")   #Creates list from string**
print(random.choice(f_content_list))