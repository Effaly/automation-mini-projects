import os
import time
import shutil

def delete_old_files(folder_path, days=7):
    now = time.time()
    cutoff = now - (days * 86400)  # 86400 seconds in a day

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path) or os.path.islink(file_path):
            file_mtime = os.path.getmtime(file_path)
            if file_mtime < cutoff:
                os.remove(file_path)
                print(f"Deleted {file_path}")
        elif os.path.isdir(file_path):
            folder_mtime = os.path.getmtime(file_path)
            if folder_mtime < cutoff:
                shutil.rmtree(file_path)
                print(f"Deleted folder {file_path}")

if __name__ == "__main__":
    downloads_path = "C:\\Users\\USERNAME\\Downloads"  # Update this path
    delete_old_files(downloads_path, days=7)
