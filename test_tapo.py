import os
import asyncio
from dotenv import load_dotenv
from tapo import ApiClient

async def main():
    load_dotenv()
    
    tapo_username = os.environ.get("TAPO_USERNAME")
    tapo_password = os.environ.get("TAPO_PASSWORD")
    tapo_ip = os.environ.get("TAPO_IP")

    print("=== Test de conexion TAPO ===")

    if not tapo_username or not tapo_password:
        print("Error: Por favor configura 'TAPO_USERNAME' y 'TAPO_PASSWORD' en el archivo .env")
        return
        
    print(f"Inicializando ApiClient con usuario: {tapo_username}")
    try:
        client = ApiClient(tapo_username, tapo_password)
        print("Cliente inicializado correctamente.")
        
        if tapo_ip:
            models_to_test = ["c210", "c220", "tc70", "c325wb", "c225"]
            connected = False
            
            for model in models_to_test:
                print(f"Probando conexion como modelo: {model}...")
                try:
                    # Obtenemos la funcion correspondiente al modelo (ej: client.c210)
                    method = getattr(client, model)
                    device = await method(tapo_ip)
                    device_info = await device.get_device_info()
                    print(f"¡Conectado exitosamente usando el modelo {model}!")
                    print(f"Info del dispositivo: {device_info.to_dict() if hasattr(device_info, 'to_dict') else device_info}")
                    connected = True
                    break
                except Exception as e:
                    print(f"  -> Fallo con {model}: {e}")
            
            if not connected:
                print("No se pudo conectar con ninguno de los modelos intentados.")
                print("Asegurate de que las credenciales sean las correctas (verificables en la app Tapo).")
        else:
            print("No se detecto 'TAPO_IP' en el archivo .env.")

    except Exception as e:
        print(f"Error general durante el test: {e}")

if __name__ == "__main__":
    asyncio.run(main())
