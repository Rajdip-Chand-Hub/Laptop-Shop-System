import read


def laptop_id_function():
    laptop_id = None
    buy_another = True
    while buy_another:
        id_loop = True
        while id_loop:
            try:
                laptop_id = int(input("Enter the laptop's ID = "))
                id_loop = False
                buy_another = False
            except ValueError:
                print("Invalid Laptop Id")
        dictionary_laptop = read.laptop_dictionary()

        while laptop_id <= 0 or laptop_id > len(dictionary_laptop):
            print("Invalid ID")
            print("\n")
            laptop_id = int(input("Enter the laptop's ID = "))
        for x in dictionary_laptop.keys():
            if x == laptop_id:
                print("Selected Laptop Name = ", dictionary_laptop[laptop_id][0])
        return laptop_id


def laptop_quantity(laptop_id):
    dictionary_laptop = read.laptop_dictionary()
    laptop_quantity = dictionary_laptop[laptop_id][5]
    Selected_Quantity = int(input("Select Quantity = "))
    while Selected_Quantity <= 0 or Selected_Quantity > int(laptop_quantity):
        print("Quantity No Available")
        print("\n")
        Selected_Quantity = int(input("Select Quantity = "))

    dictionary_laptop[laptop_id][5] = int(dictionary_laptop[laptop_id][5]) - int(Selected_Quantity)
    laptop_file = open("Laptop_Details.txt", "w")
    for i in dictionary_laptop.values():
        laptop_file.write(
            str(i[0]) + "," + str(i[1]) + "," + str(i[2]) + "," + str(i[3]) + "," + str(i[4]) + "," + str(i[5]))
        laptop_file.write("\n")
    laptop_file.close()
    print("\n")
    return Selected_Quantity


user_purchase_laptop_list = []


def laptop_bill(laptop_id, Selected_Quantity):
    global user_purchase_laptop_list
    dictionary_laptop = read.laptop_dictionary()
    laptop_name = dictionary_laptop[laptop_id][0]
    laptop_brand = dictionary_laptop[laptop_id][1]
    user_quantity = Selected_Quantity
    laptop_actual_price = dictionary_laptop[laptop_id][2]
    selected_laptop_actual_price = dictionary_laptop[laptop_id][2].replace("$", '')
    amount_to_pay = int(selected_laptop_actual_price) * int(user_quantity)
    user_purchase_laptop_list.append([laptop_name, laptop_brand, user_quantity, laptop_actual_price, amount_to_pay])
    print(user_purchase_laptop_list)
    return user_purchase_laptop_list

# Purchase code


def laptop_quantity_purchase(laptop_id):
    dictionary_laptop = read.laptop_dictionary()
    laptop_quantity = dictionary_laptop[laptop_id][5]
    Selected_Quantity = int(input("Select Quantity = "))
    while Selected_Quantity <= 0 or Selected_Quantity > int(laptop_quantity):
        print("Quantity No Available")
        print("\n")
        Selected_Quantity = int(input("Select Quantity = "))

    dictionary_laptop[laptop_id][5] = int(dictionary_laptop[laptop_id][5]) + int(Selected_Quantity)
    laptop_file = open("Laptop_Details.txt", "w")
    for i in dictionary_laptop.values():
        laptop_file.write(
            str(i[0]) + "," + str(i[1]) + "," + str(i[2]) + "," + str(i[3]) + "," + str(i[4]) + "," + str(i[5]))
        laptop_file.write("\n")
    laptop_file.close()
    print("\n")
    return Selected_Quantity


purchase_laptop_list = []


def laptop_bill_purchase(laptop_id, Selected_Quantity):
    global purchase_laptop_list
    dictionary_laptop = read.laptop_dictionary()
    laptop_name = dictionary_laptop[laptop_id][0]
    laptop_brand = dictionary_laptop[laptop_id][1]
    user_quantity = Selected_Quantity
    laptop_actual_price = dictionary_laptop[laptop_id][2]
    selected_laptop_actual_price = dictionary_laptop[laptop_id][2].replace("$", '')
    amount_to_pay = int(selected_laptop_actual_price) * int(user_quantity)
    purchase_laptop_list.append([laptop_name, laptop_brand, user_quantity, laptop_actual_price, amount_to_pay])
    return purchase_laptop_list




