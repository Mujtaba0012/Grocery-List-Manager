grocery_list = []

print("Wlcome to the Grocery List Manager!")
print("Option:1. Add 2.Remove 3.View 4.Exist")

while True:

    choice = input("\n Enter your choice(1/2/3/4):")

    if choice == "1":
        item = input("enter the item to add:")

        grocery_list.append(item)
        print(f"'{item}' has been added to your list.")

    elif choice == "2":
        item = input("Enter the item to remove:")
        if item in grocery_list:
            grocery_list.remove(item)
            print(f"'{item}'entre the item to remove:")
        else:
            print(f"'{item}'is not in the list.")

    elif choice == "3":
                 if grocery_list:
                  print("\nYour grocery List:")
                 for idx, item in enumerate(grocery_list, start=1):
                     print(f"{idx}.{item}")
                 else:
                    print("\nYour grocery list is empty.")

    elif choice == "4":
                 
                 print("exiting grocery list manager. Goodbye!")

                 break
    
    else:
        
        print("Invalid choice! Please try again.")

                  
            