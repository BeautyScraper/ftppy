
from main import connect_ftp_server
from scan_network import scan_ftp_servers

def return_connected_server():
    # FTP server details
    ftp_port = 2121           # Default FTP port is 21
    # ftp_host = scan_ftp_servers(ftp_port)  # Replace with your FTP server's IP or hostname
    # ftp_host = '192.168.0.100'  # Replace with your FTP server's IP or hostname
    ftp_host = input("Do you want to enter the FTP host IP manually? (y/no): ").strip().lower()

    if ftp_host == 'y':
        last_used_ips = []
        try:
            with open('last_used_ips.txt', 'r') as file:
                last_used_ips = file.read().splitlines()
        except FileNotFoundError:
            pass
        if last_used_ips:
            print("Last used FTP hosts:")
            for i, ip in enumerate(last_used_ips):
                print(f"{i+1}. {ip}")
            print("Enter the number of the host to use it or enter a new one: ")
            choice = input("> ").strip()
            if choice.isdigit() and 0 < int(choice) <= len(last_used_ips):
                ftp_host = last_used_ips[int(choice)-1]
            else:
                ftp_host = input("Please enter the FTP host IP: ").strip()
                with open('last_used_ips.txt', 'a') as file:
                    file.write(f"{ftp_host}\n")
    else:
        ftp_host = scan_ftp_servers(ftp_port)

    ftp_user = 'android'   # Replace with your FTP server username
    ftp_pass = 'android'   # Replace with your FTP server password
    ftp = connect_ftp_server(ftp_host, ftp_port, ftp_user, ftp_pass)
    return ftp