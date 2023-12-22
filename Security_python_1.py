approved_list = ["osowle", "lsowle", "ssowle", "osowle", "bhayes", "chayes", "raireland", "roireland"]
approved_city_list = ["moraga", "orinda", "lafaytte"]

name = input("What is your name?\n")
date_input = input("what is the date\n")
date = "December,21,2023"
city_input = input("what city are you logging in from\n")



if name in approved_list:
    print("Hello and welcome to the computer\n",name)
elif date in date_input:
    print("Hello and welcome to the computer\n",name)
elif city_input in approved_city_list:
    print("Hello and welcome to the computer\n",name)
else:
    print("you are not welcome ", name, "go away")

