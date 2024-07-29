
def laptop_dictionary():
    file = open("Laptop_Details.txt", "r")
    details_dec = {}
    laptop_id = 1
    for i in file:
        i = i.replace("\n", "")
        details_dec.update({laptop_id: i.split(",")})
        laptop_id += 1
        # print("\t\t\t  ", i)
    file.close()
    return details_dec


def laptop_table():
    print("\t___________________________________________________________________________________________________________________________________")
    print("\t\tS.N \t\t Laptop Name          Company             Price            Processor           Graphic Card            Quantity")
    print("\t___________________________________________________________________________________________________________________________________")
    file = open("Laptop_Details.txt", "r")
    a = 1
    for details in file:
        print("		", a, " 	     " + details.replace(",", "\t\t  "))
        a = a + 1
    print("\t___________________________________________________________________________________________________________________________________")
    file.close()
    print("\n")
