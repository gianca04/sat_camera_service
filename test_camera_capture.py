import os
import sys
from dotenv import load_dotenv

# Asegurar que se puede importar desde el directorio actual
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from camera_capturer import CameraCapturer

def main():
    print("=== Test de captura usando CameraCapturer (RTSP/HTTP) ===")
    
    # Cargar .env para asegurarse de tener la configuración correcta
    load_dotenv()
    
    # Instanciar el capturador del proyecto
    capturer = CameraCapturer()
    
    print("Intentando capturar frame...")
    frame_bytes = capturer.capturar_frame()
    
    if frame_bytes is not None:
        filename = "test_snapshot.jpg"
        with open(filename, "wb") as f:
            f.write(frame_bytes)
        print("Exito! Fotografia capturada exitosamente.")
        print(f"Tamano de la imagen: {len(frame_bytes)} bytes")
        print(f"Guardada como: {filename}")
    else:
        print("Error: No se pudo capturar la fotografia.")
        print("Revisa la configuración de CAMERA_RTSP_URL o CAMERA_SNAPSHOT_URL en tu .env")

if __name__ == "__main__":
    main()
