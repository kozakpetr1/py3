import re

class EncryptionInterface:
    """
    Informal interface in Python
    
    :param __key: Current encrpytion key
    :type str: str
    """
    
    def setKey(self, str = None):
        """
        Setter method to set / generate the encryption key - stores encryption key in __key property

        :param str: Parameter for initializing of the __key value
        :type str: str
        """
        pass

    def getKey(self) -> str:
        """
        Getter method to get the current __key value

        :return: __key attribute value
        :rtype: str
        """
        pass

    def encrypt(self, **kwargs) -> str:
        """
        Text encryption method - stores encrypted text in __encrypted property

        :param **kwargs: keyworded, variable length argument list
        :return: encrypted text
        :rtype: str
        """
        pass
    
    def decrypt(self, **kwargs) -> str:
        """
        Text decryption method - stores decrypted text in __decrypted property

        :param **kwargs: keyworded, variable length argument list
        :return: encrypted text
        :rtype: str
        """
        pass

class Caesar(EncryptionInterface):

    def __init__(self, **kwargs):
        self.__key = int(kwargs["key"]) if "key" in kwargs.keys() else 3
        self.__encrypted = ""
        self.__decrypted = ""
        self.__transcripted = ""

    def setKey(self, str = None):
        self.__key = int(str)

    def getKey(self) -> str:
        return self.__key

    def __transcript(self, str) -> str:
        txt = str
        new = txt.lower()
        new = re.sub(r'[àáâãäå]', 'a', new)
        new = re.sub(r'[èéêë]', 'e', new)
        new = re.sub(r'[ìíîï]', 'i', new)
        new = re.sub(r'[òóôõö]', 'o', new)
        new = re.sub(r'[ùúûüů]', 'u', new)
        new = re.sub(r'[ý]', 'y', new)
        new = re.sub(r'[žź]', 'z', new)
        new = re.sub(r'[šś]', 's', new)
        new = re.sub(r'[čć]', 'c', new)
        new = re.sub(r'[řŕ]', 'r', new)
        new = re.sub(r'[ď]', 'd', new)
        new = re.sub(r'[ť]', 't', new)
        new = re.sub(r'[ňń]', 'n', new)
        new = re.sub(r'[ .:;!?+-_]', '', new)
        new = new.upper()
        return new
            
    def encrypt(self, **kwargs) -> str:
        self.__transcripted = self.__transcript(str(kwargs["txt"]))
        if kwargs["showTranscripted"]: print(self.__transcripted)
        aIndex = ord("A")
        for c in self.__transcripted:
            cIndex = ord(c) - aIndex
            newCharacter = chr(((cIndex + self.__key) % 26) + aIndex)
            self.__encrypted += newCharacter

        return self.__encrypted
    
    def decrypt(self, **kwargs) -> str:
        self.__encrypted = str(kwargs["txt"]) if "txt" in kwargs.keys() else self.__encrypted
        aIndex = ord("A")
        for c in self.__encrypted:
            cIndex = ord(c) - aIndex
            newCharacter = chr(((cIndex - self.__key) % 26) + aIndex)
            self.__decrypted += newCharacter

        return self.__decrypted

S = Caesar(key = 5)

encrTxt = S.encrypt(txt = "čšUŽř šsůúiýáď+-", showTranscripted = True)
print(encrTxt)

decrTxt = S.decrypt(txt = encrTxt)
print(decrTxt)
