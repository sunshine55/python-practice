import os

def count_wma_files(directory):
    if not os.path.isdir(directory):
        raise ValueError(f"The directory {directory} does not exist.")
    count = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.wma'):
                count += 1
    return count

if __name__ == "__main__":
    directory = "./music-oldcollection"
    wma_file_count = count_wma_files(directory)
    print(f"Number of .wma files: {wma_file_count}")