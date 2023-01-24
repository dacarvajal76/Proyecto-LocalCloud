import threading
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from gettinIp import ipAddress
from tkinter import messagebox
import os
import time
import json


class ftp_server(threading.Thread):

    def __init__(self):
        super(ftp_server, self).__init__(name='ftp_server')
        self.authorizer = DummyAuthorizer()
        # self.authorizer.add_user('admin', 'password', '.', perm='elradfmwM')
        # self.authorizer.add_user('admin', 'password', '.')

    def run(self):
        self.handler = FTPHandler
        self.handler.authorizer = self.authorizer

        myIp = ipAddress()
       # print(myIp.getIpAddres)
       # ip = myIp.getIpAddres()

        self.address = (myIp.getIpAddres(), 21)

        self.server = FTPServer(self.address, self.handler)

        self.server.serve_forever()

    def getPath(self, user):
        path = './'+user+'/'+user+'.json'
        return path

    def getCPJson(self, user):
        path = './'+user+'/'+'changePassword.json'
        return path


#################################################################################################

    '''
    def saludar2(self):
        while True:
            print('hola2')
            '''

#################################################################################################

    def getJson(self, user):

        f = open(self.getPath(user))  # Abrimos el Json
        data = json.load(f)  # Cambiamos  de Json a diccionario

        return data

    def changeSize(self, user, val):

        data = self.getJson(user)
        # Modificamos el espacio con el nuevo valor
        data['totalSize'] = str(val)

        with open(self.getPath(user), 'w')as outfile:
            json.dump(data, outfile)

    def updateSize(self, user, val):

        data = self.getJson(user)
        # Modificamos el espacio con el nuevo valor
        data['currentSize'] = str(val)

        with open(self.getPath(user), 'w')as outfile:
            json.dump(data, outfile)

    def add_user(self, user, passwd, privi):

        if (os.path.exists(os.path.join(os.getcwd(), user))):
            print('Ya existe un usuario con ese nombre')
        else:
            os.makedirs(os.path.join(os.getcwd(), user))
            path = './'+user+'/'+user+'.json'

            jsonUser = {
                "user": str(user),
                "totalSize": str(2000000),
                "currentSize": str(0),
                "password": str(passwd)
            }

            with open(self.getPath(user), 'w')as outfile:
                json.dump(jsonUser, outfile)

        self.authorizer.add_user(str(user), str(
            passwd), str(user), perm=str(privi))

    def printUsers(self):

        print(self.authorizer.user_table['marcos']['pwd'])
        self.authorizer.user_table['marcos']['pwd'] = 'perro'
        print(self.authorizer.user_table['marcos']['pwd'])

    def changePassword(self, key):
        print('hello')
        f = open(self.getCPJson(key))
        data = json.load(f)

        self.authorizer.user_table[key]['pwd'] = data['password']
        file = open(self.getCPJson(key), 'w')
        json.dump(data, file)
        file.close()
        # with open(self.getCPJson(key), 'w') as outfile:  # cerramos el Json
        #    json.dump(data, outfile)
        os.remove(self.getCPJson(key))
        self.retrieveUserInJson()
        time.sleep(1)

    def checkPassword(self):
        while True:
            time.sleep(5)
            for key in self.authorizer.user_table.keys():
                # si el usuario cambio la contraseña
                try:
                    if (os.path.exists(self.getCPJson(key))):
                        self.changePassword(key)
                except:
                    print('')

    def retrieveUserInJson(self):

        robert = ''

        for key in self.authorizer.user_table.keys():
            f = open('./'+key+'/'+key+'.json')
            data = json.load(f)
            robert = robert + str(data) + ','
            self.writeGlobalUserJson(data)

        robert = '['+robert[:-1]+']'
        robert = robert.replace("'", '"')

        lewandoski = json.loads(robert)

        self.writeGlobalUserJson(lewandoski)

        # data = "[" + data.replace("}", "},", data.count("}")-1) + "]"

    def writeGlobalUserJson(self, data):

        with open('globalUserJson.json', 'w')as outfile:
            # data = "[" + data
            # data = data + "]"
            json.dump(data, outfile)

    def reformatingJson(self):
        f = open('globalUserJson.json')
        data = json.load(f)
        print('aqui?')
        # data = "[\n" + data
        # data = data + "\n]"

        with open('globalUserJson.json', 'w')as outfile:
            json.dump(data, outfile)

    def changePasswordYes(self):
        self.authorizer.user_table['marcos']['pwd'] = 'contrasena'

    def changeTotalSize(self, user, newSize):
        data = self.getJson(user)
        data['totalSize'] = str(newSize)
        with open('./'+user+'/'+user+'.json', 'w')as outfile:
            json.dump(data, outfile)
            outfile.write('\n')


if __name__ == '__main__':
    server = ftp_server()

    server.start()

    time.sleep(2)

    server.add_user('marcos', 'password', 'elradfmwMT')
    server.add_user('jeff', 'password', 'elradfmwMT')

    time.sleep(1)

    server.retrieveUserInJson()
    # server.reformatingJson()

    hilo1 = threading.Thread(target=server.checkPassword)
    hilo1.start()


# os.mkdir("NuevaCarpetita")   Generar nuevas carpetas
'''
{'admin': 
    {'pwd': 'password', 
     'home': 'C:\\Users\\Daniel\\Documents\\Scripts\\Python\\ServerApp', 
     'perm': 'elr', '
     operms': {}, 
     'msg_login': 'Login successful.', 
     'msg_quit': 'Goodbye.'}, 
'marcos': {'pwd': 'password', 
     'home': 'C:\\Users\\Daniel\\Documents\\Scripts\\Python\\ServerApp\\marcos', 
     'perm': 'elradfmwMT', 
     'operms': {}, 
     'msg_login': 'Login successful.', 
     'msg_quit': 'Goodbye.'}
     }

import threading #libreria

def ejecutar():
    print(f'{threading.current_thread().name} te saluda')

# creamos un temporizador
temporizador = threading.Timer(5, function=ejecutar)  # creamos el hilo con temporizador
temporizador.start()  # el hilo empezará cuando pasen 5 segundos




https://www.codigopiton.com/como-usar-hilos-o-threads-en-python/#:~:text=Los%20hilos%20en%20Python%20se%20crean%20instanciando%20la,otro%20hilo%20se%20invoca%20a%20su%20m%C3%A9todo%20join.


https://www.youtube.com/watch?v=JfpQ1XjeQEE&ab_channel=DeProgramaci%C3%B3nyTecnolog%C3%ADa


    # messagebox.showinfo("Error tal", "Mensaje tal")
'''
