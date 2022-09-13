# №23

turn_the_key = str(
    input("Is the car silent when you turn the key? Press Y if so or N for no.").upper()
)
if turn_the_key == "Y":
    battery_terminals_corroded = str(
        input("Are the battery terminals corroded? Press Y if so or N for no.").upper()
    )
    if battery_terminals_corroded == "Y":
        print("Clean terminals and try starting again.")
    if battery_terminals_corroded == "N":
        print("Replace cables and try again.")
if turn_the_key == "N":
    car_make = str(
        input("Does the car make a clicking noise? Press Y if so or N for no.").upper()
    )
    if car_make == "Y":
        print("Replace the battery.")
    if car_make == "N":
        arc_crankUp = str(
            input("Does the car crank up but fail to start? Press Y if so or N for no."
        ).upper()
    )
        if arc_crankUp == "Y":
            print("Check to ensure the choke is opening and closing.")
        if arc_crankUp == "N":
            engine_start = str(
                input("Does the engine start and then die? Press Y if so or N for no."
            ).upper()
        )
            if engine_start == "Y":
                fuel = str(
                    input("Does your car have fuel injection? Press Y if so.").upper()
                )
                if fuel == "Y":
                    print("Get it in for service.")
                if fuel == "N":
                    print("Check to ensure the choke is opening and closing.")

