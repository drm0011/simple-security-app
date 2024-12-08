# app.py

import os

def insecure_code():
    # Use of an insecure function
    exec("print('Hello World')")

    # Hardcoded credentials
    username = "admin"
    password = "password123"

    # Insecure file permissions
    os.chmod("sensitive_file.txt", 0o777)


def main():
    insecure_code()


if __name__ == "__main__":
    main()
