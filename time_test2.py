import pyperclip
from datetime import datetime
import os
import socket
import wmi
import pyautogui
import cv2

# Obtener el contenido del portapapeles
clipboard_content = pyperclip.paste()

# Obtener la fecha y hora actual
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Obtener la dirección IP de la PC
ip_address = socket.gethostbyname(socket.gethostname())

# Obtener el nombre de la red a la que está conectada la PC
c = wmi.WMI()
for interface in c.Win32_NetworkAdapterConfiguration(IPEnabled=True):
    if interface.Description.startswith("Wi-Fi"):
        network_name = interface.Caption.split(" - ")[-1]
        break
else:
    network_name = "Desconocido"

# Directorio para guardar la imagen desde la cámara frontal
output_directory = "C:/Users/Admin/Desktop/Code/time/output/FromCamera"

# Comprobar si el directorio existe, si no, crearlo
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Nombre de archivo para la imagen de la cámara frontal
camera_image_name = f"{timestamp}_front_camera.jpg"

# Ruta completa del archivo de la imagen de la cámara frontal
camera_image_path = os.path.join(output_directory, camera_image_name)

# Crear el separador para identificar cada ejecución
separator = "-------------------------------------------------------------------------\n"

# Crear el registro con el timestamp de la ejecución, IP y red
log_entry = f"{timestamp}\nIP: {ip_address}\nRed WiFi: {network_name}\n{clipboard_content}\n\n"

# Capturar la pantalla y guardarla en la subcarpeta de salida
pyautogui.screenshot(camera_image_path)

# Inicializar la cámara frontal
cap = cv2.VideoCapture(0)
ret, frame = cap.read()

# Guardar la imagen de la cámara frontal
cv2.imwrite(camera_image_path, frame)

# Liberar la cámara frontal
cap.release()

# Nombre del archivo donde se guarda el contenido del portapapeles
file_name = "clipboard_log.txt"

# Ruta completa del archivo del registro
file_path = os.path.join(output_directory, file_name)

# Leer el contenido actual del archivo si existe
if os.path.exists(file_path):
    with open(file_path, "r") as file:
        existing_content = file.read()
else:
    existing_content = ""

# Verificar si el nuevo contenido es diferente del contenido existente
if log_entry.strip() != existing_content.strip():
    # Agregar el nuevo registro al contenido existente con el separador
    new_content = f"{separator}{log_entry}{existing_content}"

    # Escribir el nuevo contenido al archivo
    with open(file_path, "w") as file:
        file.write(new_content)
    print(f"Contenido del portapapeles guardado en: {file_path}")
else:
    print("Clipboard no modificado. No se ha guardado nada.")
