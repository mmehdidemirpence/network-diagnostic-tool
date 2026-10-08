import socket
import threading
import time

def run_echo_server(host='127.0.0.1', port=65432):
    """Echo Server: Listens for incoming connections and echoes received data."""
    print(f"\n[+] Starting Echo Server on {host}:{port}...")
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server_socket.bind((host, port))
            server_socket.listen(1)
            print("[+] Waiting for connection...")
            conn, addr = server_socket.accept()
            with conn:
                print(f"[+] Connected by: {addr}")
                data = conn.recv(1024)
                if data:
                    conn.sendall(data)
                    print("[+] Data received and echoed back.")
    except Exception as e:
        print(f"[-] Server Error: {e}")

def run_echo_client(host='127.0.0.1', port=65432, message="Hello Network!"):
    """Echo Client: Sends data to the server and verifies the response."""
    print(f"\n[+] Connecting to Echo Server at {host}:{port}...")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        try:
            client_socket.connect((host, port))
            client_socket.sendall(message.encode('utf-8'))
            received_data = client_socket.recv(1024).decode('utf-8')
            
            print(f"Sent Data     : {message}")
            print(f"Received Data : {received_data}")
            
            if message == received_data:
                print("[✓] Result: Connection successful, data matches.")
            else:
                print("[X] Result: Data mismatch!")
        except socket.error as err:
            print(f"[-] Echo Test Connection Error: {err}")

def run_automated_test():
    """Runs server in a background thread and client in main thread for quick testing."""
    print("\n[+] Starting Automated Local Echo Test...")
    # Sunucuyu arka planda başlat (Thread)
    server_thread = threading.Thread(target=run_echo_server, daemon=True)
    server_thread.start()
    
    # Sunucunun dinlemeye geçmesi için kısa bir süre bekle
    time.sleep(0.5)
    
    # İstemciyi çalıştır
    run_echo_client(message="Automated Network Test Message")

def echo_test_menu():
    """Sub-menu for Echo Test module."""
    print("\n--- ECHO TEST MODULE ---")
    print("1. Start Echo Server (Requires separate terminal for Client)")
    print("2. Run Echo Client (Connects to an active Server)")
    print("3. Run Automated Self-Test (Server & Client in one go)")
    choice = input("Enter your choice (1/2/3): ").strip()
    if choice == '1':
        run_echo_server()
    elif choice == '2':
        msg = input("Enter message to send (default: Hello Network!): ").strip()
        run_echo_client(message=msg if msg else "Hello Network!")
    elif choice == '3':
        run_automated_test()
    else:
        print("[-] Invalid choice.")