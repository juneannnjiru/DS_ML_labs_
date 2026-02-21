#LISTS - mutable
numbers=[1,2,3,4,5]
print(numbers)   

#METHODS IN LISTS
#APPEND - Add new elements
numbers.append(6)
print(numbers)
     
#EXTEND - Differnt way to add new elements
numbers.extend([7,8,9])
print(numbers) 

#INSERT
numbers.insert(3,10)
print(numbers)
     
#REMOVE
numbers.remove(10)
print(numbers)   

#POP
popped_element= numbers.pop(5)
print(popped_element)
print(numbers)
     
#INDEX
index= numbers.index(7)
print(index)

#COUNT
count= numbers.count(8)
print(count)

#SORT
numbers.sort()
print(numbers)

#REVERSE
numbers.reverse()
print(numbers)

#TUPLES
my_numbers= (1,2,3,4)
print(my_numbers)

#METHODS IN TUPLES
#INDEX
index= my_numbers.index(4)
print(index)

#COUNT
count= my_numbers.count(1)
print(count)

#DICTIONARIES
my_dict= {"name":"Veekee","age":34,"city":"Lagos"}
print(my_dict)

#GET - Getting a value for a key in the dictionary
age= my_dict.get("age")
print(age)
     

#ITEMS - Dictionary keys and their 
items= my_dict.items()
print(items)


#KEYS
keys= my_dict.keys()
print(keys)
     
dict_keys(['name', 'age', 'city'])

#VALUES
values= my_dict.values()
print(values)
     
dict_values(['Veekee', 34, 'Lagos'])

#UPDATE
my_dict.update({"gender":["Female"]})
print(my_dict)


#DICTIONARIES WITH MULTIPLE VALUES
my_dict= dict([('name',['Bambi','Michelle','Raahat']),('age',[21,36,50]),('city',['Budapest','Bern','London'])])
print(my_dict)

     