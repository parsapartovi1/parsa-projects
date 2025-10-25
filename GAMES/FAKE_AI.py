#for_welcoming =
print("welcome to U-THERAPY".center(100 , "_"))
role = input("How are you feeling today?(good,..) : ").lower()
age = int(input("How old are you? "))
while True :
    role_conditions = ["good", "great", "not bad", "awesome", "incredible"]
    for roles in role_conditions:
        if role in roles:
            if age < 18 :
                print("you're just too young ! you'll figure out things eventually")

    role_conditions = ["good" , "im feeling great" ,
                       "not bad" , "awesome" , "incredible"]
    for roles in role_conditions[0:4]:
        if role in roles:
            if age >= 100:
                print("are you even alive? holy moly")
                break
            if age >= 18 :
                print("I wish you feel even better !")
                help = input("Anything else that I can help you with ?").lower()
                if help == "yes" :
                    print("actually there's nothing that I could help you with !\nsee you later friend")
                    pass
                if help == "no":
                    pass
        break

    role_conditions = ["good", "great", "not bad", "awesome", "incredible"]
    for roles in role_conditions:
         if role not in roles:
            therapy = input("want some therapy? ")
            if therapy == "no":
                break
            if therapy == "yes" :
                print(f"   You're feeling {role} ?\ndon't worry son! everything will be better ,"
                      f" you just need time !\ni remember once i was a child a wise man told me:"
                      f"\n if the night is too dark ; wait till you see how bright is tomorrow . ")
            break
    role_update = input("are you feeling better now ?")
    if role_update == "yes" :
        print("Im glad that i could help ")
        break
    print("wish you comeback when you have the needed condition")

print(">>Wish you the best my friend \nWRITTEN BY PARSA")