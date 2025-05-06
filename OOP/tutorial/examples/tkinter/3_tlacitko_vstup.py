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
        self.root.title("Ukázka tkinter aplikace")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

        # Úvodní popisek
        self.label = tk.Label(self.root, text="Zadejte odpověď na otázku.", font=("Arial", 14))
        self.label.pack(pady=20)

        # Otázka
        self.question_label = tk.Label(self.root, text="Je číslo 911 prvočíslo?", font=("Arial", 12, "bold"))
        self.question_label.pack(pady=10)

        # Label a vstupní pole pro odpověď
        self.answer_label = tk.Label(self.root, text="Odpověď:", font=("Arial", 12))
        self.answer_label.pack()

        self.answer_entry = tk.Entry(self.root, font=("Arial", 12), width=30)
        self.answer_entry.pack(pady=5)

        # Tlačítko pro kontrolu odpovědi
        self.button = tk.Button(self.root, text="Odeslat", font=("Arial", 12), command=self.on_button_click)
        self.button.pack(pady=10)

        # Výsledek kontroly odpovědi
        self.result_label = tk.Label(self.root, text="", font=("Arial", 12), fg="blue")
        self.result_label.pack(pady=10)

    def on_button_click(self):
        """
        Obsluha kliknutí na tlačítko. Vyhodnotí správnost odpovědi.
        """
        user_input = self.answer_entry.get().strip().lower()
        if user_input == "ano":
            self.result_label.config(text="Správně! 911 je prvočíslo.", fg="green")
        else:
            self.result_label.config(text="Špatná odpověď. 911 je skutečně prvočíslo.", fg="red")


if __name__ == "__main__":
    """
    Spouštěcí bod programu. Vytvoří hlavní okno a spustí aplikaci.
    """
    root = tk.Tk()
    app = SimpleApp(root)
    root.mainloop()
