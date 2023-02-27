import time
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

def feed_unicorn():
    global unicorn_health, progress_bar
    unicorn_health += 10
    progress_bar['value'] = unicorn_health
    update_progress_bar()
    if unicorn_health >= 100:
        result_label.config(text="Congratulations! You have successfully taken care of your unicorn and raised its health to 100. You win!")

def give_water():
    global unicorn_health, progress_bar
    unicorn_health += 5
    progress_bar['value'] = unicorn_health
    update_progress_bar()
    if unicorn_health >= 100:
        result_label.config(text="Congratulations! You have successfully taken care of your unicorn and raised its health to 100. You win!")

def take_walk():
    global unicorn_health, progress_bar
    unicorn_health += 15
    progress_bar['value'] = unicorn_health
    update_progress_bar()
    if unicorn_health >= 100:
        result_label.config(text="Congratulations! You have successfully taken care of your unicorn and raised its health to 100. You win!")

def update_progress_bar():
    if unicorn_health < 60:
        progress_bar['style'] = 'red.Horizontal.TProgressbar'
    elif unicorn_health < 80:
        progress_bar['style'] = 'blue.Horizontal.TProgressbar'
    elif unicorn_health < 100:
        progress_bar['style'] = 'yellow.Horizontal.TProgressbar'
    else:
        progress_bar['style'] = 'pink.Horizontal.TProgressbar'

def play_game():
    global unicorn_health, progress_bar, result_label
    unicorn_health = 50
    root = tk.Tk()
    root.title("Unicorn Pet by Avery")
    root.geometry("800x600")
    
    # Load images
    food_image = ImageTk.PhotoImage(Image.open("food.png"))
    water_image = ImageTk.PhotoImage(Image.open("water.png"))
    walk_image = ImageTk.PhotoImage(Image.open("walk.png"))
    
    # Create UI elements
    unicorn_image = ImageTk.PhotoImage(Image.open("unicorn.png"))
    unicorn_label = tk.Label(root, image=unicorn_image)
    unicorn_label.pack(pady=10)
    unicorn_label.place(x=0, y=50, width=200, height=200)
    health_label = tk.Label(root, text="Your unicorn's health is currently at " + str(unicorn_health))
    health_label.pack(pady=10)
    progress_frame = tk.Frame(root, width=200, height=20)
    progress_frame.pack(pady=10)
    progress_bar = ttk.Progressbar(progress_frame, orient=tk.HORIZONTAL, length=200, mode='determinate', value=unicorn_health)
    progress_bar.pack(side=tk.LEFT)
    s = ttk.Style()
    s.theme_use('clam')
    s.configure('red.Horizontal.TProgressbar', foreground='red', background='red')
    s.configure('blue.Horizontal.TProgressbar', foreground='blue', background='blue')
    s.configure('yellow.Horizontal.TProgressbar', foreground='yellow', background='yellow')
    s.configure('pink.Horizontal.TProgressbar', foreground='pink', background='pink')
    progress_bar['style'] = 'blue.Horizontal.TProgressbar'
    food_button = tk.Button(root, image=food_image, command=feed_unicorn)
    food_button.pack(pady=10)
    food_button.place(x=150, y=150, width=200, height=200)
    water_button = tk.Button(root, image=water_image, command=give_water)
    water_button.pack(pady=10)
    water_button.place(x=350, y=150, width=200, height=200)
    walk_button = tk.Button(root, image=walk_image, command=take_walk)
    walk_button.pack(pady=10)
    walk_button.place(x=550, y=150, width=200, height=200)
    result_label = tk.Label(root, text="")
    result_label.pack(pady=10)
    
    root.mainloop()


if __name__ == "__main__":
    play_game()
