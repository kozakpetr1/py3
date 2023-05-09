import tkinter as tk
# from cryptography.fernet import Fernet

# key = None

def load_key():
    return open("key.key", "rb").read()

# def decrypt(filename, key):
#    f = Fernet(key)
#    with open(filename, "rb") as file:
#        encrypted_data = file.read()
#    decrypted_data = f.decrypt(encrypted_data)
#    with open("Hesla-Petr.xlsx", "wb") as file:
#        file.write(decrypted_data)

root = tk.Tk()
root.title('Don\'t give up!')

canvas1 = tk.Canvas(root, width = 500, height = 150, bg = '#e8e8e8')
canvas1.pack()

def hello ():
    global key  
    label1 = tk.Label(root, text= 'Shit happens!', fg='black', bg = '#e8e8e8', font=('helvetica', 12, 'bold'))
#    key = load_key()
#    decrypt("Hesla.xlsx.cry", key)
    canvas1.create_window(250, 100, window=label1)
    
button1 = tk.Button(text='Guess what?', command=hello, bg='blue',fg='white')
canvas1.create_window(250, 50, window=button1)

root.mainloop()