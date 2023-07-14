from ftp_server import return_connected_server
from main import *

if __name__=='__main__':
    ftp = return_connected_server()
    download_folder(ftp,'Pictures/0Sachme', r'C:\Personal\stuff\Essence\FS\SachMe', True)
    # download_folder(ftp,'/storage/emulated/0/DCIM/Camera/', r'C:\Personal\stuff\Essence\FS\SachMe')