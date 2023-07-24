from ftplib import FTP
from pathlib import Path, PurePosixPath
from scan_network import scan_ftp_servers
from random import randint
from tqdm import tqdm
from ftplib import error_perm

def mkdir(ftp, rpath):
    ftp.cwd('/')
    try:
        mkdir_helper(ftp, rpath)
    except Exception as e:
        if '550' in str(e):
            print('folder already exist')
    ftp.cwd('/')
        # print(e)``
        # breakpoint()


def ccwd(rpath):
    if not '/' in rpath:
        ftp.cwd(rpath)
    else:
        current_dir = rpath.split('/')[0]
    
    temp_rpath = '/'.join(rpath.split('/')[1:])
    # breakpoint()
    if not current_dir.lower() in map(str.lower,ftp.nlst()):
        print(f'folder {current_dir} does not exist')
        return False
    ftp.cwd(current_dir)
    ccwd(temp_rpath)
    # mkdir(ftp,temp_rpath)
    

def mkdir_helper(ftp,rpath):
    print(rpath)
    if not '/' in rpath:
        ftp.mkd(rpath)
    else:
        current_dir = rpath.split('/')[0]
        temp_rpath = '/'.join(rpath.split('/')[1:])
        # breakpoint()
        if not current_dir.lower() in map(str.lower,ftp.nlst()):
            # ftp.mkd('"%s"' % current_dir)
            ftp.mkd(current_dir)
        ftp.cwd(current_dir)
        mkdir_helper(ftp,temp_rpath)



def download_folder(ftp, remote_folder, local_folder, dad=False):
    ftp.cwd(remote_folder)

    # Create the local folder if it doesn't exist
    Path(local_folder).mkdir(parents=True, exist_ok=True)

    # List files and directories in the remote folder
    file_list = ftp.nlst()

    for item in file_list:
        item_path = Path(remote_folder) / item
        local_item_path = Path(local_folder) / item
        try:
            ftp.cwd(str(item_path))
        except error_perm:
            # If item is a file, download it
            with open(str(local_item_path), 'wb') as file:
                ftp.retrbinary('RETR ' + str(item), file.write)
                print(f"File '{item}' downloaded and saved to '{local_item_path}'")
                if dad:
                    ftp.delete(str(item))
                    print(f"File '{item}' deleted from the FTP server")
        else:
            # If item is a directory, create the corresponding local directory and recursively download its contents
            local_item_path.mkdir(parents=True, exist_ok=True)
            download_folder(ftp, str(item_path), str(local_item_path))


def connect_ftp_server(host, port, username, password):
    ftp = FTP()
    ftp.connect(host, port)
    ftp.login(username, password)
    print('Connected Ftp')
    return ftp

def list_files(ftp):
    file_list = ftp.nlst()
    print("Files in the current directory:")
    for file_name in file_list:
        print(file_name)

def download_file(ftp, file_to_download, local_file_path):
    with open(local_file_path, 'wb') as file:
        ftp.retrbinary('RETR ' + file_to_download, file.write)
        print(f"File '{file_to_download}' downloaded and saved to '{local_file_path}'")

def upload_file(ftp, file_to_upload, remote_file_path):
    with open(file_to_upload, 'rb') as file:
        resp = ftp.storbinary('STOR ' + Path(file_to_upload).name, file)
        if not '226' in resp:
            breakpoint()
            
        # print(f"File '{file_to_upload}' uploaded to '{remote_file_path}'")

def upload_folder(ftp, local_folder, remote_folder):
    # remote_folder = remote_folder.replace(' ','_') 
    mkdir(ftp,remote_folder)
    local_folder_path = Path(local_folder)
    breakpoint()
    ftp.cwd(remote_folder)
    file_list = [x for x in local_folder_path.glob('**/*')]
    for file_path in tqdm(file_list):
        # breakpoint()
        if file_path.is_file():
            relative_path = file_path.relative_to(local_folder_path)
            remote_file_path = Path(remote_folder) / relative_path
            upload_file(ftp, str(file_path), remote_folder)
            file_path.unlink()
        if file_path.is_dir():
            remote_folder_temp = remote_folder+'/'+file_path.name
            upload_folder(ftp, str(file_path), remote_folder_temp)

def disconnect_ftp_server(ftp):
    ftp.quit()

if __name__=='__main__':
    # FTP server details
    ftp_host = scan_ftp_servers()  # Replace with your FTP server's IP or hostname
    ftp_port = 2121           # Default FTP port is 21
    ftp_user = 'username'   # Replace with your FTP server username
    ftp_pass = 'password'   # Replace with your FTP server password
    ftp = connect_ftp_server(ftp_host, ftp_port, ftp_user, ftp_pass)
    local_folder = r'C:\Personal\Games\Sacred2'  # Replace with the local folder path containing files to upload
    remote_folder = 'Paradise/stuff/folder'+str(randint(1,100000))  # Replace with the remote folder path where files should be uploaded)
    upload_folder(ftp, local_folder, remote_folder)

    # Close the FTP connection
    disconnect_ftp_server(ftp)
