import FileHandling as fileHandling
import Encryption as encryption
import os 

def encrypt_folder_data():
    pass

def encrypt_specific_data():
    user_input = {}
    user_input["Input"] = input("What is the file name: ")
    user_input["Output"] = input("Export file name: ")    

    return user_input

def encrypt_data(user_input, codes):
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

if __name__ == "__main__":
    print("\n", "-"*150)
    print("1. Single Doc\n2. Default Folder")
    print("\n", "-"*150)