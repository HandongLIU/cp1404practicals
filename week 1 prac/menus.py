# Handong LIU
MENU_STRING = "(H)ello\n(G)oodbye\n(Q)uit"
Name = input("Enter name: ")
print(MENU_STRING)
choice = input(">>> ").upper()
while choice !="Q":
    if choice == "H":
        print("Hello ",Name)
    elif choice == "G":
        print("Goodbye ",Name)
    print("Invalid choice")
    print(MENU_STRING)
    choice = input(">>>").upper()
print("Finished.")