dict = {
    "person1": {"name": "Nil", "age": 30, "city": "Kolkata"},
    "person2": {"name": "Nimo", "age": 20, "city": "Lake Town"},
    "person3": {"name": "Ram", "age": 39, "city": "Barasat"}
}
for person, details in dict.items():
    print(f"\nDetails of {person}:")
    for key, value in details.items():
        print(f"{key}: {value}")
