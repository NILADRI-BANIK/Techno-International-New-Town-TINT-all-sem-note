dict = {
    "name": "Nil",
    "age": 25,
    "city": "Kolkata",
    "job": "Doctor"
}
print("Original Dictionary:", dict)

del dict["city"]   
print("\nAfter using del to remove 'city':", dict)

removed_item = dict.pop("age")  
print("\nAfter using pop() to remove 'age':", dict)
print("Removed item using pop:",removed_item)

removed_item = dict.popitem()   
print("\nAfter using popitem() to remove an arbitrary item:", dict)
print("Removed item using popitem:",removed_item)

