import tkinter as tk
from PIL import Image, ImageTk
import subprocess
import os

# Key detection
def on_key_press(event):
    if event.char == "1":
        open_gmail()
    elif event.char == "2":
       open_folder(r"C:/Users/Roger/software")
    else:
        print(f"Tecla {event.char} no asignada [!]")

# GUI Settings
def create_gui():
    root = tk.Tk()
    root.title("ROSengine")

    # Create a frame for the images
    frame = tk.Frame(root)
    frame.grid(row=0, column=0, columnspan=4, pady=10)  # Ajustado a 4 columnas

    # Iages.
    images = []
    for i in range(1, 2):  # The numbers and images must be the same. This is ready to have 1 action at the moment.
        image = Image.open(f"image_{i}.png")
        # Redimensionar la imagen manteniendo la relación de aspecto
        image.thumbnail((100, 100))
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(frame, image=photo)
        label.grid(row=0, column=i-1, padx=5)
        images.append(photo)

    # Numbers.
    for i in range(1, 2): # The numbers and images must be the same. This is ready to have 1 action at the moment.
        label = tk.Label(root, text=str(i))
        label.grid(row=1, column=i-1, pady=5)

  # Note: It is recommended that each function that is put like (open_gmail, open_folder...) should have its image in the same folder as the main.py script.

    root.bind('<Key>', on_key_press)

    root.mainloop()

def open_gmail():
    chrome_path = r"" # The address of chrome.exe on your computer.
    profile_name = "Default" # It's usually like this, but check it.
    gmail_url = "https://mail.google.com"
    subprocess.Popen([chrome_path, f'--profile-directory={profile_name}', gmail_url])

def open_folder(folder_path):
    if os.path.isdir(folder_path):
        subprocess.Popen(f'explorer {os.path.realpath(folder_path)}')
    else:
        print(f"Carpeta no encontrada: {folder_path}")

# Run the graphical user interface.
if __name__ == "__main__":
    create_gui()
