list1 = [10, 20, 30, 40, 50]
list2 = [60, 70, 80]
search = 30
if search in list1:
    print(f"{search} found in list1 at index {list1.index(search)}")
else:
    print(f"{search} not found in list1")
print("Before updation:", list1)
list1[2] = 99
print("After updating the element at index 2:", list1)
concatenated_list = list1 + list2
print("After concatenation of list1 and list2:", concatenated_list)
