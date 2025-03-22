import tkinter as tk
from tkinter import ttk
import random
import time
import ttkbootstrap as tb


def bubble_sort(data, draw_data, speed):
    n = len(data)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
                draw_data(data, ["red" if x == j or x == j + 1 else "blue" for x in range(len(data))])
                time.sleep(speed)
        if not swapped:
            break


def selection_sort(data, draw_data, speed):
    n = len(data)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if data[j] < data[min_idx]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
        draw_data(data, ["red" if x == i or x == min_idx else "blue" for x in range(len(data))])
        time.sleep(speed)


def draw_data(data, color_array):
    canvas.delete("all")
    c_width = 600
    c_height = 400
    x_width = c_width / (len(data) + 1)
    offset = 30
    spacing = 10
    max_height = max(data)

    for i, value in enumerate(data):
        x0 = i * x_width + offset
        y0 = c_height - (value / max_height) * (c_height - 50)
        x1 = (i + 1) * x_width + offset - spacing
        y1 = c_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=color_array[i])
        canvas.create_text((x0 + x1) / 2, y0 - 10, text=str(value), fill="white", font=("Arial", 10))
    root.update_idletasks()


def generate_data():
    global data
    data = [random.randint(10, 100) for _ in range(30)]
    draw_data(data, ["blue" for _ in range(len(data))])


def start_sorting():
    global data
    speed = speed_scale.get()
    algo = algo_menu.get()

    if algo == "Bubble Sort":
        bubble_sort(data, draw_data, speed)
    elif algo == "Selection Sort":
        selection_sort(data, draw_data, speed)
    draw_data(data, ["green" for _ in range(len(data))])


root = tb.Window(themename="darkly")
root.title("Visualizador de Algoritmos de Ordenamiento")
root.geometry("700x500")

frame = ttk.Frame(root)
frame.pack(pady=20)

algo_menu = ttk.Combobox(frame, values=["Bubble Sort", "Selection Sort"])
algo_menu.grid(row=0, column=0, padx=10)
algo_menu.current(0)

speed_scale = ttk.Scale(frame, from_=0.01, to=0.5, length=200, value=0.1)
speed_scale.grid(row=0, column=1, padx=10)

generate_button = ttk.Button(frame, text="Generar Datos", command=generate_data)
generate_button.grid(row=0, column=2, padx=10)

start_button = ttk.Button(frame, text="Ordenar", command=start_sorting)
start_button.grid(row=0, column=3, padx=10)

canvas = tk.Canvas(root, width=600, height=400, bg="white")
canvas.pack(pady=20)

data = []
generate_data()

root.mainloop()
