import read
import write
import operations


def shop_name():
    print("\t\t\t\t\t\t\t\t\t\t\t                Welcome To")
    print("\t\t\t\t\t\t\t\t\t\t\t             Digital Tech Nepal")
    print("\t\t\t\t\t\t\t\t\t\t\t Labim Mall, Lalitpur | Contact Number: 9804500677")
    print("\n")


def system_entry():
    print("===============================================")
    print("Please Select A Option According To Your Need")
    print("===============================================")
    print("\n")
    print("Press 1 for selling laptops")
    print("Press 2 for purchasing laptops")
    print("Press 3 for exiting from system")
    print("\n")
    print("================================================")
    print("\n")


def laptop_buy_sell():
    shop_name()
    read.laptop_table()
    system_entry()
    laptop = True
    while laptop:
        try:
            laptop_system = int(input("Select any option above to continue: "))
            print("\n")

            if laptop_system == 1:
                write.user_details()
                main_loop = True
                while main_loop:
                    product_id = operations.laptop_id_function()
                    quantity = operations.laptop_quantity(product_id)
                    laptop_list = operations.laptop_bill(product_id, quantity)
                    print("\n")
                    print("Dear User, if you want to sell another laptop")
                    print("Press 1")
                    print("Dear User, if you do not want to sell another laptop")
                    print("Press 2")
                    loop = True
                    while loop:
                        user_input = int(input("Select one option = "))
                        if user_input == 1:
                            loop = False
                        elif user_input == 2:
                            loop = False
                            main_loop = False
                            write.selling_laptop_details(laptop_list)
                        else:
                            print("Your entered option", user_input, "does not match our requirement")

                print("Thanks for selling laptop")
                print("\n")
                system_entry()
            elif laptop_system == 2:
                write.user_details()
                purchase_loop = True
                while purchase_loop:
                    purchase_id = operations.laptop_id_function()
                    Quantity = operations.laptop_quantity_purchase(purchase_id)
                    purchase_list = operations.laptop_bill_purchase(purchase_id, Quantity)
                    print("\n")
                    print("Dear User, if you want to sell another laptop")
                    print("Press 1")
                    print("Dear User, if you do not want to sell another laptop")
                    print("Press 2")
                    loop_purchase = True
                    while loop_purchase:
                        user_input = int(input("Select one option = "))
                        if user_input == 1:
                            loop_purchase = False
                        elif user_input == 2:
                            loop_purchase = False
                            purchase_loop = False
                            write.purchasing_laptop_details(purchase_list)
                        else:
                            print("Your entered option", user_input, "does not match our requirement")
                print("Thanks for purchasing laptop")
                print("\n")
                system_entry()
            elif laptop_system == 3:
                laptop = False
                print("Thanks For Visiting Us\nHava A Good Day!!!")
                print("\n")
            else:
                print("Your entered option", laptop_system, "does not match our requirement")
                print("\n")
                system_entry()
        except ValueError:
            print("Invalid Input Enter correct value")
            system_entry()


laptop_buy_sell()
