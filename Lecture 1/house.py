name = input("what is your name:")

match name:
    case"Harry" | "Hermione" | "Ron":
        print("Red")
    case"Draco":
        print("Blue")
    case _:
        print("who?")
