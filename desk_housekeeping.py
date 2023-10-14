from ftp_server import return_connected_server
from main import *

if __name__=='__main__':
    ftp = return_connected_server()
    download_folder(ftp,'MIUI/sound_recorder/call_rec', r'D:\mobile\call_records', True)
    download_folder(ftp,'DCIM/Camera', r'D:\mobile\Cam_video', True, ['.mp4'])
    download_folder(ftp,'Pictures/0Sachme', r'D:\paradise\stuff\essence\FS\sachme', True, ['.mp4','.jpg','.jpeg', '.png'])
    download_folder(ftp,'Pictures/Personal', r'D:\mobile\personal_pics', True, ['.mp4','.jpg','.jpeg', '.png'])
    download_folder(ftp,'Pictures/Fs Source Personal', r'D:\paradise\stuff\simswappg\srcs\Fs_source', True, ['.mp4','.jpg','.jpeg', '.png'])
    download_folder(ftp,'WhatsApp/Media/WhatsApp Video', r'D:\mobile\whatsapp_video', True, ['.mp4'])
    # download_folder(ftp,'WhatsApp/Media/WhatsApp Audio', r'D:\mobile\whatsapp_audio', True)
    # download_folder(ftp,'/storage/emulated/0/DCIM/Camera/', r'C:\Personal\stuff\Essence\FS\SachMe')