class Furniture:
    
    # uprav kód tak, aby v případě, že nebyly zadány hodnoty vstupních parametrů (kromě amount) proběhl raise výjimky
    def __init__(self, **kwargs):
        if "material" in kwargs:
            self.__material = kwargs["material"]
        else:
            raise ValueError("Parameter material missing.")
        self.__width = kwargs["width"]
        self.__height = kwargs["height"]
        self.__depth = kwargs["depth"] 
        self.__amount = kwargs["amount"] if ("amount" in kwargs) else 1
    
    # doplň kód pro zobrazení vlastností objektu
    def __str__(self):
        return f"Material: {self.__material}\nWidth: {self.__width}\nHeight: {self.__height}\nDepth: {self.__depth}\nAmount: {self.__amount}"
         
class Table(Furniture):
    
    # doplň kód pro zobrazení vlastností objektu
    def __str__(self):
        return f"Table\n" + super().__str__()


class Chair(Furniture):
    
    # doplň kód pro zobrazení vlastností objektu
    def __str__(self):
        return f"Chair\n" + super().__str__()

class ChestOfDrawers(Furniture):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__num_of_drawers = kwargs["drawers"]
        
    # doplň kód pro zobrazení vlastností objektu
    def __str__(self):
        return f"Chest of drawers\nNumber of drawers: {self.__num_of_drawers}\n" + super().__str__()

class ShelfCabinet(Furniture):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__num_of_shelves = kwargs["shelves"]
    
    # doplň kód pro zobrazení vlastností objektu
    def __str__(self):
        return f"Shelf cabinet\nNumber of shelves:{self.__num_of_shelves}\n" + super().__str__()

class Factory:
    
    # doplň kód pro "výrobu nábytku", metody vrátí objekt nebo provede raise výjimky
    def make(self, **kwargs):
        match kwargs["furniture"]:
            case "table":
                return Table(**kwargs)
            case "chair":
                return Chair(**kwargs)
            case "chest of drawers":
                return ChestOfDrawers(**kwargs)
            case "shelf cabinet":
                return ShelfCabinet(**kwargs)
            case _: 
                raise ValueError("Can't make this kind of furniture.")
              
f = Factory()
chest_of_drawers = f.make(
    furniture = "chest of drawers",
    material = "oak",
    width = 90,
    height = 180,
    depth = 60,
    drawers = 4
)
print(chest_of_drawers)

table = f.make(
    furniture = "table",
    material = "oak",
    width = 70,
    height = 75,
    depth = 130
)
print(table)