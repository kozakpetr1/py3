import tkinter as tk
from tkinter import filedialog, messagebox

class TextEditorApp:
    """
    Jednoduchá textová aplikace s editorem, který umožňuje otevřít a uložit textové soubory.
    """

    def __init__(self, root):
        """
        Inicializuje hlavní okno a vytvoří widgety.
        
        Parametry:
        root (tk.Tk): Hlavní okno aplikace.
        """
        self.root = root
        self.root.title("Jednoduchý Textový Editor")
        self.root.geometry("800x600")
        
        # Vytvoření textového widgetu pro úpravu textu
        self.text_area = tk.Text(self.root, wrap="word", font=("Arial", 12))
        self.text_area.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

        # Vytvoření hlavního menu
        self.create_menu()

    def create_menu(self):
        """
        Vytvoří menu s možnostmi pro otevření a uložení souborů.
        """
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        # Menu File
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        
        # Možnost otevření souboru
        file_menu.add_command(label="Open", command=self.open_file)
        
        # Možnost uložení souboru
        file_menu.add_command(label="Save", command=self.save_file)

    def open_file(self):
        """
        Otevře textový soubor a načte jeho obsah do textového widgetu.
        """
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    file_content = file.read()
                    self.text_area.delete(1.0, tk.END)  # Smazání aktuálního obsahu
                    self.text_area.insert(tk.END, file_content)  # Načtení souboru do textového widgetu
            except Exception as e:
                messagebox.showerror("Chyba", f"Chyba při otevírání souboru: {e}")

    def save_file(self):
        """
        Uloží obsah textového widgetu do textového souboru.
        """
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as file:
                    file_content = self.text_area.get(1.0, tk.END)
                    file.write(file_content.strip())  # Uložení textu z textového widgetu
                messagebox.showinfo("Uloženo", "Soubor byl úspěšně uložen.")
            except Exception as e:
                messagebox.showerror("Chyba", f"Chyba při ukládání souboru: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditorApp(root)
    root.mainloop()
