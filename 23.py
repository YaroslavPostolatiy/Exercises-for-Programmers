# №23

turnTheKey = str(input("Is the car silent when you turn the key? Press Y if so or N for no.").upper())
if turnTheKey == "Y":
    batteryTerminalsCorroded = str(input("Are the battery terminals corroded? Press Y if so or N for no.").upper())
    if batteryTerminalsCorroded == "Y":
        print("Clean terminals and try starting again.")
    if batteryTerminalsCorroded == "N":
        print("Replace cables and try again.")
if turnTheKey == "N":
    carMake = str(input("Does the car make a clicking noise? Press Y if so or N for no.").upper())
    if carMake == "Y":
        print("Replace the battery.")
    if carMake == "N":
        arcCrankUp = str(input("Does the car crank up but fail to start? Press Y if so or N for no.").upper())
        if arcCrankUp == "Y":
            print("Check to ensure the choke is opening and closing.")
        if arcCrankUp == "N":
            engineStert = str(input("Does the engine start and then die? Press Y if so or N for no.").upper())
            if engineStert == "Y":
                fuel = str(input("Does your car have fuel injection? Press Y if so.").upper())
                if fuel == "Y":
                    print("Get it in for service.")
                if fuel == "N":
                    print("Check to ensure the choke is opening and closing.")

