# IoT-Security-BTL7: Secure Gateway with M-TLS & Suricata IDS

Dự án triển khai mô hình phòng thủ chiều sâu cho hệ thống IoT, tập trung vào việc bảo mật luồng dữ liệu từ Sensor Node đến Gateway và giám sát xâm nhập.

##  Các lớp bảo mật chính
1. **Encryption (TLS 1.2):** Mã hóa toàn bộ dữ liệu MQTT trên cổng 8883.
2. **Authentication (M-TLS):** Xác thực hai chiều giữa Broker và Sensor thông qua chứng chỉ số.
3. **Detection (IDS):** Sử dụng Suricata để phát hiện các hành vi quét cổng (Port Scan) và tấn công DoS.

##  Cấu trúc thư mục
- `srcs/gateway`: Cấu hình Mosquitto Broker và tệp ACL.
- `srcs/sensor`: Mã nguồn giả lập thiết bị (Python).
- `srcs/pkis`: Lưu trữ các chứng chỉ (CA, Server, Client).
- `refs/`: File bắt gói tin `.pcap` và các bộ luật cho Suricata.

##  Hướng dẫn triển khai nhanh (Quick Start)

### 1. Khởi động Mosquitto Broker
```bash
cd srcs/gateway
mosquitto -c mosquitto.conf -v
```
### 2. Chạy Sensor Node
```bash
cd srcs/sensor
python3 iot_sensor.py
```
### 3. Vận hành Suricata IDS
```bash
sudo suricata -c /etc/suricata/suricata.yaml -S refs/local.rules --pcap=lo
```
## Kết quả thực nghiệm
Hệ thống đã được kiểm chứng qua:

Wireshark: Xác nhận dữ liệu đã mã hóa (Encrypted Application Data).

<img width="1531" height="825" alt="image" src="https://github.com/user-attachments/assets/3895a6de-f186-4387-b73f-b95f046965ee" />


Suricata Logs: Ghi nhận cảnh báo quét cổng từ công cụ Nmap.

<img width="1124" height="258" alt="image" src="https://github.com/user-attachments/assets/9397c09d-19c3-464d-8580-4d58f34a114a" />
<img width="1301" height="287" alt="image" src="https://github.com/user-attachments/assets/11eb2629-c5ac-4565-99f2-1282fddf3184" />

