# ==========================================
# Day 19 - File Organizer
# 30 Days Python GitHub Project Challenge
# ==========================================

import os
import shutil


print("======================================")
print("           FILE ORGANIZER")
print("======================================")


# Folder to organize
folder_path = input("\nEnter folder path: ").strip()


# Check if folder exists
if not os.path.exists(folder_path):
    print("\n❌ Folder does not exist.")
    exit()

if not os.path.isdir(folder_path):
    print("\n❌ The given path is not a folder.")
    exit()


# File categories
file_categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".ppt", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Python": [".py"],
    "CSV": [".csv"],
}


# Find category
def get_category(extension):

    for category, extensions in file_categories.items():

        if extension.lower() in extensions:
            return category

    return "Others"


# Organize files
files_moved = 0

for file_name in os.listdir(folder_path):

    file_path = os.path.join(folder_path, file_name)

    # Skip folders
    if os.path.isdir(file_path):
        continue

    # Get file extension
    extension = os.path.splitext(file_name)[1]

    # Skip files without extension
    if extension == "":
        continue

    # Get category
    category = get_category(extension)

    # Create category folder
    category_folder = os.path.join(folder_path, category)

    if not os.path.exists(category_folder):
        os.makedirs(category_folder)

    # Destination path
    destination = os.path.join(category_folder, file_name)

    # Avoid overwriting files
    if os.path.exists(destination):

        base_name, file_extension = os.path.splitext(file_name)

        counter = 1

        while os.path.exists(destination):

            new_name = f"{base_name}_{counter}{file_extension}"
            destination = os.path.join(
                category_folder,
                new_name
            )

            counter += 1

    # Move file
    shutil.move(file_path, destination)

    print(f"✅ Moved: {file_name} → {category}/")

    files_moved += 1


# Final result
print("\n======================================")
print("         ORGANIZATION COMPLETE")
print("======================================")
print(f"Files organized : {files_moved}")
print(f"Folder          : {folder_path}")
print("======================================")