import os
from pydub import AudioSegment

def convert_wma_to_mp3(wma_dir, mp3_dir):
    if not os.path.isdir(wma_dir):
        raise ValueError(f"The directory {wma_dir} does not exist.")
    if not os.path.isdir(mp3_dir):
        raise ValueError(f"The directory {mp3_dir} does not exist.")
    wma_file_count = 0
    for root, dirs, files in os.walk(wma_dir):
        for file in files:
            if not file.endswith('.wma'):
                continue
            wma_file_count += 1
            wma_filepath = os.path.join(root, file)
            mp3_dirpath = os.path.join(root.replace(wma_dir, mp3_dir))
            if not os.path.exists(mp3_dirpath):
                os.makedirs(mp3_dirpath)
            mp3_filepath = os.path.join(mp3_dirpath, file.replace('.wma', '.mp3'))    
            try:
                audio = AudioSegment.from_file(wma_filepath)
                audio.export(mp3_filepath, format="mp3")
                print(f"Successfully converted '{os.path.basename(wma_filepath)}' to '{os.path.basename(mp3_filepath)}'")
            except Exception as e:
                print(f"Error converting '{os.path.basename(wma_filepath)}': {e}")
    return wma_file_count
    
if __name__ == "__main__":
    wma_dir = "./music-oldcollection"
    mp3_dir = "./music-newcollection"
    wma_file_count = convert_wma_to_mp3(wma_dir, mp3_dir)
    print(f"Number of .wma files counted: {wma_file_count}")