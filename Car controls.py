command = ""
started = False
stopped = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started :
            print("The Car is already started!")
        else:
            print("Car started..")
            started = True
    elif command == "stop":
        if stopped:
            print("The car is already stopped!")
        else:
            print("Car stoped..")
            stopped = True
    elif command == "help":
        print("""
Start - To start car
Stop  - To stop Car
Quit  - To quit
        """)
    elif  command == 'quit':
        break
    else:
        print("Index not supported")


