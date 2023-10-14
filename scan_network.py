import socket
import netifaces

def get_subnet_address():
    interfaces = netifaces.interfaces()
    addresses_l = [netifaces.ifaddresses(x) for x in interfaces if netifaces.AF_INET in netifaces.ifaddresses(x) ]
    for addresses in addresses_l:
        if netifaces.AF_INET in addresses:
            for link in addresses[netifaces.AF_INET]:
                # print(addresses)
                if 'addr' in link:
                    ip_address = link['addr']
                    if not '192' in ip_address:
                        continue
                    # breakpoint()
                    subnet_address = ip_address.rsplit('.', 1)[0] + '.'
                    sfh = int(ip_address.split('.')[-1])
                    return subnet_address, sfh #start_from_here

def scan_ftp_servers():
    subnet_address, sfh = get_subnet_address()
    for i in range(sfh - 5, 256):  # Scan all possible IP addresses in the subnet
        ip_address = subnet_address + str(i)
        ftp_port = 2121  # Default FTP port is 21
        print(f'testing {ip_address}:{str(ftp_port)} ')
        # Create a socket and set a timeout
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Timeout of 1 second

        try:
            # Attempt to connect to the FTP server
            result = sock.connect_ex((ip_address, ftp_port))
            # result = sock.connect((ip_address, ftp_port))
            if result == 0:
                print(f"FTP server found at {ip_address}")
                return str(ip_address)
        except socket.error:
            pass

        sock.close()
    return None

# Get the subnet address automatically


