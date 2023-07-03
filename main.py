import earthquake
import flood
import hurricane

print("\n>>>>>>Welcome to the Disaster Prediction System!<<<<<<<<\n")
print("This system predicts the occurrence of natural disasters based on weather parameters.")
print("The natural disasters that can be predicted are: ")
print("1. Earthquake")
print("2. Flood")
print("3. Hurricane")

while True:
    choice = int(input("Enter your choice (or enter 0 to exit): "))
    
    if choice == 0:
        break
    
    elif choice == 1:
        earthquake.main()

    elif choice == 2:
        flood.main()

    elif choice == 3:
        hurricane.main()

    else:
        print("Invalid choice! Please try again.")
    
    print("\n-----------------------------\n")

print("\nThank you for using the Disaster Prediction System!")
print("\nStay safe!")
print("\n-----------------------------\n")
print("\nDeveloped by: Ayushi")
