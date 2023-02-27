import socket
import sys

ip = input("IP adresini girin: ")
start_port = int(input("Başlangıç port numarasını girin: "))
end_port = int(input("Bitiş port numarasını girin: "))

for port in range(start_port, end_port + 1):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print("Port {} : Açık".format(port))
        sock.close()

    except KeyboardInterrupt:
        print("\nProgram sonlandırıldı.")
        sys.exit()

    except socket.gaierror:
        print("\nHostname bulunamadı.")
        sys.exit()

    except socket.error:
        print("\nBağlantı hatası.")
        sys.exit()