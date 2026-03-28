from hash import generate_hash
import os
import json

def create_manifest(directory):
    manifest = {}

    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)

        if os.path.isfile(path):
            manifest[filename] = generate_hash(path)

    with open("metadata.json", "w") as f:
        json.dump(manifest, f, indent=4)
        

def check_integrity(directory):
    with open("metadata.json", "r") as f:
        old_manifest = json.load(f)

    for filename, old_hash in old_manifest.items():
        path = os.path.join(directory, filename)

        if not os.path.exists(path):
            print(f"{filename} is missing!")
            continue

        new_hash = generate_hash(path)

        if new_hash != old_hash:
            print(f"{filename} has been modified!")
        else:
            print(f"{filename} is OK")