list = []







while True: 

    action = input("""What would you like to do?

                                  Enter 1 to add item

                                  Enter 2 to remove item

                                  Enter 3 to leave the list:\n""")

    if action =="1": 
        add = input("What would you like to add?")
        list.append(add)
        print("This is what your list is" , list)

    elif action =="2":
        add = input("What do you want to remove")
        list.remove(add)

        print("This is what your list is" , list)

    else:

        print("Have a good day")

        break