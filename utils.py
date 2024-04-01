import os
import shutil
import datetime

threshold_date = datetime.datetime.now() - datetime.timedelta(days=30)

def delete_node_modules(base_directory):
    for root, dirs, files in os.walk(base_directory):
        if 'node_modules' in dirs:
            node_modules_path = os.path.join(root, 'node_modules')
            parent_dir = os.path.dirname(node_modules_path)
            if not has_recently_updated_files(parent_dir):
                shutil.rmtree(node_modules_path)
                print(f"Deleted node_modules directory in {root}")
            dirs.clear()

def has_recently_updated_files(directory):
    for root, dirs, files in os.walk(directory):
        if 'node_modules' in dirs:
            dirs.remove('node_modules')
        for file in files:
            file_path = os.path.join(root, file)
            file_modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
            if file_modified_time >= threshold_date:
                return True
    return False
