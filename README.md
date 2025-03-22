
## Visualizador de Algoritmos de Ordenamiento
##### Este es un programa en Python con interfaz gráfica que permite visualizar el funcionamiento de los algoritmos de ordenamiento Bubble Sort y Selection Sort. La interfaz está construida con tkinter y ttkbootstrap para mejorar la apariencia.**

### Características
- Generación de datos aleatorios.

- Visualización del proceso de ordenamiento.

- Selección de algoritmo de ordenamiento.

- Ajuste de la velocidad de ejecución.

### Requisitos

Asegúrate de tener Python instalado en tu sistema. Además, instala las siguientes dependencias:
```python
pip install  ttkbootstrap
```
### Algoritmos Implementados

##### Bubble Sort
Este algoritmo compara pares de elementos adyacentes y los intercambia si están en el orden incorrecto. Se repite hasta que la lista está ordenada.
```python
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
```

Selection Sort

Este algoritmo busca el elemento más pequeño en cada iteración y lo coloca en su posición correcta.
```python
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

```
### Estructura de la Interfaz
La interfaz gráfica está diseñada con tkinter y ttkbootstrap para mejorar su apariencia. Se compone de:

- Un menú desplegable para seleccionar el algoritmo de ordenamiento.
Permite seleccionar el algoritmo de ordenamiento.


```python
algo_menu = ttk.Combobox(frame, values=["Bubble Sort", "Selection Sort"])
algo_menu.grid(row=0, column=0, padx=10)
algo_menu.current(0)

```

- Una barra deslizante para ajustar la velocidad de ejecución.

  Permite ajustar la velocidad de ejecución.

```python
speed_scale = ttk.Scale(frame, from_=0.01, to=0.5, length=200, value=0.1)
speed_scale.grid(row=0, column=1, padx=10)

```
- Un botón "Generar Datos" para crear una nueva lista de números aleatorios.

Genera una lista de números aleatorios.

```python
generate_button = ttk.Button(frame, text="Generar Datos", command=generate_data)
generate_button.grid(row=0, column=2, padx=10)

```

- Un botón "Ordenar" para iniciar el proceso de ordenamiento.
Inicia el proceso de ordenamiento.

```python
start_button = ttk.Button(frame, text="Ordenar", command=start_sorting)
start_button.grid(row=0, column=3, padx=10)

```
- Un lienzo gráfico (Canvas) donde se visualizan los datos y sus cambios durante la ejecución del algoritmo.
Se encarga de visualizar los datos y sus cambios durante el ordenamiento.

```python
canvas = tk.Canvas(root, width=600, height=400, bg="white")
canvas.pack(pady=20)

```
