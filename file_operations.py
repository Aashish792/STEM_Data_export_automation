import os
import shutil

def move_file(src_directory, dst_directory, pattern):
    for fname in os.listdir(src_directory):
        if fname.startswith(pattern):
            src_path = os.path.join(src_directory, fname)
            dst_path = os.path.join(dst_directory, fname)
            shutil.move(src_path, dst_path)
            print(f"File moved to {dst_path}")
            return dst_path
    return None
