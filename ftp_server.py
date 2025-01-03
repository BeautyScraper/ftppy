
from main import connect_ftp_server
from scan_network import scan_ftp_servers

def return_connected_server():
    # FTP server details
    ftp_port = 2121           # Default FTP port is 21
    ftp_host = scan_ftp_servers(ftp_port)  # Replace with your FTP server's IP or hostname
    ftp_user = 'android'   # Replace with your FTP server username
    ftp_pass = 'android'   # Replace with your FTP server password
    ftp = connect_ftp_server(ftp_host, ftp_port, ftp_user, ftp_pass)
    return ftp