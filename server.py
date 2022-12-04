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
        self.__sockIp = sockIP
        self.__sockPort = sockPort
        print(f"Socket IP: {(str(self.__sockIp))}\nPort: {self.__sockPort}")
        
    # Startet den Server und sendet nach erhalt der Daten die Größe in Byte zurück
    def runningServer(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.__sockIp,self.__sockPort))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print(f"\nEingehende Verbindung von {addr}")
                while True:
                    data = conn.recv(1024)
                    client_msg = data.decode()
                    print(f"Client send: {client_msg}")
                    conn.send(f"Datenpaket mit {len(client_msg.encode('utf-8'))} byte erhalten".encode())
                    if client_msg == "shutdown":
                        break
                s.close()
                
myServer = Server("750W", cpuinfo.get_cpu_info()['brand_raw'], psutil.cpu_freq().max, psutil.virtual_memory().total, platform.system(), socket.gethostbyname(socket.gethostname()), "TCP-Socket Server")
myServer.getInfo()
print(f"Service: {myServer._service}")
myServer.createSocket("127.0.0.1", 1337)
myServer.runningServer()
