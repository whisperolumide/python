# guessing game
secret_number = 7
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('you won')
        break
else:
    print('you failed')


# car game
command = ""
stopped = True
while True:
    command = input("> ").lower()
    if command == "start":
        if not stopped:
            print("car already started")
        else:
            stopped = False
            print("car started")
    elif command == "stop":
        if stopped:
            print("car already stopped")
        else:
            stopped = True
            print("car stopped")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit the game        
        """)
    elif command == "quit":
        print("game finished")
        break
    else:
        print("sorry i don't understand")

