import sys
from hash import generate_hash
from local_integrity import create_manifest, check_integrity
from sign import generate_keys, sign_manifest, verify_signature


# First, Before Running the Code, Make sure to run the sign.py file to sign the file using the Private Key of the Sender
# Then tell the user to enter the name of the file to be sent,

def main():
    command = sys.argv[1]

    if command == "generate_keys":
        generate_keys()

    elif command == "manifest":
        directory = sys.argv[2]
        create_manifest(directory)

    elif command == "check":
        directory = sys.argv[2]
        check_integrity(directory)
    elif command == "sign":
        sign_manifest()
    elif command == "verify":
        verify_signature()

    else:
        print("Unknown command")

if __name__ == "__main__":
    main()
