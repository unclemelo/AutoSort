import os
import shutil
import time
import platform

# Detect operating system
OS_TYPE = platform.system()
if OS_TYPE == "Windows":
    DOWNLOADS_FOLDER = os.path.expanduser("~\\Downloads")
    SORT_DESTINATIONS = {
        "invoice": "~\\Documents\\Invoices",
        "report": "~\\Documents\\Reports",
        "image": "~\\Pictures\\Downloaded",
        "video": "~\\Videos\\Downloaded",
        "pdf": "~\\Documents\\PDFs",
        "audio": "~\\Music\\Downloaded",
        "archive": "~\\Documents\\Archives",
        "code": "~\\Documents\\Code_Files"
    }
elif OS_TYPE in ["Linux", "Darwin"]:  # Darwin is macOS
    DOWNLOADS_FOLDER = os.path.expanduser("~/Downloads")
    SORT_DESTINATIONS = {
        "invoice": "~/Documents/Invoices",
        "report": "~/Documents/Reports",
        "image": "~/Pictures/Downloaded",
        "video": "~/Videos/Downloaded",
        "pdf": "~/Documents/PDFs",
        "audio": "~/Music/Downloaded",
        "archive": "~/Documents/Archives",
        "code": "~/Documents/Code_Files"
    }
else:
    print(f"Unsupported OS: {OS_TYPE}")
    exit(1)

# Ensure all destination directories exist
for path in SORT_DESTINATIONS.values():
    os.makedirs(os.path.expanduser(path), exist_ok=True)

# Define file extensions mapping
FILE_TYPES = {
    "image": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "video": [".mp4", ".mkv", ".avi", ".mov"],
    "pdf": [".pdf"],
    "audio": [".mp3", ".wav", ".flac"],
    "archive": [".zip", ".rar", ".tar", ".gz", ".deb", ".7zip", ".NanaZip"],
    "code": [".py", ".js", ".html", ".css", ".java", ".cpp", ".json", ".cs", ".cpp", ".c", ".z"]
}

def sort_files():
    print("Scanning for files...")
    try:
        for filename in os.listdir(DOWNLOADS_FOLDER):
            file_path = os.path.join(DOWNLOADS_FOLDER, filename)
            
            if os.path.isfile(file_path):
                for category, extensions in FILE_TYPES.items():
                    if any(filename.lower().endswith(ext) for ext in extensions):
                        dest_path = os.path.expanduser(SORT_DESTINATIONS.get(category, DOWNLOADS_FOLDER))
                        try:
                            shutil.move(file_path, os.path.join(dest_path, filename))
                            print(f"Moved {filename} to {dest_path}")
                        except Exception as e:
                            print(f"Error moving {filename}: {e}")
                        break
    except Exception as e:
        print(f"Error scanning directory: {e}")
    print("Scan complete.")

if __name__ == "__main__":
    while True:
        try:
            sort_files()
        except Exception as e:
            print(f"Unexpected error: {e}")
        time.sleep(10)  # Check for new files every 10 seconds
