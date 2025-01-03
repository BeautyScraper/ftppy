from ftp_server import return_connected_server
from main import *

if __name__=='__main__':
    ftp = return_connected_server()
    # download_folder(ftp,'Pictures/0goodone', r'C:\Heaven\Haven\brothel\goodone', True, ['.mp4','.jpg','.jpeg', '.png'])
    # download_folder(ftp,'MIUI/sound_recorder/call_rec', r'D:\mobile\call_records', True)

    download_folder(ftp,'DCIM/Camera', r'D:\mobile\Cam_video', True, ['.mp4'])
    download_folder(ftp,'DCIM/Snapchat', r'D:\mobile\Cam_video', True, ['.mp4','.jpg','.jpeg', '.png'])
    download_folder(ftp,'Pictures/0P', r'D:\mobile\Cam_video', True, ['.mp4','.jpg','.jpeg', '.png'])

    # download_folder(ftp,'Pictures/0Sachme', r'D:\paradise\stuff\essence\FS\sachme', True, ['.mp4','.jpg','.jpeg', '.png'])
    # download_folder(ftp,'Pictures/5PersonalPic', r'D:\mobile\personal_pics', True, ['.mp4','.jpg','.jpeg', '.png'])
    # download_folder(ftp,'Pictures/0personal', r'D:\mobile\personal_pics', True, ['.mp4','.jpg','.jpeg', '.png'])
    download_folder(ftp,'Pictures/BestFap', r'C:\Heaven\Haven\brothel\BestFromMobile', True, ['.jpg','.jpeg', '.png'])
    download_folder(ftp,'Pictures/0f', r'C:\Heaven\Haven\brothel\BestFromMobile', True, ['.jpg','.jpeg', '.png'])
    download_folder(ftp,'Download/Meet', r'D:\mobile\Cam_video', True, ['.jpg','.jpeg', '.png'])
    download_folder(ftp,'Download', r'C:\Heaven\Haven\brothel\BestFromMobile', True, ['.jpg','.jpeg', '.png'])
    download_folder(ftp,'Pictures/BestFap', r'D:\paradise\stuff\new\clips', True, ['.mp4'])
    download_folder(ftp,'Download', r"D:\paradise\stuff\new\to_be_clipped", True, ['.mp4'])
    # download_folder(ftp,'Pictures/Fs Source Personal', r'D:\paradise\stuff\simswappg\srcs\Fs_source', True, ['.mp4','.jpg','.jpeg', '.png'])
    # download_folder(ftp,'WhatsApp/Media/WhatsApp Video', r'D:\mobile\whatsapp_video', True, ['.mp4'])
    # download_folder(ftp,'WhatsApp/Media/WhatsApp Audio', r'D:\mobile\whatsapp_audio', True)
    # download_folder(ftp,'/storage/emulated/0/DCIM/Camera/', r'C:\Personal\stuff\Essence\FS\SachMe')