import os
import shutil


def organize_files(directory_path):
    file_extensions = {
        "Images":    [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
        "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv"],
        "Audio":     [".mp3", ".wav", ".aac", ".flac"],
        "Video":     [".mp4", ".mkv", ".mov", ".avi"],
        "Archives":  [".zip", ".rar", ".tar", ".gz", ".7z"],
        "Scripts":   [".py", ".js", ".html", ".css", ".cpp", ".java"]
    }

    if not os.path.exists(directory_path):
        print("Error: Directory '" + directory_path + "' not found.")
        return

    script_path = os.path.abspath(__file__)

    for filename in os.listdir(directory_path):
        filepath = os.path.abspath(os.path.join(directory_path, filename))

        if os.path.isdir(filepath):
            continue

        if filepath == script_path:
            continue

        file_ext = os.path.splitext(filename)[1].lower()
        moved = False

        for folder_name, extensions in file_extensions.items():
            if file_ext in extensions:
                target_folder = os.path.join(directory_path, folder_name)
                os.makedirs(target_folder, exist_ok=True)

                target_path = os.path.join(target_folder, filename)

                if os.path.exists(target_path):
                    base, ext = os.path.splitext(filename)
                    target_path = os.path.join(target_folder, base + "_copy" + ext)

                shutil.move(filepath, target_path)
                print("Moved: " + filename + " -> " + folder_name + "/")
                moved = True
                break

        if not moved:
            others_folder = os.path.join(directory_path, "Others")
            os.makedirs(others_folder, exist_ok=True)
            shutil.move(filepath, os.path.join(others_folder, filename))
            print("Moved: " + filename + " -> Others/")

    print("\nOrganization complete!")


if __name__ == "__main__":
    target_directory = input("Enter the full path of the directory to organize: ").strip()
    organize_files(target_directory)