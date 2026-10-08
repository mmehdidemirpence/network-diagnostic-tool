import socket

def test_socket_settings():
    """Demonstrates socket buffer sizes, timeouts, and exception handling."""
    print("\n--- SOCKET SETTINGS & ERROR MANAGEMENT ---")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # 1. Modify Buffer Sizes
        s.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 4096)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 4096)
        rcvbuf = s.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
        sndbuf = s.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
        print(f"[+] Receive Buffer Size (SO_RCVBUF) : {rcvbuf}")
        print(f"[+] Send Buffer Size (SO_SNDBUF)    : {sndbuf}")
        
        # 2. Set Socket Timeout
        s.settimeout(2.0)
        print(f"[+] Socket Timeout set to           : {s.gettimeout()} seconds")
        
        # 3. Trigger & Catch Socket Timeout Error
        print("[+] Attempting connection to a closed port (127.0.0.1:9999)...")
        s.connect(('127.0.0.1', 9999))
        
    except socket.timeout:
        print("[!] CAUGHT EXCEPTION: Connection timed out (socket.timeout).")
    except socket.error as err:
        print(f"[!] CAUGHT EXCEPTION: Socket Error -> {err}")
    finally:
        s.close()
        print("[+] Socket connection closed.\n")