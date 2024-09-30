import tkinter as tk
import json

class Formular(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.jmeno_label = tk.Label(self.master, text="Jméno:")
        self.jmeno_entry = tk.Entry(self.master)

        self.prijmeni_label = tk.Label(self.master, text="Příjmení:")
        self.prijmeni_entry = tk.Entry(self.master)

        self.datum_narozeni_label = tk.Label(self.master, text="Datum narození:")
        self.datum_narozeni_entry = tk.Entry(self.master)

        self.ulozit_button = tk.Button(self.master, text="Uložit", command=self.ulozit_data)

        self.jmeno_label.pack()
        self.jmeno_entry.pack()

        self.prijmeni_label.pack()
        self.prijmeni_entry.pack()

        self.datum_narozeni_label.pack()
        self.datum_narozeni_entry.pack()

        self.ulozit_button.pack()

    def ulozit_data(self):
        jmeno = self.jmeno_entry.get()
        prijmeni = self.prijmeni_entry.get()
        datum_narozeni = self.datum_narozeni_entry.get()

        data = {
            "jmeno": jmeno,
            "prijmeni": prijmeni,
            "datum_narozeni": datum_narozeni
        }

        with open("data.json", "w") as f:
            json.dump(data, f)

        print("Data byla uložena do souboru data.json")

if __name__ == "__main__":
    root = tk.Tk()
    formular = Formular(root)
    root.mainloop()
