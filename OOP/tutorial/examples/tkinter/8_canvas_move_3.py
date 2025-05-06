import tkinter as tk
import math

class MoverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Odraz od pevného objektu")

        self.canvas_width = 400
        self.canvas_height = 400
        self.canvas = tk.Canvas(root, width=self.canvas_width, height=self.canvas_height, bg='white')
        self.canvas.pack()

        # Parametry pohyblivého objektu
        self.moving_radius = 20
        self.fixed_radius = 30

        # Pevný objekt uprostřed
        cx = self.canvas_width // 2
        cy = self.canvas_height // 2
        self.fixed = self.canvas.create_oval(cx - self.fixed_radius, cy - self.fixed_radius,
                                             cx + self.fixed_radius, cy + self.fixed_radius,
                                             fill='gray')

        # Pohyblivý objekt (vlevo nahoře)
        mx, my = 60, 60
        self.moving = self.canvas.create_oval(mx - self.moving_radius, my - self.moving_radius,
                                              mx + self.moving_radius, my + self.moving_radius,
                                              fill='blue')

        self.vx = 0
        self.vy = 0
        self.friction = 0.99
        self.moving_flag = False

        self.root.bind('<Key>', self.start_movement)

    def start_movement(self, event):
        speed = 5
        if event.keysym == 'Up':
            self.vx, self.vy = 0, -speed
        elif event.keysym == 'Down':
            self.vx, self.vy = 0, speed
        elif event.keysym == 'Left':
            self.vx, self.vy = -speed, 0
        elif event.keysym == 'Right':
            self.vx, self.vy = speed, 0
        else:
            return

        if not self.moving_flag:
            self.moving_flag = True
            self.animate()

    def animate(self):
        if abs(self.vx) < 0.1 and abs(self.vy) < 0.1:
            self.moving_flag = False
            return

        # Aktuální pozice pohyblivého objektu
        x0, y0, x1, y1 = self.canvas.coords(self.moving)
        cx = (x0 + x1) / 2
        cy = (y0 + y1) / 2

        # Nová pozice
        new_cx = cx + self.vx
        new_cy = cy + self.vy

        # Detekce kolize se středovým objektem
        fx0, fy0, fx1, fy1 = self.canvas.coords(self.fixed)
        fcx = (fx0 + fx1) / 2
        fcy = (fy0 + fy1) / 2
        dist = math.hypot(new_cx - fcx, new_cy - fcy)
        min_dist = self.fixed_radius + self.moving_radius

        if dist <= min_dist:
            # Výpočet normály
            nx = new_cx - fcx
            ny = new_cy - fcy
            norm_length = math.hypot(nx, ny)
            if norm_length == 0:
                norm_length = 1  # prevence dělení nulou
            nx /= norm_length
            ny /= norm_length

            # Odražení vektoru podle rovnice: R = V - 2*(V·N)*N
            dot = self.vx * nx + self.vy * ny
            self.vx = self.vx - 2 * dot * nx
            self.vy = self.vy - 2 * dot * ny

        # Kontrola hranic
        if not (0 + self.moving_radius <= new_cx <= self.canvas_width - self.moving_radius):
            self.vx = -self.vx
        if not (0 + self.moving_radius <= new_cy <= self.canvas_height - self.moving_radius):
            self.vy = -self.vy

        # Pohyb a zpomalení
        self.canvas.move(self.moving, self.vx, self.vy)
        self.vx *= self.friction
        self.vy *= self.friction

        self.root.after(20, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    app = MoverApp(root)
    root.mainloop()
