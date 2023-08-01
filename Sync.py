import os
import shutil

def sync_to_hard_drive_if_missing(local_path, hard_drive_path, file_extensions=[".jpg", ".png", ".mp4"]):
    # Check if the local path exists
    if not os.path.exists(local_path):
        print("Local path not found!")
        return

    # Check if the hard drive path exists
    if not os.path.exists(hard_drive_path):
        print("Hard drive path not found!")
        return

    # Retrieve the list of files in the local path
    local_files = os.listdir(local_path)

    # Sync the files from local machine to hard drive if missing in hard drive
    for file in local_files:
        if os.path.splitext(file)[1].lower() in file_extensions:
            local_file_path = os.path.join(local_path, file)
            hard_drive_file_path = os.path.join(hard_drive_path, file)

            if os.path.isfile(local_file_path) and not os.path.exists(hard_drive_file_path):
                print(f"Syncing file '{file}' to hard drive...")
                shutil.copy2(local_file_path, hard_drive_path)

    print("Syncing complete.")

# Specify the path of your local machine where the images or videos are stored
local_path = "C:/Users/MadhavaRaj/Desktop/data/images/checking"

# Specify the path of your hard drive
hard_drive_path = "E:/"

# Call the function to sync missing files to the hard drive
sync_to_hard_drive_if_missing(local_path, hard_drive_path)
