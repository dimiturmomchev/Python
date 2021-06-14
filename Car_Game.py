command = ""
start_command = "start - to start the car"
stop_command = "stop - to stop the car"
quit_command = "quit - to exit"
started = False
stopped = False

while True :
    command = input("")
    if command.upper()==("START"):
        if started:
            print("Car is already started!")
        else:
            started = True
            stopped = False
            print("Car started...Ready to go!")

    elif command.upper()==("STOP"):
        if stopped:
            print("Car is alredy stopped!")
        else:
            started = False
            stopped = True
            print("Car stopped.")
    elif command.upper()==("HELP"):
        print(start_command)
        print(stop_command)
        print(quit_command)
    elif command.upper() == ("QUIT"):
        break
    else:
        print("I don't understand that...")