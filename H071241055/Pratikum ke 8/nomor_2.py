import re

def detect_ip_address(ip):
    # Pattern untuk IPv4
    ipv4_pattern = r'^((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$'
    
    # Pattern untuk IPv6
    ipv6_pattern = r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'
    
    # Cek apakah IP adalah IPv4
    if re.match(ipv4_pattern, ip):
        return "IPv4"
    
    # Cek apakah IP adalah IPv6
    elif re.match(ipv6_pattern, ip):
        return "IPv6"
    
    # Jika tidak memenuhi keduanya
    return "Bukan IP Address"

# Baca jumlah input
n = int(input("Masukkan jumlah baris: "))

# Loop untuk memproses setiap baris
for _ in range(n):
    ip_input = input().strip()
    print(detect_ip_address(ip_input))
