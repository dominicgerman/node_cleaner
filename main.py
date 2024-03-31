import sys, os
from utils import delete_node_modules

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Requires exactly two (2) args: python PROGRAM_PATH WORKSPACE_DIRECTORY")
        for arg in sys.argv:
            print(arg)
        sys.exit(1)

    workspace_directory = sys.argv[1]

    if not os.path.isdir(workspace_directory):
        print("Error: Workspace directory does not exist.")
        sys.exit(1)

    delete_node_modules(workspace_directory)
