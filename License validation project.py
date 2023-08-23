user_age = int(input("please put your age? \n"))
if user_age == 18:
    print("good that is the first step")
    car_license = input("do you have a ride license? \n")
    if car_license.lower() == "yes":
        print("you can have a car")
    else:
        print("you must have a ride license")
else:
    print("you have to be 18")