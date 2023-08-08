from Punch import Punches
import time

def main():
    punch_system = Punches()

    while True:
        
        time.sleep(0.5)
        print("1. Add User")
        
        time.sleep(0.1)
        print("2. Clock In")


        time.sleep(0.1)
        print("3. Clock Out")

        time.sleep(0.1)
        print("4. Remove User")

        time.sleep(0.1)
        print("5. Display Users")

        time.sleep(0.1)
        print("6. Display Logs")

        time.sleep(0.1)
        print("7. Display Total Time")

        time.sleep(0.1)
        print("8. Exit")
        print()
        time.sleep(0.5)
        choice = input("Select an option: ")

        if choice == "1":
            user_id = input("Enter user ID (4 numbers): ")
            time.sleep(1)
            print()
            user_name = input("Enter user name: ")
            punch_system.add_user(user_id, user_name)
            time.sleep(1)
            print()
            print("User Successfully added.")

        elif choice == "2":

            user_id = input("Enter user ID: ")
            print()
            time.sleep(1)
            punch_system.clock_in(user_id)
            print()
        elif choice == "3":
            user_id = input("Enter user ID: ")
            print()
            session_duration = punch_system.clock_out(user_id)
            time.sleep(1)
            if session_duration:
                print()  # Add an empty line for separation
        elif choice == "4":
            time.sleep(1)
            print()
            punch_system.print_current_users()
            print()
            user_id = input("Enter user ID to remove: ")
            punch_system.remove_user(user_id)
            print()
            print("User removed successfully")
            time.sleep(1)
            print()
        elif choice == "5":
            time.sleep(1)
            punch_system.print_current_users()
            print()
        elif choice == "6":
            time.sleep(1)
            print()
            punch_system.display_logs()
            print()
        elif choice == "7":
            time.sleep(1)
            print()
            total_time = punch_system.get_total_time()
            print(f"Total time accumulated: {total_time} hours")
            time.sleep(1)
            print()
        elif choice == "8":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()