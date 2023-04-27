import FileHandling as fileHandling
import Encryption as encryption
import os 
from os import system

def encrypt_folder_data():
    pass

def encrypt_specific_data():
    user_input = {}
    user_input["Input"] = input("What is the file name: ")
    user_input["Output"] = input("Export file name: ")    

    return user_input

def encrypt_data(user_input, code):
    fh = fileHandling.FileHandling()
    file_byte_array = fh.read_from_file_bytearray(user_input["Input"])

    enc = encryption.Encrypt()
    encrypted_data = enc.binary_encryption(file_byte_array, code)
    # encrypted_data = enc.binary_encryption(file_byte_array, 233)

    fh.write_bytearray_to_file(encrypted_data, user_input["Output"])

def file_name():
    arr = os.listdir("./images")

    for file in arr:
        print(file.strip())

def enter_codes():
    codes = []    
    while len(codes) < 3:        
        try:
            code = int(input(f"Enter the code {len(codes) + 1}: "))
            
            if (code > 256 or code < 0):
                raise Exception()
                
            codes.append(code)
        except:
            print("Incorrect Input")   

    return codes

def dashboard():
    
    print("\n", "-"*150)
    print("1. Single Doc\n2. Default Folder")
    print("\n", "-"*150)

def user_choice():
    user_choice = -1

    while (user_choice not in [1,2]):
        dashboard()
        user_choice = input("--> ")
        system('cls')

    return user_choice


if __name__ == "__main__":    
    choice = user_choice()
    codes = enter_codes()

    if (choice == 1):
        file_names = encrypt_specific_data()
        
