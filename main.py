import hashlib
import os

def calculate_hash(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        while chunk := file.read(4096):
            sha256.update(chunk)

    return sha256.hexdigest()

def main():
    print("=" * 50)
    print("FILE INTEGRITY CHECKER")
    print("=" * 50)

    file_path = input("Enter file path: ")

    if not os.path.exists(file_path):
        print("File not found!")
        return

    current_hash = calculate_hash(file_path)

    print("\nSHA-256 Hash:")
    print(current_hash)

    choice = input("\nSave this hash for future verification? (y/n): ")

    if choice.lower() == "y":
        with open("stored_hash.txt", "w") as f:
            f.write(current_hash)
        print("Hash saved successfully!")

    verify = input("\nVerify file against stored hash? (y/n): ")

    if verify.lower() == "y":
        if not os.path.exists("stored_hash.txt"):
            print("No stored hash found!")
            return

        with open("stored_hash.txt", "r") as f:
            saved_hash = f.read().strip()

        if saved_hash == current_hash:
            print("\nFile Integrity Status: VERIFIED")
            print("No modifications detected.")
        else:
            print("\nFile Integrity Status: FAILED")
            print("File has been modified!")

if __name__ == "__main__":
    main()
