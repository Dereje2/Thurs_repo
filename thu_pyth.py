# data types - String, List, Tuple, Dict and set

# String - immutable

s1 = "Welcome to The First Session"

#index
# print(s1[-15])

# substring/slicing
print(s1[2:5]) #lco
print(s1[:8])
print(s1[2:-1])
print(s1[::-1]) # reverse a string using slicing


# manipulation funcs / methods

# res = s1.index('First')
# print(res)

# ind = s1.find("Fist") 
# print(ind)


# s2 = s1.replace("First", "1st")
# print(s2)



# s2 = s1.capitalize()
# print(s2)


# format
# name = "John"
# city = "Kansas"
# # print("hello I am {}. I am from {}".format(name, city))

# # split - separating

# # res = s1.split("xyz") # split returns always a list
# # print(res)

# # strip - 
# # print("Before strip", s1)
# # res = s1.strip("p")
# # print("After strip", res)


# # is related func
# # s1 = "he1l2l3o4w5o6rldfdasg"
# s1 = "2456a4356"
# res = s1.isnumeric()
# print(res)




# # List - mutable - heterogeneous data type - []

# # l1 = [1,1.123, True, "Hello"]
# # l1 = [1,2,3,4,5]
# # l1 = ['a','b','c']
# l1 = [21,23,14,32,20,19]
# # index and slicing
# print(l1[::-1])

# # list manipulations
# l1.append(100)
# print(l1)

# l1.insert(2,222)
# print(l1)
# l2 = [1,1,1,1]

# to merge two lists
# l1.extend(l2)
# print(l1)

# remove by index
# l1.pop(2)
# print("After pop", l1)

# remove by value
# l1.remove(100)
# print("After remove", l1)


# # l1 = [1,"hello", True]
# l1.sort(reverse=True)
# print("sorted list",l1)


# l1.reverse()
# print("reversed",l1)

# l1.clear()
# print("clear", l1)


# l2 = l1.copy()
# print(l2)


# ind = l1.count(1)
# print(ind)

# string to a list
# s1 = "Hello World"
# l1 = list(s1)
# print(l1)


# llist to string
# l1 = ["a","b","d","g"]
# s1 = "".join(l1)
# print(s1)


# Dictionary - mutable - {} - index and slicing - unordered

d1 = {"apple": 5, "banana":3, "mango":5, "orange":7}
# print(d1)
# manipulations

# d1['pineapple'] = 9
# print(d1)


# d1.update({'xyz':11, 'pqr':20})
# print(d1)

# d1.pop("mango") # removes the mango kv pair
# print("After POP", d1)

# d1.popitem() # removes the last kv pair
# print("After popitem", d1)

# k = d1.keys()
# print(k)

# v = d1.values()
# print(v)

# i = d1.items()
# print(i)

# d1.clear()
# print(d1)

# does nothing if the key already exists; else it will create a new kv pair
# d1.setdefault("ssiw", 22)
# print(d1)

# d2 = d1.fromkeys([1,2,3,4], "xyz")
# print(d2)




# tuple - immutable - () - index and slicing

# t1 = (2,3,1,5,7,11)

# print(t1[2:5])
# occ = t1.count(2)
# t1.replace(12)


# condition statemenets - if, elif and else
# blocks - if,elif,else,for,while,try,catch,def,class
# block first line should end with colon and from second line its housld have indents


age = 15
# if(age>18):
#     print("Eligible")
#     print("Congrats")
# else:
#     print("Not Eligible")

marks = 55
if(marks>85 and marks<=100):
   print("Grade A")
elif(marks>70 and marks<=85):
    print("Grade B")
elif(marks>45 and marks<=70):
    print("Grade C")
else:
     print("Grade D")

"""
1. Else/elif needs an IF before them
2 one If can have mul elifs but onlyy single else    
3. If one of the block in if/elif/else is executed, all others blocks will bypass    
    """
# age = 20
# if(age>9):
#     print("bye")
# elif(age>10):
#     print("Hello")
# elif(age>12):
#     print("Good morning")
# else:
#     print("Welcome")


country = "India"
state = "KN"
city = "Hubli"

#  Nested If conditions

# if(country=="India"):
#     print("Welcome to India")
#     if(state=="KN"):
#         print("Welcome to KN")
#         if(city=="Bangalore"):
#             print("Welcome to Bangalore")
#         else:
#             print("Not in Bangalore")
#     else:
#         print("Not In KN")
# else:
#     print("You are outside of India")

# Loops - for and while


# ip = "Hello World Welcome To The World Of Coding"

# for i in ip:
#     if(i.islower()):
#         print(i,end=" ")


# l1 = [21,23,33,24,32,18]

# for i in l1:
#     if(i%2==1):
#         print(i)


d = {'john':23, 'madhie': 27, 'lilly':31, 'rob': 30, 'calres': 28}

for i in d:
    if(d[i]>25):
        print(i, d[i])





























