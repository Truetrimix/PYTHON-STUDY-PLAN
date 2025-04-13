#This code prints the data in .txt file

#The following code checks if the file exists. If it does, it will read the file and return the data. If it does not exist, it will print an error message.
def check_file_exists(file_path):
    try:
        with open(file_path, "r") as file:
            return True
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return False
#The following code checks if the file is empty. If it is, it will print an error message. If it is not, it will return True.
def check_file_not_empty(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read().strip()
            if not content:
                print(f"File is empty: {file_path}")
                return False
            return True
    except Exception as e:
        log_error(f"Error reading file for emptiness: {e}")
        return False

#The following code checks if the file is writable. If it is, it will return True. If it is not, it will print an error message.
def check_file_writable(file_path):
    try:
        with open(file_path, "a") as file:
            return True
    except Exception as e:
        print(f"Error checking file: {e}")
        return False

#if erros occur, the code will print the error messege in a .txt file, including date and time. If new error it will add the new error to the file.
def log_error(error_message):
    from datetime import datetime
    error_log_file = "/Users/simonlintu/Documents/Github/week3/Errors/error_log.txt"
    with open(error_log_file, "a") as log_file:
        log_file.write(f"{datetime.now()}: {error_message}\n")


#The following code is the main code. It asks the user to insert the file path for the .txt file. if anyy errors it will ask the user to insert the file path again. If the file is not empty, readable and writable, it will print a message saying that the file is ready to be read.
def main():
    file_path = input("Please enter file path for the .txt file: ")
    while True:
        if check_file_exists(file_path) and check_file_not_empty(file_path) and check_file_writable(file_path):
            print(f"The file {file_path} is ready to be read.")
            break
        else:
            file_path = input("Please enter a valid file path: ")
    with open(file_path, "r") as file:
        for line in file:
            print(line.strip())
if __name__ == "__main__":
    main()