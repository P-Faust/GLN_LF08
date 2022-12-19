#!./env/bin/python
import computer, socket, psutil, platform, cpuinfo

#Erstelle Klasse Client und erbe von Klasse Computer
class Client(computer.Computer):
    __remoteIP = ""
    __remotePort = 0
    #Legt die Werte für sen Socket fest
    def createSocket(self, remoteIP, remotePort):
        try:
            self.__remoteIP = remoteIP
            self.__remotePort = remotePort
            self.web_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print(f"Remote-IP: {myClient.__remoteIP}\nRemote-Port: {myClient.__remotePort}")
        except Exception as error:
            print(f"Fehler bei erstellung des Sockets: {error}]")

    #Verbindet sich mit dem Socket und sendet Daten
    def sendData(self):
        try:
            usr_msg = ""
            self.web_socket.connect((self.__remoteIP, self.__remotePort))
            print(f"\nErfolgreich verbunden mit {self.__remoteIP}:{self.__remotePort}")
            while usr_msg != "shutdown":
                usr_msg = input("Zu sendenden Text angeben:\n")
                self.web_socket.sendall(usr_msg.encode())
                data = self.web_socket.recv(1024)
                print(data.decode())
                if(usr_msg == "shutdown"):    
                    print("Server wird Heruntergefahren")
                    print("Vielen dank für die Nutzung des 1337LeetSockets")
                    self.web_socket.close()
                elif(usr_msg == "exit"):
                    print("Vielen dank für die Nutzung des 1337LeetSockets")
                    self.web_socket.close()
                    break
        except Exception as error:
            print(f"Fehler bei Serverausführung: {error}]")

myClient = Client("750W", cpuinfo.get_cpu_info()['brand_raw'], psutil.cpu_freq().max, psutil.virtual_memory().total, platform.system(), socket.gethostbyname(socket.gethostname()))
myClient.getInfo()
myClient.createSocket("127.0.0.1", 1337)
try:
    myClient.sendData()
except:
    print("Server nicht Erreichbar.\nBitte stelle sicher, dass server.py ausgeführt wurde")
