import tkinter as tk
import time

def update_clock():
    # Función para actualizar el reloj
    current_time = time.strftime('%H:%M:%S')
    label.config(text=current_time)
    label.after(1000, update_clock)  # Actualizar cada segundo (1000 ms)

# Crear la ventana
root = tk.Tk()
root.title("Reloj")

# Crear una etiqueta para mostrar el reloj
label = tk.Label(root, font=('Helvetica', 48), fg='black')
label.pack(padx=20, pady=20)

# Llamar a la función para iniciar el reloj
update_clock()

# Ejecutar el bucle principal de tkinter
root.mainloop()
