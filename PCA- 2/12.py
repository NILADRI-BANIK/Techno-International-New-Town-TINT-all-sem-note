list = [10, 20, 30, 40, 50]
del list[2]
print("After del my_list[2]:", list)
list.remove(40)
print("After remove(40):", list)
removed_element = list.pop(1)
print("After pop(1):", list)
print("Element removed using pop:", removed_element)
list.clear()
print("After clear():", list)
