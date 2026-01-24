import os
import shutil


def create_folder(path: str, extension: str) -> str:
    """
    Create a folder named after a file extension inside the given path.

    If the folder does not already exist, it will be created.

    Args:
        path (str): Base directory (usually the current directory).
        extension (str): File extension (e.g. ".jpg", ".png").

    Returns:
        str: Full path to the created (or existing) folder.
    """
    folder_name: str = extension[1:]
    folder_path: str = os.path.join(path, folder_name)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    return folder_path


def sort_files(source_path: str):
    """
    Sort files in a directory tree into folders based on file extension.

    This function walks through the given source directory recursively.
    For each file found, it determines the file extension and moves the file
    into a corresponding folder (e.g. '.jpg' → 'jpg/') inside the source path.
    If the target folder does not exist, it will be created.

    Args:
        source_path (str): Path to the directory containing files to be sorted.
    """

    for root_dir, sub_dir, filenames in os.walk(source_path):
        for filename in filenames:
            file_path: str = os.path.join(root_dir, filename)
            extension: str = os.path.splitext(filename)[1]  # <-- split ext !!!

            if extension:
                target_folder: str = create_folder(source_path, extension)
                target_path: str = os.path.join(target_folder, filename)

                shutil.move(file_path, target_path)


def remove_empty_folders(source_path: str):
    """
    Remove all empty directories within a given directory tree.

    This function walks the directory tree bottom-up to ensure that
    subdirectories are processed before their parent directories.
    Any directory found to be empty is removed.

    Args:
        source_path (str): Path to the root directory to clean up.
    """

    for root_dir, sub_dir, filenames in os.walk(source_path, topdown=False):
        for current_dir in sub_dir:
            folder_path: str = os.path.join(root_dir, current_dir)
            if not os.listdir(folder_path):
                os.rmdir(folder_path)


def main():
    """
    Prompt the user for a directory path and sort files inside it.

    Keeps asking until the user provides a valid path. Once valid,
    sorts files by extension and removes empty folders.
    """
    user_input: str = input("Please provide a file path to sort: ")
    user_input = os.path.abspath(user_input)
    while not os.path.exists(user_input):
        print("Invalid path, please provide a valid file path.")
        user_input = input("Please provide a file path to sort: ")
        user_input = os.path.abspath(user_input)
    sort_files(user_input)
    remove_empty_folders(user_input)
    print("Files sorted successfully")


if __name__ == "__main__":
    main()
