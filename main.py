import subprocess

data=subprocess.check_output(['netsh','wlan','show','profiles']).decode('utf-8').split('\n')
wifis=[line.split(':')[1][1:-1]for line in data  if "Perfil de todos los usuarios" in line]

print('NOMBRE DE LAS REDES WIFI : ',wifis)

for wifi in wifis:
    resultado=subprocess.check_output(['netsh','wlan','show','profile',wifi,'key=clear']).decode('ISO-8859-1').split('\n')
    resultado=[line.split(':')[1][1:-1] for line in resultado if "Contenido de la clave" in line]
    try:
        print(f'Nombre del wifi :{wifi},Password del wifi : {resultado[0]}')
    except IndexError:
        print(f'Nombre:{wifi},Password: nose lo siento ')
        

