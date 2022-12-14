#!./env/bin/python
import computer, socket, psutil, sys, platform, cpuinfo, datetime
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
            self.web_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.web_socket.bind((self.__sockIp, self.__sockPort))
            print(f"Socket IP: {(str(self.__sockIp))}\nPort: {self.__sockPort}")
        except Exception as error:
            print(f"Fehler bei erstellung des Sockets: {error}]")

    # Startet den Server und sendet nach erhalt der Daten die Größe in Byte zurück
    def runningServer(self):
        try:
            self.web_socket.listen()
            conn, addr = self.web_socket.accept()
            with conn:
                print(f"\nEingehende Verbindung von {addr[0]}:{self.__sockPort}")
                dateNow = datetime.datetime.now()
                formatted_time = dateNow.strftime("%d/%m/%Y, %H:%M:%S")
                while True:
                    data = conn.recv(1024)
                    client_msg = data.decode()
                    print(f"{formatted_time}\nClient with IP: {addr[0]} sent: {client_msg}")
                    conn.send(f"Datenpaket mit {len(client_msg.encode('utf-8'))} byte erhalten".encode())
                    if client_msg == "shutdown":
                        break
                    elif client_msg == "exit":
                        conn.detach()
                        self.runningServer()
                self.web_socket.close()
        except Exception as error:
            print(f"Fehler bei Serverausführung: {error}]")

myServer = Server("750W", cpuinfo.get_cpu_info()['brand_raw'], psutil.cpu_freq().max, psutil.virtual_memory().total, platform.system(), socket.gethostbyname(socket.gethostname()), "TCP-Socket Server")
myServer.getInfo()
print(f"Service: {myServer._service}")
myServer.createSocket("127.0.0.1", 1337)
myServer.runningServer()
