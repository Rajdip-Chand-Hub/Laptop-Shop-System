from _datetime import date
from datetime import datetime
to = date.today()
print(to)
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
user_name = None
user_contact = None
user_address = None


def user_details():
    global user_name, user_contact, user_address
    user_name = input("Enter your name: ")
    contact_loop = True
    while contact_loop:
        try:
            user_contact = int(input("Enter your contact number: "))
            contact_loop = False
        except ValueError:
            print("Invalid Input")
    user_address = input("Enter your address: ")


def selling_laptop_details(laptop_list):
    x = 1
    file = open(f"{user_name}.txt", "w")
    file.write("Name = " + str(user_name) + "\n")
    file.write("Contact = " + str(user_contact) + "\n")
    file.write("Address = " + str(user_address) + "\n")
    total_Amount = 0
    for i in laptop_list:
        total_Amount += i[4]
        file.write("\nLaptop " + str(x) + "\n")
        file.write("Laptop Name = " + i[0] + "\n" + "Laptop Brand = " + i[1] + "\n" + "Quantity = " + str(i[2]) + "\n" + "Laptop Price = " + i[3] + "\n" + "Total = $" + str(i[4]) + "\n")
        print("\nLaptop " + str(x))
        print("Laptop Name = " + i[0] + "\n" + "Laptop Brand = " + i[1] + "\n" + "Quantity = " + str(i[2]) + "\n" + "Laptop Price = " + i[3] + "\n" + "Total = $" + str(i[4]) + "\n")
        x = x + 1
    file.write("\nTotal Amount = $" + str(total_Amount) + "\n")
    shipping_cost = False
    shipping_loop = True
    while shipping_loop:
        shipping = input("Dear Customer do you want your product to be shipped(Yes/No) = ")
        if shipping == "Yes":
            shipping_cost = True
            shipping_loop = False
            break
        elif shipping == "No":
            shipping_loop = False
            print("Thank You")
            break
        else:
            print("Invalid value")
    if shipping_cost == True:
        file.write("Shipping cost = $250\n")
        file.write("Total Amount with Shipping Cost = $" + str(total_Amount + 250))
        print("\nTotal Amount = $" + str(total_Amount))
        print("Shipping cost = $250")
        print("Total Amount with Shipping Cost = $" + str(total_Amount + 250) + "\n")
    file.close()


def purchasing_laptop_details(purchase_list):
    x = 1
    file = open(f"{user_name}.txt", "w")
    file.write("Name = " + str(user_name) + "\n")
    file.write("Contact = " + str(user_contact) + "\n")
    file.write("Address = " + str(user_address) + "\n")
    total_Amount = 0
    vat_amount = 0
    total_Amount_with_vat = 0
    for i in purchase_list:
        total_Amount += i[4]
        vat_amount = total_Amount * 0.13
        total_Amount_with_vat = total_Amount + vat_amount
        file.write("\nLaptop " + str(x) + "\n")
        file.write("Laptop Name = " + i[0] + "\n" + "Laptop Brand = " + i[1] + "\n" + "Quantity = " + str(i[2]) + "\n" + "Laptop Price = " + i[3] + "\n" + "Total = $" + str(i[4]) + "\n")
        x = x + 1
    file.write("\nTotal Amount of all laptops = $" + str(total_Amount) + "\n")
    file.write("Vat amount = $" + str(vat_amount) + "\n")
    file.write("Total amount with vat = $" + str(total_Amount_with_vat) + "\n")
    # print("\n" + "Laptop Name = " + i[0] + "\n" + "Quantity = " + str(i[1]) + "\n" + "Laptop Price = " + i[2] + "\n" + "Total =$" + str(i[3]))
    file.close()