import ftplib
import os
import json
import time


class ftp_client:

    totalSize = 0
    currentSize = 0
    password = 0
###################################################################################################
#                                   Constructor
###################################################################################################
    # ------------------- Inicia la conexion FTP de tipo cliente -----------------------

    def __init__(self, FTP_HOST, FTP_USER, FTP_PASS):
        self.FTP_HOST = FTP_HOST
        self.FTP_USER = FTP_USER
        self.FTP_PASS = FTP_PASS
        self.ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
        self.downloadSize()

        data = self.getJson(self.FTP_USER)
        self.currentSize = int(data['currentSize'])
        self.totalSize = int(data['totalSize'])
        self.password = data['password']

###################################################################################################
#                                   Archivos tipo Json
###################################################################################################
    # ---------------------- Retorna la direccion del tipo Json ------------------------
    def getPath(self, user):
        path = user+'.json'
        return path

    # --------------- Descarga el archivo de tipo Json en el contructor -----------------
    def downloadSize(self):
        with open(self.FTP_USER+'.json', "wb") as file:
            self.ftp.retrbinary("RETR " + self.FTP_USER+'.json', file.write)

    def downloadGUJ(self):
        c = 'globalUserJson.json/../'
        with open(self.FTP_USER+'.json', "wb") as file:
            self.ftp.retrbinary("RETR " + self.FTP_USER+'.json', file.write)

    # -------------------------- Elimina un archivo tipo Json ---------------------------
    def deleteJson(self):
        os.remove('./'+self.FTP_USER+'.json')

    # --------- Actualiza los valor del Size cuando sube algo en el Json ----------------
    def uploadJson(self):

        data = self.getJson(self.FTP_USER)

        data['currentSize'] = str(self.currentSize)
        data['totalSize'] = str(self.totalSize)
        data['password'] = str(self.password)

        with open(self.FTP_USER+'.json', 'w')as outfile:
            json.dump(data, outfile)

        with open(self.FTP_USER+'.json', "rb") as file:  # Sube el archivo de tipo Json
            self.ftp.storbinary('STOR '+'/../'+self.FTP_USER+'.json', file)
            # self.ftp.dir()

        self.deleteJson()

    # ----------------- Retorna un diccionario del archivo de tipo Json ---------------------
    def getJson(self, user):

        f = open(self.getPath(user))  # Abrimos el Json
        data = json.load(f)  # Cambiamos  de Json a diccionario

        return data

    def createCPJson(self, passwd):
        jsonUser = {
            "password": str(passwd)
        }

        with open('changePassword.json', 'w')as outfile:
            json.dump(jsonUser, outfile)

        with open('changePassword.json', "rb") as file:  # Sube el archivo de tipo Json
            self.ftp.storbinary('STOR '+'/../'+'changePassword.json', file)

#######################################################################################################

    # -------- Compara el tamaño del archivo con el tamaño disponible de la persona ---------
    def compareSize(self, filename):
        print(self.totalSize - self.currentSize)
        print(os.path.getsize('./'+filename))
        if ((self.totalSize - self.currentSize) >= os.path.getsize('./'+filename)):
            return True
        else:
            return False

    # ------------------------- Cambiar la contraseña del user -----------------------------
    def changePassword(self, psw):

        if (len(psw) > 4 and len(psw) < 15):
            self.password = psw
            self.uploadJson()
            self.createCPJson(psw)
        else:
            print("Password invalida")

    # ---------------------------------- Sube un archivo ------------------------------------
    def uploadFile(self, filename):

        if (self.compareSize(filename)):
            with open(filename, "rb") as file:
                self.ftp.storbinary('STOR '+filename, file)

            self.currentSize = self.currentSize + \
                os.path.getsize('./'+filename)
            self.uploadJson()
        else:
            print('No hay espacio suficiente para este archivo')

    # ------------------------------ Descarga un archivo -----------------------------
    def downloadFile(self, filename):

        with open(filename, "wb") as file:
            self.ftp.retrbinary("RETR " + filename, file.write)

    # --------------------------- Elimina un archivo ----------------------------------
    def deleteFile(self, filename):

        self.currentSize = self.currentSize - os.path.getsize('./'+filename)
        self.uploadJson()

        self.ftp.delete(filename)

     # --------------------------- Elimina una carpeta  ----------------------------------

    def deleteFolder(self, folderName):

        self.ftp.rmd(folderName)

        # -------------- Se mueve de directorio a la carpeta seleccionada -------------------

    def moveToFolder(self, folderName):
        self.ftp.cwd(folderName)

    # --------------------------- Regresa al directorio anterior ------------------------
    def moveBackFromFolder(self):
        self.ftp.cwd('../')

    # ----------------------------- Crea un nuevo directorio ----------------------------
    def createFolder(self, namefolder):
        self.ftp.mkd(namefolder)

    # ------------------------------ Elimina un directorio ------------------------------
    def deleteFolder(self, namefolder):
        self.ftp.rmd(namefolder)


###################################################################################################
#                                   Main
###################################################################################################
if __name__ == '__main__':
    client = ftp_client("192.168.1.100", "marcos", "password")
    client.moveBackFromFolder
    client.downloadFile('globalUserJson.json')

    # client.uploadFile('prueba.ts')

    time.sleep(1)
    # client.changePassword('password')

    # client.changePassword('arrivederci')


# client.uploadFile('prueba.ts')
# client.createFolder('Carpeta')
# client.moveToFolder('Carpeta')
# client.uploadFile('prueba.ts')

# client.ftp.mkd('carpeta')

# print(client.ftp.nlst())
# client.ftp.cwd('carpeta')
# print(client.ftp.nlst())
# client.ftp.cwd('../')
# print(client.ftp.nlst())

# client.uploadFile('prueba.ts')
# client.deleteFolder('churro')

# self.ftp.cwd("Directorio nuevo")


'''


ftp.dir(argumento[, ...])
Genere una lista de directorios como devuelve el comando LIST, imprimiéndola en la salida estándar. 
El argumento opcional es un directorio para enumerar (el valor predeterminado es el directorio del servidor actual). 
Se pueden utilizar varios argumentos para pasar opciones no estándar al comando LIST. 

ftp.nlst() # lista de los directorios de la carpeta

ftp.cwd(pathname) # Establezca el directorio actual en el servidor.

ftp.mkd(pathname) # Cree un nuevo directorio en el servidor.

ftp.pwd() # Devuelve la ruta de acceso del directorio actual en el servidor.

ftp.rmd(dirname) # Quite el directorio denominado dirname en el servidor.

'''
