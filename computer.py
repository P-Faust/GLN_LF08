import platform, psutil, socket, cpuinfo

class Computer():
    
    powerSupply = ""
    _cpu = ""
    _cpuSpeed = 0.0
    _ram = 0
    _os = ""
    _ip = ""

    def __init__(self, power_supply, cpu, cpu_speed,ram,os,ip):
        self.powerSupply = power_supply
        self._cpu = cpu
        self._cpuSpeed = str(cpu_speed) + " MHz"
        self._ram = str(ram)[:2] + " GB" 
        self._os = os
        self._ip = ip
        
    def getInfo(self):
        info_list = [self._cpu, self._cpuSpeed,self._ram,self._os, self._ip]
        for x in range(len(info_list)):
            if x == 0:
                print(f"Cpu: {info_list[x]}")
            elif x == 1:
                print(f"Cpu Taktrate: {info_list[x]}")
            elif x == 2:
                print(f"Memory: {info_list[x]}")
            elif x == 3:
                print(f"Betriebssystem: {info_list[x]}")
            elif x == 4:
                print(f"IP: {info_list[x]}")
            else:
                break
