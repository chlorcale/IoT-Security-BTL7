import paho.mqtt.client as mqtt
import ssl
import time
import random

# Thông số Gateway
BROKER = "localhost"
PORT = 8883
TOPIC = "hcmut/iot/sensor/data"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Kết nối Mutual TLS thành công!")
    else:
        print(f"❌ Kết nối thất bại, mã lỗi: {rc}")

client = mqtt.Client(client_id="Sensor_Node_01")
client.username_pw_set("iot_admin", "admin") # Khớp với file passwd
client.on_connect = on_connect

# Cấu hình chứng chỉ 2 chiều
client.tls_set(
    ca_certs="../pkis/ca.crt",      # CA để tin tưởng Server
    certfile="../pkis/client.crt",  # Chứng chỉ của chính mình để trình diện Server
    keyfile="../pkis/client.key",   # Khóa bí mật của chính mình
    tls_version=ssl.PROTOCOL_TLSv1_2
)

client.connect(BROKER, PORT)
client.loop_start()

try:
    while True:
        val = round(random.uniform(20.0, 35.0), 2)
        client.publish(TOPIC, f"Nhiet do: {val}C")
        print(f"🚀 Sending: {val}C (Encrypted via M-TLS)")
        time.sleep(5)
except KeyboardInterrupt:
    client.loop_stop()
    client.disconnect()