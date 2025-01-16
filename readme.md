#Socket Communication Script by Patrik Faust
### Erstellen virtual environment ###
python3 -m venv env
### Linux ###
source env/Scripts/activate 
source env/bin/activate #Verzeichnis variiert nach Python Version
### Windows ### 
cd env/Scripts/
activate.bat 
### Module installieren ###
pip install -r requirements.txt
### Server starten ###
python3 server.py
### Client starten ###
python3 client.py
### Beenden ###
Um den Server abzuschalten "shutdown" an den Server senden
