import socket
import struct
import time

def get_sntp_time(host="pool.ntp.org"):
    """Fetches the current time from an SNTP server."""
    NTP_DELTA = 2208988800  # Seconds between 1900 and 1970
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.settimeout(5)
    
    # NTP Request Packet (48 bytes)
    data = b'\x1b' + 47 * b'\0'
    
    try:
        print(f"[+] Sending SNTP request to '{host}'...")
        client.sendto(data, (host, 123))
        data, _ = client.recvfrom(1024)
        
        if data:
            unpacked = struct.unpack("!12I", data)
            t = unpacked[10] - NTP_DELTA
            sntp_time_str = time.ctime(t)
            print("\n--- SNTP TIME SYNCHRONIZATION ---")
            print(f"NTP Server Time : {sntp_time_str}")
            print(f"Local System Time: {time.ctime()}")
            print("---------------------------------\n")
            return sntp_time_str
    except socket.timeout:
        print("[-] Error: SNTP request timed out.")
    except Exception as e:
        print(f"[-] SNTP Error: {e}")
    finally:
        client.close()