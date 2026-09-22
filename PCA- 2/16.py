dict = {
    "name": "Niladri",
    "age": 25,
    "city": "Lake Town",
    "job": "Doctor"
}
print("Accessing values using keys:")
print("Name:", dict["name"])  
print("Age:", dict["age"])    
print("City:", dict["city"])  
print("Job:", dict["job"])    

print("\nAccessing values using get():")
print("Name:", dict.get("name"))  
print("Age:", dict.get("age"))    

print("\nAccessing a non-existing key using get():")
print("Country:", dict.get("country", "Not Found"))  

print("\nAccessing all keys and values:")
for key, value in dict.items():
    print(key, ":", value)
