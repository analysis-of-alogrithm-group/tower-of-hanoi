import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# def draw_on_canvas(canvas, color):
#     canvas.create_rectangle(20, 20, 80, 80, fill=color)
#
# # Create the main Tkinter window
# root = tk.Tk()
# root.title("Multiple Canvases Example")
#
# # Create and pack the first canvas
# canvas1 = tk.Canvas(root, width=100, height=100, bg="white")
# canvas1.pack(side=tk.LEFT)
# draw_on_canvas(canvas1, "red")
#
# # Create and pack the second canvas
# canvas2 = tk.Canvas(root, width=100, height=100, bg="white")
# canvas2.pack(side=tk.RIGHT)
# draw_on_canvas(canvas2, "blue")
#
# # Create and pack additional canvases as needed
#
# # Start the Tkinter event loop
# root.mainloop()

def start_action():
    try:
        disc_number = entry.getint(entry.get())
        print(disc_number)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

def quit_action():
    if messagebox.askokcancel("Quit", "Do you really want to quit?"):
        root.destroy()


root = tk.Tk()
root.geometry("1300x800")
root.title("Tower Of Hanoi")

ico = Image.open('icon.png')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)


frame = tk.Frame(root, padx=1, pady=1)
frame.pack(padx=10, pady=10)

# Label and entry for number of disks
label = tk.Label(frame, text="Enter the number of disks:")
label.pack()

# entry widget = textbox that accepts a single line of user input
entry = tk.Entry(frame)
entry.pack()

# Create a "Start" button
start_button = tk.Button(frame, text="Start", command=start_action, width=20, height=1)
start_button.pack(side=tk.TOP, padx=5, pady=5)

# Create a "Quit" button
quit_button = tk.Button(frame, text="Quit", command=quit_action, width=20, height=1)
quit_button.pack(side=tk.TOP, padx=5, pady=5)

canvas1 = tk.Canvas(frame, width=600, height=600, bg="white")
canvas1.place(x=-150, y=-150)
canvas1.pack(side=tk.LEFT)
canvas2 = tk.Canvas(frame, width=600, height=600, bg="white")
canvas2.place(x=150, y=150)
canvas2.pack(side=tk.RIGHT)

root.mainloop()
