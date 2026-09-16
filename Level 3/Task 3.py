import os
import shutil

# Folder to organize
folder = input("Enter the folder path: ")

# File categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Media": [".mp3", ".mp4", ".avi", ".mkv"],
    "Code": [".py", ".java", ".html", ".css", ".js"]
}

# Check whether the folder exists
if not os.path.exists(folder):
    print("Folder does not exist.")
else:

    # Read all files in the folder
    for file in os.listdir(folder):

        file_path = os.path.join(folder, file)

        # Process files only
        if os.path.isfile(file_path):

            # Get the file extension
            extension = os.path.splitext(file)[1].lower()

            moved = False

            # Find the correct category
            for category, extensions in file_types.items():

                if extension in extensions:

                    # Create category folder if it does not exist
                    category_folder = os.path.join(folder, category)
                    os.makedirs(category_folder, exist_ok=True)

                    # Move the file
                    shutil.move(
                        file_path,
                        os.path.join(category_folder, file)
                    )

                    print(f"Moved {file} -> {category}")
                    moved = True
                    break

            # Files that don't match any category
            if not moved:
                print(f"Skipped: {file}")

    print("\nFile organization completed!")