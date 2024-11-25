class XorMe:
    
    def __init__(self, what, xor_num):
        self.__s = self.__crypto(what, xor_num)
    
    def __crypto(self, what, xor_num):
        
        ch = ""
        for c in what:
            ch += chr(ord(c) ^ xor_num)
        return ch

        # return ''.join(chr(ord(c) ^ xor_num) for c in what)
    
    def __str__(self):
        return self.__s

open_text = "You look like hell!"
xor_num = 30000

encrypted_text = XorMe(open_text, xor_num)
print(encrypted_text)

decrypted_text = XorMe(str(encrypted_text), xor_num)
print(decrypted_text)