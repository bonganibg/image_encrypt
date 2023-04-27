class Encrypt: 
    def binary_encryption(self, byte_array, code):
        for index, line in enumerate(byte_array):            
            byte_array[index] = line ^ code

        return byte_array
    
