import os
import glob

def cleanup_wma_files(directory):
    wma_files = glob.glob(os.path.join(directory, '**', '*.wma'), recursive=True)
    wma_file_count = 0
    for file in wma_files:
        try:
            os.remove(file)
            print(f"Deleted: {file}")
            wma_file_count += 1
        except Exception as e:
            print(f"Error deleting {file}: {e}")
    print(f"Number of .wma files deleted: {wma_file_count}")

if __name__ == "__main__":
    cleanup_wma_files('./music-oldcollection')