class FileHandling:

    def read_from_file_bytearray(self, file_name):
        byte_list = []
        with open(f"{file_name}", "rb") as file:
            byte_list = bytearray(file.read())
        return byte_list
    
    def write_bytearray_to_file(self, byte_array, file_name):
        with open(f"{file_name}", "wb") as file:
            file.write(byte_array)