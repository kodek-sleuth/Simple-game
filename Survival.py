choose = input("Enter a tag key so as to enter the game-TAG KEYS ARE DEF,INC,SIN: ")
location = {"DEF": "You are stuck on an Island somewhere in the pacific ",
                 "INC": "You are in the desert in Namibia",
                 "SIN": "You are on Mars"}
while True:
    try:
        if choose in location.keys():
            print("You have already entered the Game")
            generate=location.get(choose)
            print(generate)
            break
        elif choose in location.keys():
            print("You have already entered the Game")
            raising=location.get(choose)
            print(raising)
            break
        elif choose in location.keys():
            print("You have already entered the Game")
            namb=location.get(choose)
            print(namb)
            break
    except:
        print("You hav entered the game but no location")


while True:
    exiting=input("Choose how you want to exit by entering in any number 1-5: ")
    exits={"1":"Go south","2":"Go west","3":"Go North","4":"Go East","5":"Call  A plane,Phone in Pocket"}
    if exiting=="1":
        yielding=exits.get(exiting)
        print(yielding)
        break

    elif exiting=="2":
        west=exits.get(exiting)
        print(west)
        break

    elif exiting=="3":
        north=exits.get(exiting)
        print(north)
        break

    elif exiting=="4":
        east=exits.get(exiting)
        print(east)
        break

    elif exiting == "5":
        call = exits.get(exiting)
        print(call)
        break

    else:
        break

class Escape(object):
    def escapingbyland(self):
        print("Truck","Lamborghini","Cross country")
        land=input("Enter which vehicle you want to use: ")
        if land=="Truck":
            print("You are using a {} nice choice ".format("Truck"))
        elif land=="Lamborghini":
            print("You are using a Lamborghini but its hard to use them in deserts ")
        elif land=="Cross country":
            print("You are using a Cross country nice choice ")

    def escapingbysea(self):
        print("Veron","Speed Boat","Jetski")
        means=input("What boat  Do you want to use: ")
        print(means)
        if means=="Veron":
            print("You are escaping with {} bad choice re run game".format("Veron"))
        elif means=="Speed Boat":
            print("You are escaping with  a {} but mind the fuel".format("Speed Boat"))
        elif means=="Jetski":
            print("You are escaping with a {}".format("Jetski"))

    def escapeonMars(self):
        print("Rocket","Space ship","Speed shoes")
        ways=input("Enter what you would like to use: ")
        if ways=="Rocket":
            print("You are escaping with a {} nice choice".format("Rocket"))
        elif ways=="Space ship":
            print("You are escaping with a {}".format("Space ship"))
        elif ways=="Speed shoes":
            print("You are escaping with {} bad choice you are going to die ".format("Speed shoes"))

escape=Escape()
print(" Where are you (Mars,Desert,Pacific Island)")
y=input()

if y=="Mars":
    escape.escapeonMars()

elif y=="Desert":
    escape.escapingbyland()

elif y=="Pacific Island":
    escape.escapingbysea()

print("*****************GAME OVER*****************")


