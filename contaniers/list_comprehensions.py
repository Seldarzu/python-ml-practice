animals1=["dog","goat","sloth","tiger"]

animals2=animals1

#del animals2[1]
"""
animals3=animals1.copy()

animals4=[animal for animal in animals1]
print(animals4)"""

animals4=[animal.upper() for animal in animals1]
print(animals4)

lengths = [len(text)for text in animals1]
print(lengths)

print()

numbers1 =[3,6,3,8,5]
numbers2 =[x*x for x in numbers1]
print(numbers2)