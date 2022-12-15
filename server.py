import computer, socket, psutil, sys, platform, cpuinfo
class Server(computer.Computer):
    _service = ""
    __sockIp = ""
    __sockPort = 0
    # Bei Initialisierung wird der auch der service als Übergabeparameter gefordet und ruft die __init__ der Parent-Klasse auf
    def __init__(self,power_supply, cpu, cpu_speed,ram,os,ip,service):
        super().__init__(power_supply, cpu, cpu_speed,ram,os,ip)
        self._service = service
        
    def createSocket(self, sockIP,sockPort):
        try:
            self.__sockIp = sockIP
            self.__sockPort = sockPort
            web_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            web_socket.bind((self.__sockIp, self.__sockPort))
            self.__sock = web_socket
            print(f"Socket IP: {(str(self.__sockIp))}\nPort: {self.__sockPort}")
        except Exception as error:
            print(f"Fehler bei erstellung des Sockets: {error}]")

    # Startet den Server und sendet nach erhalt der Daten die Größe in Byte zurück
    def runningServer(self):
        try:
            web_socket = self.__sock
            web_socket.listen()
            conn, addr = web_socket.accept()
            with conn:
                print(f"\nEingehende Verbindung von {addr}")
                while True:
                    data = conn.recv(1024)
                    client_msg = data.decode()
                    print(f"Client send: {client_msg}")
                    conn.send(f"Datenpaket mit {len(client_msg.encode('utf-8'))} byte erhalten".encode())
                    if client_msg == "shutdown":
                        break
                    elif client_msg == "exit":
                        conn.detach()
                        self.runningServer()
                web_socket.close()
        except Exception as error:
            print(f"Fehler bei Serverausführung: {error}]")

myServer = Server("750W", cpuinfo.get_cpu_info()['brand_raw'], psutil.cpu_freq().max, psutil.virtual_memory().total, platform.system(), socket.gethostbyname(socket.gethostname()), "TCP-Socket Server")
myServer.getInfo()
print(f"Service: {myServer._service}")
myServer.createSocket("127.0.0.1", 1337)
myServer.runningServer()
