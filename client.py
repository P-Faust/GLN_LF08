import computer, socket, psutil, platform, cpuinfo
class Client(computer.Computer):
    __remoteIP = ""
    __remotePort = 0

    def createSocket(self, remoteIP, remotePort):
        self.__remoteIP = remoteIP
        self.__remotePort = remotePort
        print(f"Remote-IP: {myClient.__remoteIP}\nRemote-Port: {myClient.__remotePort}")
    
    def sendData(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            usr_msg = ""
            s.connect((self.__remoteIP, self.__remotePort))
            print(f"\nErfolgreich verbunden mit {self.__remoteIP}:{self.__remotePort}")
            while usr_msg != "shutdown":
                usr_msg = input("Zu sendenden Text angeben:\n")
                s.sendall(usr_msg.encode())
                data = s.recv(1024)
                print(data.decode())
                if(usr_msg == "shutdown"):    
                    print("Server wird Heruntergefahren")
                    print("Vielen dank für die Nutzung des 1337LeetSockets")
                    s.close()
                elif(usr_msg == "exit"):
                    print("Vielen dank für die Nutzung des 1337LeetSockets")
                    s.close()
                    break

        

myClient = Client("750W", cpuinfo.get_cpu_info()['brand_raw'], psutil.cpu_freq().max, psutil.virtual_memory().total, platform.system(), socket.gethostbyname(socket.gethostname()))
myClient.getInfo()
myClient.createSocket("127.0.0.1", 6420)
try:
    myClient.sendData()
except:
    print("Server nicht Erreichbar.\nBitte stelle sicher, dass server.py ausgeführt wurde")
