import os
import shutil
import sys

def organize_jpg_files(source_dir, dest_dir):
    """
    Scans source_dir for all .jpg and .jpeg files and moves them to dest_dir.
    
    Parameters:
        source_dir (str): Path to the folder containing unorganized files.
        dest_dir (str): Path to the destination folder where .jpg files will be stored.
    """
    # Verify source directory exists
    if not os.path.exists(source_dir):
        print(f"Error: Source directory '{source_dir}' does not exist.")
        return

    # Create destination directory if it doesn't exist
    os.makedirs(dest_dir, exist_ok=True)
    
    moved_count = 0
    skipped_count = 0

    # List all items in the source directory
    for filename in os.listdir(source_dir):
        # Case-insensitive check for .jpg and .jpeg extensions
        if filename.lower().endswith(('.jpg', '.jpeg')):
            src_path = os.path.join(source_dir, filename)
            
            # Skip if it's a sub-directory with a .jpg name
            if os.path.isfile(src_path):
                dest_path = os.path.join(dest_dir, filename)
                
                # Handle filename collisions in destination folder
                if os.path.exists(dest_path):
                    base, ext = os.path.splitext(filename)
                    counter = 1
                    while os.path.exists(dest_path):
                        dest_path = os.path.join(dest_dir, f"{base}_{counter}{ext}")
                        counter += 1
                
                shutil.move(src_path, dest_path)
                print(f"[MOVED] {filename} -> {dest_path}")
                moved_count += 1
            else:
                skipped_count += 1

    print("\n--- Summary ---")
    print(f"Total .jpg/.jpeg files moved: {moved_count}")
    if skipped_count > 0:
        print(f"Skipped directories: {skipped_count}")

if __name__ == "__main__":
    # Default directories for quick execution/testing
    src = sys.argv[1] if len(sys.argv) > 1 else "./source_folder"
    dst = sys.argv[2] if len(sys.argv) > 2 else "./jpg_folder"
    
    print(f"Starting organization from '{src}' to '{dst}'...\n")
    organize_jpg_files(src, dst)
