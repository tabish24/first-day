# Creating a Dictionary
import pprint
Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4], 'nida': {'name': 'nnaz', 'class': '10th', 'sub': 'maths', 'marks': '20', 'salary': {'2021':'22k', 'new': '23k'}},'ilma': {'name': 'ilnaz', 'class': '10th', 'sub': 'english', 'marks': '20', 'salary': {'2021':'22k', 'new': '23k'}}}
print("Creating Dictionary: ")
pprint.pprint(Dict)
str




# accessing a element using key 
print("Accessing a element using key:") 
print(Dict['Name']) 

# accessing a element using get() 
# method 
print("Accessing a element using get:") 
print(Dict.get(1)) 

# creation using Dictionary comprehension
myDict = {x: x**2 for x in [1,2,3,4,5]}
print(myDict)
