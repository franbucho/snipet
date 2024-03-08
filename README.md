# Script de Registro de Portapapeles y Captura de Cámara Frontal

Este script de Python permite registrar el contenido del portapapeles en un archivo de texto y capturar una imagen con la cámara frontal de la computadora. El registro se guarda junto con la dirección IP de la computadora y el nombre de la red WiFi a la que está conectada.

## Requisitos

- Python 3.x
- Bibliotecas Python:
  - `pyperclip`
  - `datetime`
  - `os`
  - `socket`
  - `wmi`
  - `pyautogui`
  - `opencv-python-headless`

## Instalación

1. Clona o descarga este repositorio en tu máquina local.

   ```bash
   git clone https://github.com/tu_usuario/registro-portapapeles-camara
   ```

2. Instala las bibliotecas requeridas. Puedes usar pip para instalarlas.

   ```bash
   pip install pyperclip datetime wmi pyautogui opencv-python-headless
   ```

## Uso

1. Ejecuta el script `time_test2.py` para registrar el contenido del portapapeles y capturar una imagen con la cámara frontal.

   ```bash
   python time_test2.py
   ```

2. El script guardará el registro del portapapeles en un archivo `clipboard_log.txt` en la carpeta `output`, junto con la imagen de la cámara frontal en la carpeta `output/FromCamera`.

## Estructura de Archivos

- `time_test2.py`: El script principal que realiza el registro del portapapeles y la captura de la cámara frontal.
- `output/`: Carpeta donde se guardan los archivos de salida.
  - `output/clipboard_log.txt`: Archivo de registro del portapapeles.
  - `output/FromCamera/`: Carpeta donde se guardan las imágenes de la cámara frontal.

## Notas

- Asegúrate de tener una cámara frontal disponible en tu dispositivo para la captura de imágenes.
- El LED indicador de la cámara se encenderá automáticamente cuando se active la cámara.
- Por razones de seguridad y privacidad, respeta las regulaciones y políticas de privacidad al utilizar la cámara.

## Contribuciones

¡Las contribuciones son bienvenidas! Si tienes sugerencias, mejoras o encuentras algún problema, por favor abre un [issue](https://github.com/tu_usuario/registro-portapapeles-camara/issues) o envía un [pull request](https://github.com/tu_usuario/registro-portapapeles-camara/pulls).

## Licencia

Este proyecto está bajo la [Licencia MIT](LICENSE).

---

Por supuesto, asegúrate de personalizar el contenido del `README.md` según las necesidades específicas de tu proyecto. Esto proporciona una guía básica sobre cómo instalar, ejecutar y utilizar tu script, así como también cómo contribuir al proyecto si otros desean hacerlo.

Espero que esto sea útil. Si necesitas más ayuda, no dudes en preguntar.
