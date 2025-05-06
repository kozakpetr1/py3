import tkinter as tk

class ImageGridApp:
    """
    Aplikace zobrazující mřížku 3x2 obrázků, které vyplňují celou plochu s paddingem.
    """

    def __init__(self, root):
        """
        Inicializuje hlavní okno a rozmístí obrázky v gridu.

        Parametry:
        root (tk.Tk): hlavní okno aplikace.
        """
        self.root = root
        self.root.title("Mřížka 3x2 obrázků")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

        self.canvas_width = 800
        self.canvas_height = 600
        self.padding = 20
        self.rows = 3
        self.columns = 2

        # Výpočet dostupné šířky/výšky pro obrázky
        image_width = (self.canvas_width - (self.columns + 1) * self.padding) // self.columns
        image_height = (self.canvas_height - (self.rows + 1) * self.padding) // self.rows

        self.images = []
        colors = ["red", "green", "blue", "yellow", "cyan", "magenta"]

        for color in colors:
            img = tk.PhotoImage(width=image_width, height=image_height)
            img.put(color, to=(0, 0, image_width, image_height))
            self.images.append(img)

        # Rozmístění obrázků do gridu s paddingem
        index = 0
        for row in range(self.rows):
            for col in range(self.columns):
                label = tk.Label(self.root, image=self.images[index])
                label.place(
                    x=self.padding + col * (image_width + self.padding),
                    y=self.padding + row * (image_height + self.padding),
                    width=image_width,
                    height=image_height
                )
                index += 1


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageGridApp(root)
    root.mainloop()
