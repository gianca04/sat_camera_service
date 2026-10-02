import os
from dotenv import load_dotenv
from pytapo import Tapo

def main():
    load_dotenv()
    
    tapo_ip = os.environ.get("TAPO_IP")
    tapo_user = os.environ.get("TAPO_USERNAME") # Para camaras KLAP, el usuario es el correo de la nube
    tapo_pass = os.environ.get("TAPO_PASSWORD") # La contrasena de la nube

    print("=== Test de conexion TAPO (Libreria Pytapo para Camaras) ===")
    
    if not tapo_ip or not tapo_user or not tapo_pass:
        print("Error: Asegurate de tener TAPO_IP, TAPO_USERNAME y TAPO_PASSWORD configurados en tu .env")
        return

    print(f"IP: {tapo_ip}")
    print(f"Usuario (Nube): {tapo_user}")
    print("Intentando autenticacion (Protocolo KLAP / Seguro)...")
    
    try:
        # Para camaras KLAP modernas, se usa directamente el correo y pass de la nube
        cam = Tapo(tapo_ip, tapo_user, tapo_pass)
        
        info = cam.getBasicInfo()
        print("¡Conectado exitosamente a la cámara!")
        print("Información básica:")
        for key, value in info.items():
            print(f"  {key}: {value}")
            
    except Exception as e:
        print(f"Fallo al conectar: {e}")
        print("\nSi el error persiste, verifica que:")
        print("1. El 'TAPO_CAMERA_USERNAME' sea el usuario configurado en la 'Cuenta de Cámara' en la app (por defecto suele ser admin).")
        print("2. La cámara esté conectada y la IP sea correcta.")

if __name__ == "__main__":
    main()
