def everything():
    while True:
        print("1 Add")
        print("2 Subtract")
        print("3 Multiply")
        print("4 Divide")
        print("5 Quit")

        choice = input("Choice: ")

        if choice == "1":
            x = input("First: ")
            y = input("Second: ")
            x = float(x)
            y = float(y)
            result = x + y
            print("Answer:", result)

        elif choice == "2":
            x = input("First: ")
            y = input("Second: ")
            x = float(x)
            y = float(y)
            result = x - y
            print("Answer:", result)

        elif choice == "3":
            x = input("First: ")
            y = input("Second: ")
            x = float(x)
            y = float(y)
            result = x * y
            print("Answer:", result)

        elif choice == "4":
            x = input("First: ")
            y = input("Second: ")
            x = float(x)
            y = float(y)
            if y == 0:
                print("Error")
            else:
                result = x / y
                print("Answer:", result)

        elif choice == "5":
            break
        else:
            print("Bad input")


everything()