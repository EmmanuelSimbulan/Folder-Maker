import os

def create_folders(base_path):
    try:
        # Create 12 folders
        for i in range(1, 13):                          #How many iterartions you want to do
            folder_name = f'folder_name{i}'             #Name of the folder
            folder_path = os.path.join(base_path, folder_name)
            os.makedirs(folder_path)
            print(f"Folder '{folder_name}' created at {folder_path}")
    except OSError as e:
        print(f"Error: {e}")

# Specify the file path where you want to create the folders
file_path = 'folder path'  # Replace this with your desired directory path

create_folders(file_path)
