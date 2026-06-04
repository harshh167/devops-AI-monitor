import platform
import psutil
import socket

def get_server_metrics():
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
    except:
        ip_address = "127.0.0.1"
        
    return {
        "cpu": psutil.cpu_percent(interval=None),
        "ram": psutil.virtual_memory().percent,
        "os": f"{platform.system()} {platform.release()}",
        "ip": ip_address,
        "cpu_count": psutil.cpu_count(),
        "disk": psutil.disk_usage('/').percent,
        "network_sent": f"{psutil.net_io_counters().bytes_sent / (1024*1024):.2f} MB",
        "network_recv": f"{psutil.net_io_counters().bytes_recv / (1024*1024):.2f} MB"
    }
