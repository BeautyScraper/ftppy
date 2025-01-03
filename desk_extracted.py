from ftp_server import return_connected_server
from main import *
from pathlib import Path
import random
import shutil

def move_random_files(input_dir, output_dir, number_of_files_to_move):
    # Convert input_dir and output_dir to Path objects
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    
    # Ensure the input directory exists
    if not input_path.is_dir():
        raise ValueError("The input directory does not exist.")
    
    # Create the output directory if it doesn't exist
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Get a list of all files in the input directory
    all_files = [file for file in input_path.iterdir() if file.is_file()]
    
    # Check if the number of files to move is more than the available files
    if number_of_files_to_move > len(all_files):
        raise ValueError("The number of files to move exceeds the number of available files.")
    
    # Randomly select the specified number of files
    files_to_move = random.sample(all_files, number_of_files_to_move)
    
    # Move each selected file to the output directory
    for file in files_to_move:
        shutil.move(str(file), output_path / file.name)
    
    print(f"{len(files_to_move)} file(s) moved to {output_path}.")

# Example usage
# move_random_files('path/to/input_dir', 'path/to/output_dir', 5)

if __name__=='__main__':
    ftp = return_connected_server()
    move_random_files(r'D:\paradise\stuff\new\pvd2\extractedVideo2', r'D:\paradise\stuff\new\temp_tobecopied_into_mobile', 20)
    move_random_files(r'D:\paradise\stuff\new\clips', r'D:\paradise\stuff\new\temp_tobecopied_into_mobile', 20)
    local_folder = r'D:\paradise\stuff\new\temp_tobecopied_into_mobile'
    remote_folder = 'Paradise/stuff'  # Replace with the remote folder path where files should be uploaded)
    # mkdir(ftp,remote_folder)
    upload_folder(ftp, local_folder, remote_folder)

    # download_folder(ftp,'/storage/emulated/0/DCIM/Camera/', r'C:\Personal\stuff\Essence\FS\SachMe')