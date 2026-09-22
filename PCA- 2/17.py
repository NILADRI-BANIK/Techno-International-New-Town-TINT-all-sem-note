dict = {
    "name": "Nil",
    "age": 25,
    "city": "Lake Town"
}

print("Original Dictionary:", dict)

dict["job"] = "Engineer"  
print("\nAfter adding a new key 'job':", dict)

dict["age"] = 26  
print("\nAfter modifying the value of 'age':", dict)

dict.update({"country": "India"})  
print("\nAfter using update() to add 'country':", dict)

dict.update({"city": "Lake Town", "job": "Manager"})  
print("\nAfter using update() to modify 'city' and 'job':", dict)
