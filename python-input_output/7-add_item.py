#!/usr/bin/python3
if __name__ == "__main__":
    import os
    import sys
    save = __import__("5-save_to_json_file").save_to_json_file
    load = __import__("6-load_from_json_file").load_from_json_file

    filename = "add_item.json"

    if os.path.exists(filename):
        item = load(filename)
    else:
        item = []

    item.append(sys.argv[1:])

    save(item, filename)
