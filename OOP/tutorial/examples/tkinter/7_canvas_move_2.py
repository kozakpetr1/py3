import tkinter as tk

class MoverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Zpomalený pohyb objektu")

        self.canvas_width = 400
        self.canvas_height = 400
        self.circle_size = 40

        self.canvas = tk.Canvas(root, width=self.canvas_width, height=self.canvas_height, bg='white')
        self.canvas.pack()

        # Vytvoření kruhu uprostřed canvasu
        x0 = (self.canvas_width - self.circle_size) // 2
        y0 = (self.canvas_height - self.circle_size) // 2
        x1 = x0 + self.circle_size
        y1 = y0 + self.circle_size

        self.circle = self.canvas.create_oval(x0, y0, x1, y1, fill='blue')

        # Inicializace směru a rychlosti
        self.vx = 0
        self.vy = 0
        self.friction = 0.9  # Koeficient odporu
        self.moving = False

        self.root.bind('<Key>', self.start_movement)

    def start_movement(self, event):
        step = 5  # Počáteční rychlost

        if event.keysym == 'Up':
            self.vx, self.vy = 0, -step
        elif event.keysym == 'Down':
            self.vx, self.vy = 0, step
        elif event.keysym == 'Left':
            self.vx, self.vy = -step, 0
        elif event.keysym == 'Right':
            self.vx, self.vy = step, 0
        else:
            return

        if not self.moving:
            self.moving = True
            self.animate()

    def animate(self):
        if abs(self.vx) < 0.1 and abs(self.vy) < 0.1:
            self.moving = False
            return

        # Aktuální pozice
        x0, y0, x1, y1 = self.canvas.coords(self.circle)

        # Nové souřadnice
        new_x0 = x0 + self.vx
        new_y0 = y0 + self.vy
        new_x1 = x1 + self.vx
        new_y1 = y1 + self.vy

        # Kontrola hranic
        if 0 <= new_x0 and new_x1 <= self.canvas_width:
            self.canvas.move(self.circle, self.vx, 0)
        else:
            self.vx = 0

        if 0 <= new_y0 and new_y1 <= self.canvas_height:
            self.canvas.move(self.circle, 0, self.vy)
        else:
            self.vy = 0

        # Aplikace "odporu"
        self.vx *= self.friction
        self.vy *= self.friction

        # Naplánování dalšího snímku
        self.root.after(20, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    app = MoverApp(root)
    root.mainloop()
