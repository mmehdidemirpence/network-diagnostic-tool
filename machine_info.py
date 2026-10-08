import socket

def get_machine_info():
    """Retrieves and displays the local machine hostname and IP address."""
    try:
        host_name = socket.gethostname()
        ip_address = socket.gethostbyname(host_name)
        
        print("\n--- MACHINE INFORMATION ---")
        print(f"Hostname   : {host_name}")
        print(f"IP Address : {ip_address}")
        print("---------------------------\n")
    except socket.error as err:
        print(f"[-] Failed to retrieve machine info: {err}")

if __name__ == "__main__":
    get_machine_info()