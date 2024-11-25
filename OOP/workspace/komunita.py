class Community:

    class Member:
    
        def __init__(self, member_id, nick_name):
            self.__id = member_id
            self.__nick = nick_name
        
        def getID(self):
            return self.__id
    
        def getNick(self):
            return self.__nick

        def __str__(self):
            return f"{self.__id}: {self.__nick}"

    def __init__(self, name) -> None:
        self.__name = name
        self.__members = []
        
    def getName(self):
        return self.__name
    
    def addMember(self, member_id, nick_name):
        self.__members.append(self.Member(member_id, nick_name)) # [1. člen (objekt), 2. člen, 3. člen]
        
    def removeMember(self, id):
        for m in self.__members:
            if m.getID() == id:
                self.__members.remove(m)
        
    def getMembers(self):
        return self.__members
                
    
aa = Community("Anonymní alkoholici")

aa.addMember(1, "Dalibor")
aa.addMember(2, "Daniel")
aa.addMember(3, "Matěj")

aa.removeMember(2)

print(aa.getName())
for member in aa.getMembers():
    print(member)
    
