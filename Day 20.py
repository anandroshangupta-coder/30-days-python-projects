# ==========================================
# Day 20 - Bulk File Renamer
# 30 Days Python GitHub Project Challenge
# ==========================================

import os

print("======================================")
print("          BULK FILE RENAMER")
print("======================================")

# Get folder path
folder_path = input("\nEnter folder path: ").strip()

# Check folder
if not os.path.exists(folder_path):
    print("❌ Folder does not exist.")
    exit()

if not os.path.isdir(folder_path):
    print("❌ The given path is not a folder.")
    exit()


# Get new file name
new_name = input("Enter new file name: ").strip()

if new_name == "":
    print("❌ File name cannot be empty.")
    exit()


# Get files
files = []

for file_name in os.listdir(folder_path):

    file_path = os.path.join(folder_path, file_name)

    # Only files, not folders
    if os.path.isfile(file_path):
        files.append(file_name)


# Sort files
files.sort()

if not files:
    print("\n❌ No files found in this folder.")
    exit()


print("\n======================================")
print("         RENAMING FILES")
print("======================================")


renamed_count = 0

# Rename files
for number, old_name in enumerate(files, start=1):

    old_path = os.path.join(folder_path, old_name)

    # Get extension
    extension = os.path.splitext(old_name)[1]

    # Create new name
    new_file_name = f"{new_name}_{number}{extension}"

    new_path = os.path.join(
        folder_path,
        new_file_name
    )

    # Avoid overwriting
    if os.path.exists(new_path):
        print(f"⚠️ Skipped: {old_name}")
        continue

    # Rename file
    os.rename(old_path, new_path)

    print(f"✅ {old_name} → {new_file_name}")

    renamed_count += 1


# Final result
print("\n======================================")
print("        RENAMING COMPLETED")
print("======================================")
print(f"Files found   : {len(files)}")
print(f"Files renamed : {renamed_count}")
print("======================================")