import socket
from datetime import datetime

LOG_FILE = "chat_logs.txt"

def log_message(sender, message):
    """Logs chat messages with a timestamp to a text file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {sender}: {message}\n"
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(entry)
    except Exception as e:
        print(f"[-] Log Error: {e}")

def run_chat_server(port=5001):
    """Runs the chat module in Server Mode."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Portun hemen serbest kalmasını sağlar
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        server.bind(('0.0.0.0', port))
        server.listen(1)
        print(f"\n[+] Chat Server listening on port {port}...")
        print("[!] Waiting for a client to connect... (Press Ctrl+C to cancel)")
        
        conn, addr = server.accept()
        print(f"[+] Connected by {addr}. Chat started!")
        print("[!] Type 'exit' to end the conversation.\n")
        
        while True:
            data = conn.recv(1024).decode('utf-8')
            if not data or data.lower() == 'exit':
                print("\n[-] Client has disconnected or ended the chat.")
                break
            print(f"Client: {data}")
            log_message("Client", data)
            
            reply = input("You: ")
            conn.sendall(reply.encode('utf-8'))
            log_message("Server", reply)
            if reply.lower() == 'exit':
                print("\n[+] You ended the chat.")
                break
        conn.close()

    except KeyboardInterrupt:
        print("\n[-] Chat Server cancelled by user (Ctrl+C). Returning to menu.")
    except Exception as e:
        print(f"\n[-] Server Error: {e}")
    finally:
        server.close()

def run_chat_client(host='127.0.0.1', port=5001):
    """Runs the chat module in Client Mode."""
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((host, port))
        print(f"\n[+] Connected to Chat Server at {host}:{port}. Chat started!")
        print("[!] Type 'exit' to end the conversation.\n")
        
        while True:
            msg = input("You: ")
            client.sendall(msg.encode('utf-8'))
            log_message("Client", msg)
            if msg.lower() == 'exit':
                print("\n[+] You ended the chat.")
                break
                
            reply = client.recv(1024).decode('utf-8')
            if not reply or reply.lower() == 'exit':
                print("\n[-] Server has disconnected or ended the chat.")
                break
            print(f"Server: {reply}")
            log_message("Server", reply)

    except KeyboardInterrupt:
        print("\n[-] Chat Client exited by user (Ctrl+C). Returning to menu.")
    except Exception as e:
        print(f"\n[-] Connection Error: {e}")
    finally:
        client.close()

def chat_menu():
    """Sub-menu for Chat module."""
    print("\n--- CHAT MODULE ---")
    print("1. Server Mode (Listen)")
    print("2. Client Mode (Connect)")
    choice = input("Enter your choice (1/2): ").strip()
    if choice == '1':
        run_chat_server()
    elif choice == '2':
        ip = input("Enter Target IP (default: 127.0.0.1): ").strip() or "127.0.0.1"
        run_chat_client(host=ip)
    else:
        print("[-] Invalid choice.")