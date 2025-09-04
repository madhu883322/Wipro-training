try:
    filename = input("Enter the file name: ") + ".txt"
    with open(filename, 'r') as file:
        lines = file.readlines()

    total_items = 0
    free_items = 0
    total_amount = 0
    discount = 0

    for line in lines:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        if len(parts) != 2:
            continue
        item, price = parts
        total_items += 1
        if price.lower() == "free":
            free_items += 1
        elif item.lower() == "discount":
            discount = int(price)
        else:
            total_amount += int(price)

    final_amount = total_amount - discount

    print("No of items purchased:", total_items)
    print("No of free items:", free_items)
    print("Amount to pay:", total_amount)
    print("Discount given:", discount)
    print("Final amount paid:", final_amount)

except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print("Error:", e)


