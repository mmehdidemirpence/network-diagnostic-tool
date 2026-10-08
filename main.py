from machine_info import get_machine_info
from echo_test import echo_test_menu
from sntp_sync import get_sntp_time
from chat_app import chat_menu
from socket_settings import test_socket_settings

def display_menu():
    print("=" * 48)
    print("  CEN437 - NETWORK DIAGNOSTIC & TOOL PACKAGE ")
    print("=" * 48)
    print("1. Machine Information")
    print("2. Echo Test")
    print("3. SNTP Time Synchronization")
    print("4. Simple Chat Module")
    print("5. Socket Settings & Error Management")
    print("6. Exit")
    print("=" * 48)

def main():
    while True:
        display_menu()
        choice = input("Select an option (1-6): ").strip()
        
        if choice == '1':
            get_machine_info()
        elif choice == '2':
            echo_test_menu()
        elif choice == '3':
            get_sntp_time()
        elif choice == '4':
            chat_menu()
        elif choice == '5':
            test_socket_settings()
        elif choice == '6':
            print("[+] Exiting program. Goodbye!")
            break
        else:
            print("[-] Invalid selection! Please enter a number between 1 and 6.\n")

if __name__ == "__main__":
    main()