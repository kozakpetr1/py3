class Texto:
    """
    String manipulation operation.
    
    :param str: Text string to manipulate.
    :type str: str
    """

    def __init__(self, str):
        """
        Assign a string when the object is initialized.

        :param str: Text string to initialize.
        :type str: str
        """

        self.str = str
    
    def getS(self):
        """
        Getter returns value of a str attribute.

        :return: str attribute value
        :rtype: str
        """

        return self.str
    
    def replaS(self, what, byWhat, str = None):
        """
        Method replaces 'what' substring by 'byWhat' substring
        inside the value of a str attribute.

        :param what: Input substring to by replaced.
        :type what: str

        :param byWhat: Output substring to replace.
        :type byWhat: str

        :param str: Optional text string to manipulate.
        :type str: str
        """

        if not str == None: self.str = str
        self.str = self.str.replace(what, byWhat)
        