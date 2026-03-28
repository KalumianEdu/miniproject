import hashlib

def generate_hash(file_path): 

    try:
        with open(file_path, "rb") as f:
            data = f.read()
        sha256 = hashlib.sha256(data)
        return sha256.hexdigest()
    except Exception as e:
        print(f"Error generating hash for {file_path}: {e}")
        return None
