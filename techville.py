def move_forward():
    print("moving forward")

def turn(direction):
    print(f"turning {direction}")

def start_engine():
    print("starting engine")

def stop_engine():
    print("stopping engine")

def follow_roundabout(exit_number):
    print(f"taking exit number {exit_number} from the roundabout")

def navigate_to(destination):
    start_engine()
    
    if destination == "library":
        move_forward()
        turn("left")
        print("Arrived at the library.")
    
    elif destination == "tech park":
        move_forward()
        turn("right")
        print("Arrived at the tech park.")
    
    elif destination in ["hospital", "mall", "airport", "university", "stadium"]:
        move_forward()
        print("Entering the roundabout.")
        
        if destination == "hospital":
            follow_roundabout(1)
            print("Arrived at the hospital.")

        elif destination == "mall":
            follow_roundabout(2)
            move_forward()
            turn("right")
            print("Arrived at the mall.")

        elif destination == "airport":
            follow_roundabout(3)
            print("Arrived at the airport.")

        elif destination == "university":
            follow_roundabout(4)
            move_forward()
            turn("left")
            print("Arrived at the university.")

        elif destination == "stadium":
            follow_roundabout(4)
            move_forward()
            turn("right")
            print("Arrived at the stadium.")

    else:
        print("Error: Destination not recognized.")
    
    stop_engine()

navigate_to("hospital")