from ftp_server import return_connected_server
from main import *

if __name__=='__main__':
    ftp = return_connected_server()
    local_folder = r'c:\Personal\Audiobook\toMobile'
    remote_folder = 'Paradise/Audiobook'  # Replace with the remote folder path where files should be uploaded)
    # mkdir(ftp,remote_folder)
    upload_folder(ftp, local_folder, remote_folder)

    # download_folder(ftp,'/storage/emulated/0/DCIM/Camera/', r'C:\Personal\stuff\Essence\FS\SachMe')