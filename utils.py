import os
import shutil
import datetime

threshold_date = datetime.datetime.now() - datetime.timedelta(days=30)

def is_recently_updated(directory):
    directory_modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(directory))
    if directory_modified_time >= threshold_date:
        return True
    return False

def delete_node_modules(base_directory):
    for root, dirs, files in os.walk(base_directory):
        if 'node_modules' in dirs:
            node_modules_path = os.path.join(root, 'node_modules')
            if not is_recently_updated(node_modules_path):
                shutil.rmtree(node_modules_path)
                print(f"Deleted node_modules directory in {root}")

