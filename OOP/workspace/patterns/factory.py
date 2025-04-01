class Shape:
    def render(self):
        print("Initializing to render some shape...")
        
class Square(Shape):
    def render(self):
        super().render()
        print("Rendering square...")
        
class Triangle(Shape):
    def render(self):
        super().render()
        print("Rendering Triangle...")

class Circle(Shape):
    def render(self):
        super().render()
        print("Rendering Circle...")

s1 = Square()
s1.render()

t1 = Triangle()
t1.render()

c1 = Circle()
c1.render()