# SAT Camera Frame Capture Microservice

Microservicio modular en Python encargado de capturar fotogramas en tiempo real desde la cámara del laboratorio:
`http://192.168.10.XX:19XX/laboratorio-cam/`

---

## 🛠️ Características

1. **Múltiples Estrategias de Captura**:
   - HTTP GET directo a endpoints de fotogramas (`/frame.jpeg`).
   - Endpoint de API go2rtc / MediaMTX (`http://192.168.10.XX:19XX/api/frame.jpeg?src=laboratorio-cam`).
   - OpenCV `cv2.VideoCapture` para streams RTSP / MJPEG.
   - Generación de imagen sintética de prueba para desarrollo/fallback cuando la cámara física está desconectada.
2. **REST API Integrada (FastAPI)**:
   - `GET /capture`: Retorna los bytes JPEG del fotograma actual.
   - `GET /health`: Estado del servicio de cámara.
3. **Integración con Telegram**: Permite adjuntar imágenes reales de la planta directamente en las alertas de anomalías del bot de Telegram.

---

## ⚙️ Configuración (`.env`)

```env
CAMERA_URL=http://192.168.10.XX:19XX/laboratorio-cam/
CAMERA_SNAPSHOT_URL=http://192.168.10.XX:19XX/laboratorio-cam/frame.jpeg
CAMERA_RTSP_URL=rtsp://192.168.10.XX:8554/laboratorio-cam
CAMERA_TIMEOUT_SECONDS=4
CAMERA_ENABLED=true
PORT=8005
```

---

## 🚀 Instalación y Uso

### 1. Instalación de Dependencias
```bash
pip install -r requirements.txt
```

### 2. Capturar Fotograma desde CLI
```bash
python main.py --snapshot --output captura.jpg
```

### 3. Iniciar Servidor REST API
```bash
python main.py --serve --port 8005
```

---

## ⚙️ Registro como Servicio del Sistema (`systemd` Daemon)

Para despliegues de producción 24/7 en Linux, crea el servicio `/etc/systemd/system/sat_camera_service.service`:

```ini
[Unit]
Description=SAT Camera Frame Capture Service
After=network.target network-online.target
Wants=network-online.target

[Service]
Type=simple
User=root
WorkingDirectory=/root/sat_camera_service

# Apuntar directamente al ejecutable Python dentro del entorno virtual (venv)
ExecStart=/root/sat_camera_service/venv/bin/python /root/sat_camera_service/main.py --serve --port 8005

Environment=PYTHONUNBUFFERED=1
Restart=always
RestartSec=5s
StandardOutput=journal
StandardError=journal
SyslogIdentifier=sat_camera_service

[Install]
WantedBy=multi-user.target
```

### Comandos de Gestión:
```bash
systemctl daemon-reload
systemctl enable sat_camera_service.service
systemctl start sat_camera_service.service
systemctl status sat_camera_service.service
journalctl -u sat_camera_service.service -f
```

