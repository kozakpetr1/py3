class Product:
    
    def __init__(self, name):
        self.__name = name if name else None
        
    def __str__(self):
        return f"{self.__name}"

class PC(Product):
    
    def __init__(self, **kwargs):
        super().__init__(kwargs['name'])
        self.__CPU = kwargs['CPU'] if 'CPU' in kwargs else None
        self.__RAM = kwargs['RAM'] if 'RAM' in kwargs else None

    def __str__(self):
        return f"PC: {super().__str__()}, {self.__CPU}, {self.__RAM} GB"   

class Monitor(Product):

    def __init__(self, **kwargs):
        super().__init__(kwargs['name'])
        self.__diagonal = kwargs['diagonal'] if 'diagonal' in kwargs else None
        self.__resolution = kwargs['resolution'] if 'resolution' in kwargs else None
        
    def __str__(self):
        return f"Monitor: {super().__str__()}, {self.__diagonal}, {self.__resolution}"

class Keyboard(Product):

    def __init__(self, **kwargs):
        super().__init__(kwargs['name'])
        self.__type = kwargs['type'] if 'type' in kwargs else None

    def __str__(self):
        return f"Keyboard: {super().__str__()}, {self.__type}"

class Mouse(Product):

    def __init__(self, **kwargs):
        super().__init__(kwargs['name'])
        self.__type = kwargs['type'] if 'type' in kwargs else None

    def __str__(self):
        return f"Mouse: {super().__str__()}, {self.__type}"


class Factory:
    
    products = ['PC', 'Monitor', 'Keyboard', 'Mouse']

    @staticmethod
    def create(**kwargs):
        if kwargs['article'] in Factory.products:
            return globals()[kwargs['article']](**kwargs)
        else:
            return None
    
p = []
p.append(Factory.create(article = 'Monitor', name = 'HP', diagonal = '27', resolution = 'Full HD'))
p.append(Factory.create(article = 'PC', name = 'ASUS', CPU = 'i5', RAM = '16'))
p.append(Factory.create(article = 'Mouse', name = 'Genius', type = 'wireless'))
p.append(Factory.create(article = 'Keyboard', name = 'Genius', type = 'wireless'))

for prod in p:
    print(prod)
