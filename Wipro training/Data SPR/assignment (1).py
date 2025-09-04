# --------------------- Q1 ---------------------
# Create a list of 5 integers and display items. Access individual elements through index.
nums = [10, 20, 30, 40, 50]
print("List:", nums)
print("Access using index:")
for i in range(len(nums)):
    print(f"Index {i} = {nums[i]}")

# --------------------- Q2 ---------------------
# Append a new item to the end of the list.
nums.append(60)
print("\nAfter appending 60:", nums)

# --------------------- Q3 ---------------------
# Reverse the order of items in the list.
reversed_list = nums[::-1]
print("\nReversed list:", reversed_list)

# --------------------- Q4 ---------------------
# Print number of occurrences of a specified element.
element = 20
count = nums.count(element)
print(f"\nNumber of occurrences of {element}:", count)

# --------------------- Q5 ---------------------
# Append the items of list1 to list2 in the front.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list2 = list1 + list2
print("\nAfter appending list1 to the front of list2:", list2)

# --------------------- Q6 ---------------------
# Insert a new item before the second element in a list.
items = ['a', 'b', 'c', 'd']
items.insert(1, 'z')  # index 1 is before second element
print("\nAfter inserting 'z' before second element:", items)

# --------------------- Q7 ---------------------
# Remove item from a specified index.
index_to_remove = 2
if 0 <= index_to_remove < len(items):
    removed_item = items.pop(index_to_remove)
    print(f"\nAfter removing item at index {index_to_remove} ({removed_item}):", items)
else:
    print("\nInvalid index to remove.")

# --------------------- Q8 ---------------------
# Remove the first occurrence of a specified element.
element_to_remove = 'z'
if element_to_remove in items:
    items.remove(element_to_remove)
    print(f"\nAfter removing first occurrence of '{element_to_remove}':", items)
else:
    print(f"\nElement '{element_to_remove}' not found in list.")
