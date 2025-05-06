import tkinter as tk

class SimpleApp:
    """
    Třída představující jednoduchou GUI aplikaci pomocí knihovny tkinter.
    """

    def __init__(self, root):
        """
        Inicializuje komponenty uživatelského rozhraní.

        Parametry:
        root (tk.Tk): Hlavní okno aplikace.
        """
        self.root = root
        self.root.title("Plíátno s tlačítkem - 800x600")
        self.root.geometry("800x600")         # Nastavení pevné velikosti okna
        self.root.resizable(False, False)     # Zákaz změny velikosti okna (šířka, výška)

        # Vytvoření štítku
        self.label = tk.Label(self.root, text="Stiskni tlačítko pro odpověď.", font=("Arial", 14))
        self.label.pack(pady=20)

        # Vytvoření tlačítka
        self.button = tk.Button(self.root, text="A tati, hoří hovno?", font=("Arial", 12), command=self.on_button_click)
        self.button.pack(pady=10)

    def on_button_click(self):
        """
        Obsluha události kliknutí na tlačítko.
        Změní text ve štítku.
        """
        self.label.config(text="To záleží. Třeba velbloudí ano.")


if __name__ == "__main__":
    """
    Spouštěcí bod programu. Vytvoří hlavní okno a spustí aplikaci.
    """
    root = tk.Tk()
    app = SimpleApp(root)
    root.mainloop()
