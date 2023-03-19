user1 = input("Username : ")
pass1 = input("Password : ")

if user1 == "admin" and pass1 == "420":
    print("Welcome back",user1)
    print("-------PRODUCT-------")
    milk_p = 12
    beer_p = 55
    yogurt_p = 20
    mama_p = 6
    milk = milk_p * (int(input("1.Milk 12 Bath - Amout : ")))
    beer = beer_p * (int(input("2.Beer 55 Bath - Amout : ")))
    yogurt = yogurt_p * (int(input("Yogurt 20 Bath - Amout : ")))
    mama = mama_p * (int(input("Mama 6 Bath - Amout : ")))
    result = (milk+beer+yogurt+mama)
    print("---------------------")
    print("Total : ",result)
else:
    print("Fail to login!")
