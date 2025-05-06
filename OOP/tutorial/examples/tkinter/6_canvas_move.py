import tkinter as tk

class MoverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pohyb objektu na canvasu (OOP, s omezením)")

        self.canvas_width = 400
        self.canvas_height = 400

        self.canvas = tk.Canvas(root, width=self.canvas_width, height=self.canvas_height, bg='white')
        self.canvas.pack()

        # Vytvoření kruhu (40x40 px)
        self.circle_size = 40
        x0 = (self.canvas_width - self.circle_size) // 2
        y0 = (self.canvas_height - self.circle_size) // 2
        x1 = x0 + self.circle_size
        y1 = y0 + self.circle_size

        self.circle = self.canvas.create_oval(x0, y0, x1, y1, fill='blue')

        self.root.bind('<Key>', self.move_circle)

    def move_circle(self, event):
        dx, dy = 0, 0
        step = 10

        if event.keysym == 'Up':
            dy = -step
        elif event.keysym == 'Down':
            dy = step
        elif event.keysym == 'Left':
            dx = -step
        elif event.keysym == 'Right':
            dx = step

        # Získání aktuální pozice objektu
        x0, y0, x1, y1 = self.canvas.coords(self.circle)

        # Výpočet nové pozice
        new_x0 = x0 + dx
        new_y0 = y0 + dy
        new_x1 = x1 + dx
        new_y1 = y1 + dy

        # Kontrola, zda nová pozice bude v rámci canvasu
        if 0 <= new_x0 and new_x1 <= self.canvas_width and 0 <= new_y0 and new_y1 <= self.canvas_height:
            self.canvas.move(self.circle, dx, dy)

if __name__ == "__main__":
    root = tk.Tk()
    app = MoverApp(root)
    root.mainloop()
