import json
import os
import tkinter
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from FTP_Client import ftp_client


class Login():
    #  ----------- Centramos la Ventana en el medio------------------------------
    def centrar(self, window):
        pwidth = round(window.winfo_screenwidth()/2 - 900/2)
        pheight = round(window.winfo_screenheight()/2 - 500/2)
        window.geometry(str(900)+"x"+str(500)+"+"+str(pwidth)+"+"+str(pheight))

    def getJson(self):
        f = open('globalUserJson.json')  # Abrimos el Json
        data = json.load(f)  # Cambiamos  de Json a diccionario
        return data

    def check_login(self, username, password, direccion):
        try:
            ftpClient = ftp_client(direccion, username, password)
            self.window.destroy()
            Menu(ftpClient)

        except:
            messagebox.showwarning(
                message="Credenciales incorrectas", title="Alerta!")

    def __init__(self):
        self.window = Tk()  # Creo la ventana
        self.window.geometry("900x500")  # Doy dimensiones de la ventana
        # Ventana de tamaño fija (No tiene maximizar ni minimizar tamaño)
        self.window.resizable(0, 0)
        self.window.title("login")  # Titulo de la ventana
        self.centrar(self.window)

        #  ----------------------- Agregamos el fondo  ------------------------------
        img = PhotoImage(file="Sprites/Login.png")
        lbl = Label(self.window, image=img).place(x=0, y=0)

        #  --------------------------------------------------------------------------
        #  ------------------------- Boton de siguiente -----------------------------
        img2 = PhotoImage(file="Sprites/next.png")
        btn1 = tkinter.Button(self.window, text="", bg='#14405D',
                              image=img2, borderwidth=0, command=lambda: self.check_login(username.get(), password.get(), direccion.get()))
        btn1.pack()
        btn1.place(x=358, y=355, height=45, width=45)

        #  --------------------------------------------------------------------------
        #  -------------------------   Cajas de texto   -----------------------------

        username = tkinter.Entry(
            self.window, font="Helvetica 14", borderwidth=0)
        username.pack()
        username.place(x=188, y=154, height=30, width=200)

        password = tkinter.Entry(
            self.window, font="Helvetica 14", borderwidth=0)
        password.pack()
        password.place(x=188, y=223, height=30, width=200)

        direccion = tkinter.Entry(
            self.window, font="Helvetica 14", borderwidth=0)
        direccion.pack()
        direccion.place(x=188, y=292, height=30, width=200)

        #  --------------------------------------------------------------------------
        self.window.mainloop()  # Muesta la ventana

########################################################################################################
########################################################################################################


class Menu():
    #  ----------- Centramos la Ventana en el medio------------------------------
    def centrar(self, window):
        pwidth = round(window.winfo_screenwidth()/2 - 900/2)
        pheight = round(window.winfo_screenheight()/2 - 500/2)
        window.geometry(str(900)+"x"+str(500)+"+"+str(pwidth)+"+"+str(pheight))

    def close(self, A):
        self.window.destroy()
        A.ftp.quit()
        B = Login()

    def up(self, window, A):
        window.destroy()
        UploadFile(A)

    def chagepass(self, window, A):
        window.destroy()
        ChangePassword(A)

    def down(self, window, A):
        window.destroy()
        DownloadFile(A)

    def share(self, window, A):
        window.destroy()
        ShareFile(A)

    def viewfile(self, window, A):
        window.destroy()
        ViewFolder(A)

    def __init__(self, A):
        self.window = Tk()  # Creo la ventana
        self.window.geometry("900x500")  # Doy dimensiones de la ventana
        # Ventana de tamaño fija (No tiene maximizar ni minimizar tamaño)
        self.window.resizable(0, 0)
        self.window.title("Menu")  # Titulo de la ventana
        self.centrar(self.window)

        #  ----------------------- Agregamos el fondo  ------------------------------
        img = PhotoImage(file="Sprites/Menu.png")
        lbl = Label(self.window, image=img).place(x=0, y=0)

        lbl2 = Label(self.window, text=A.FTP_USER, bg='#14405D',
                     fg='White', font="Black 16").place(x=270, y=60)

        #  --------------------------------------------------------------------------
        #  -------------------------      Botonnes      -----------------------------

        btns_verArchivos = tkinter.Button(
            self.window, text="Ver Archivos", borderwidth=0, command=lambda: self.viewfile(self.window, A))
        btns_verArchivos.pack()
        btns_verArchivos.place(x=280, y=355, height=35, width=250)

        btns_subirArchivos = tkinter.Button(
            self.window, text="Subir Archivos", borderwidth=0, command=lambda: self.up(self.window, A))
        btns_subirArchivos.pack()
        btns_subirArchivos.place(x=280, y=175, height=35, width=250)

        btns_bajarArchivos = tkinter.Button(
            self.window, text="Bajar Archivos", borderwidth=0, command=lambda: self.down(self.window, A))
        btns_bajarArchivos.pack()
        btns_bajarArchivos.place(x=280, y=235, height=35, width=250)

        btns_compartirArchivos = tkinter.Button(
            self.window, text="Compartir Archivos",  borderwidth=0, command=lambda: self.share(self.window, A))
        btns_compartirArchivos.pack()
        btns_compartirArchivos.place(x=280, y=295, height=35, width=250)

        btns_cambiarContra = tkinter.Button(
            self.window, text="Cambiar contraseña", bg='#14405D', fg='White', font="Black 11", borderwidth=0, command=lambda: self.chagepass(self.window, A))
        btns_cambiarContra.pack()
        btns_cambiarContra.place(x=270, y=97, height=35, width=135)

        btns_cerrarSesion = tkinter.Button(
            self.window, text="Cerrar sesión", font="Black 16", borderwidth=0, command=lambda: self.close(A))
        btns_cerrarSesion.pack()
        btns_cerrarSesion.place(x=655, y=380, height=40, width=170)

        #  --------------------------------------------------------------------------

        #  --------------------------------------------------------------------------
        self.window.mainloop()

########################################################################################################
########################################################################################################


class DownloadFile:
    #  ----------- Centramos la Ventana en el medio------------------------------
    def centrar(self, window):
        pwidth = round(window.winfo_screenwidth()/2 - 900/2)
        pheight = round(window.winfo_screenheight()/2 - 500/2)
        window.geometry(str(900)+"x"+str(500)+"+"+str(pwidth)+"+"+str(pheight))
    #  --------------------------------------------------------------------------
    #  ------------------- Opciones de los Bonotes ------------------------------

    def menu(self, A):
        self.window.destroy()
        A.ftp.cwd('../')
        Menu(A)

    def create(self, A):
        self.window.destroy()
        DownloadFile(A)

    def llenado_table(self, table, A):
        for A in A.ftp.nlst():
            table.insert("", END, text=A)

    def show_selection(self, t1, A, dato):
        try:
            item1 = t1.selection()[0]
        except IndexError:
            messagebox.showwarning(
                message="Debe seleccionar un elemento.",
                title="No hay selección"
            )
        else:
            text = t1.item(item1, option="text")
            messagebox.showinfo(message=text, title="Selección")
            if (dato == 1):
                A.downloadFile(text)
            else:
                try:
                    A.ftp.cwd(text)
                    self.window.destroy()
                    DownloadFile(A)
                except:
                    messagebox.showinfo(
                        message='No selecciono una carpeta', title="Selección")

    #  --------------------------------------------------------------------------
    #  --------------------------------------------------------------------------

    def __init__(self, A):
        self.window = Tk()  # Creo la ventana
        self.window.geometry("900x500")  # Doy dimensiones de la ventana
        # Ventana de tamaño fija (No tiene maximizar ni minimizar tamaño)
        self.window.resizable(0, 0)
        self.window.title("Login")  # Titulo de la ventana
        self.centrar(self.window)
        #  ----------------------- Agregamos el fondo  ------------------------------
        img = PhotoImage(file="Sprites/DownFile.png")
        lbl = Label(self.window, image=img).place(x=0, y=0)
        lbl2 = Label(self.window, text=A.FTP_USER, bg='#14405D',
                     fg='White', font="Black 12").place(x=270, y=90)

        #  ----------------------- Agregamos la Tabla  ------------------------------

        files = ttk.Treeview(self.window, height=7)
        files.column("#0", width=200, anchor=CENTER)
        files.heading("#0", text="Archivos", anchor=CENTER)
        files.pack()
        files.place(x=280, y=150)
        self.llenado_table(files, A)

        #  --------------------------------------------------------------------------
        #  ---------------------------- Bonotes -------------------------------------
        img2 = PhotoImage(file="Sprites/back.png")
        btn1 = tkinter.Button(self.window, text="", bg='#14405D',
                              image=img2, borderwidth=0, command=lambda: self.menu(A))
        btn1.pack()
        btn1.place(x=410, y=390, height=45, width=45)

        btn_bajar = tkinter.Button(self.window, text="Descargar",
                                   borderwidth=0, command=lambda: self.show_selection(files, A, 1))
        btn_bajar.pack()
        btn_bajar.place(x=145, y=380, height=40, width=125)

        btn_mover = tkinter.Button(self.window, text="Mover",
                                   borderwidth=0, command=lambda: self.show_selection(files, A, 2))
        btn_mover.pack()
        btn_mover.place(x=155, y=220, height=40, width=90)

        #  --------------------------------------------------------------------------

        self.window.mainloop()  # Muesta la ventana

########################################################################################################
########################################################################################################


class UploadFile:
    #  ----------- Centramos la Ventana en el medio------------------------------
    def centrar(self, window):
        pwidth = round(window.winfo_screenwidth()/2 - 900/2)
        pheight = round(window.winfo_screenheight()/2 - 500/2)
        window.geometry(str(900)+"x"+str(500)+"+"+str(pwidth)+"+"+str(pheight))

    #  --------------------------------------------------------------------------
    #  ------------------- Opciones de los Bonotes ------------------------------
    def menu(self, A):
        self.window.destroy()
        Menu(A)

    def show_selection(self, t1, A):
        try:
            item1 = t1.selection()[0]
        except IndexError:
            messagebox.showwarning(
                message="Debe seleccionar un elemento.",
                title="No hay selección"
            )
        else:
            text = t1.item(item1, option="text")
            messagebox.showinfo(message=text, title="Selección")

            A.uploadFile(text)

    def llenado_table(self, table):
        for A in os.listdir():
            if (('.' in A[:-3]) or ('.' in A[:-4]) or ('.' in A[:-2])):  # si es archivo
                table.insert("", END, text=A)

    #  --------------------------------------------------------------------------
    #  --------------------------------------------------------------------------

    def __init__(self, A):
        self.window = Tk()  # Creo la ventana
        self.window.geometry("900x500")  # Doy dimensiones de la ventana
        # Ventana de tamaño fija (No tiene maximizar ni minimizar tamaño)
        self.window.resizable(0, 0)
        self.window.title("Subir Archivo")  # Titulo de la ventana
        self.centrar(self.window)
        #  ----------------------- Agregamos el fondo  ------------------------------
        img = PhotoImage(file="Sprites/UpFile.png")
        lbl = Label(self.window, image=img).place(x=0, y=0)
        lbl2 = Label(self.window, text=A.FTP_USER, bg='#14405D',
                     fg='White', font="Black 12").place(x=285, y=90)
        #  ----------------------- Agregamos la Tabla  ------------------------------

        files = ttk.Treeview(self.window, height=8)
        files.column("#0", width=200, anchor=CENTER)
        files.heading("#0", text="Archivos", anchor=CENTER)
        files.pack()
        files.place(x=270, y=150)
        self.llenado_table(files)

        #  --------------------------------------------------------------------------
        #  ---------------------------- Bonotes -------------------------------------
        img2 = PhotoImage(file="Sprites/back.png")
        btn_volver = tkinter.Button(self.window, text="", bg='#14405D',
                                    image=img2, borderwidth=0, command=lambda: self.menu(A))
        btn_volver.pack()
        btn_volver.place(x=385, y=355, height=45, width=45)

        btn_subir = tkinter.Button(self.window, text="Subir",
                                   borderwidth=0, command=lambda: self.show_selection(files, A))
        btn_subir.pack()
        btn_subir.place(x=150, y=355, height=45, width=130)

        #  --------------------------------------------------------------------------

        self.window.mainloop()  # Muesta la ventana

########################################################################################################
########################################################################################################


class ShareFile:
    #  ----------- Centramos la Ventana en el medio------------------------------
    def centrar(self, window):
        pwidth = round(self.window.winfo_screenwidth()/2 - 900/2)
        pheight = round(self.window.winfo_screenheight()/2 - 500/2)
        window.geometry(str(900)+"x"+str(500)+"+"+str(pwidth)+"+"+str(pheight))

    def menu(self, A):
        self.window.destroy()
        Menu(A)
    #  --------------------------------------------------------------------------
    #  ------------------- Opciones de los Bonotes ------------------------------

    def show_selection(self, t1, t2):
        try:
            item1 = t1.selection()[0]
            item2 = t2.selection()[0]
        except IndexError:
            messagebox.showwarning(
                message="Debe seleccionar un elemento.",
                title="No hay selección"
            )
        else:
            text = t1.item(item1, option="text") + ' y ' + \
                t2.item(item2, option="text")
            messagebox.showinfo(message=text, title="Selección")

    #  --------------------------------------------------------------------------
    #  --------------------------------------------------------------------------
    def __init__(self, A):
        self.window = Tk()
        self.window.geometry("900x500")
        self.window.resizable(0, 0)
        self.window.title("Compartir Archivo")  # Titulo de la ventana
        self.centrar(self.window)
        #  ----------------------- Agregamos el fondo  ------------------------------
        img = PhotoImage(file="Sprites/ShareFile.png")
        lbl = Label(self.window, image=img).place(x=0, y=0)
        lbl2 = Label(self.window, text=A.FTP_USER, bg='#14405D',
                     fg='White', font="Black 12").place(x=270, y=90)
        #  ----------------------- Agregamos la Tabla  ------------------------------

        users = ttk.Treeview(self.window, height=10)
        users.column("#0", width=200, anchor=CENTER)
        users.heading("#0", text="Usuario", anchor=CENTER)
        users.pack()
        users.place(x=100, y=150)

        file = ttk.Treeview(self.window, height=10)
        file.column("#0", width=200, anchor=CENTER)
        file.heading("#0", text="Usuario", anchor=CENTER)
        file.pack()
        file.place(x=250, y=150)

        button = ttk.Button(text="Mostrar selección",
                            command=lambda: self.show_selection(users, file))
        button.pack()

        #  ---------------------------- Bonotes -------------------------------------
        img2 = PhotoImage(file="Sprites/back.png")
        btn1 = tkinter.Button(self.window, text="", bg='#14405D',
                              image=img2, borderwidth=0, command=lambda: self.menu(A))
        btn1.pack()
        btn1.place(x=358, y=355, height=45, width=45)
        #  --------------------------------------------------------------------------

        #  --------------------------------------------------------------------------
        self.window.mainloop()  # Muesta la ventana

########################################################################################################
########################################################################################################


class ChangePassword:
    #  ----------- Centramos la Ventana en el medio------------------------------
    def centrar(self, window):
        pwidth = round(self.window.winfo_screenwidth()/2 - 900/2)
        pheight = round(self.window.winfo_screenheight()/2 - 500/2)
        window.geometry(str(900)+"x"+str(500)+"+"+str(pwidth)+"+"+str(pheight))

    def menu(self, A):
        self.window.destroy()
        Menu(A)

    #  --------------------------------------------------------------------------
    #  ------------------- Opciones de los Bonotes ------------------------------

    def change(self, A, oldPassword, newPassword):
        if A.FTP_PASS == oldPassword:
            A.changePassword(newPassword)
            self.window.destroy()
            Login()

        #  --------------------------------------------------------------------------
        #  --------------------------------------------------------------------------

    def __init__(self, A):
        self.window = Tk()  # Creo la ventana
        self.window.geometry("900x500")  # Doy dimensiones de la ventana
        # Ventana de tamaño fija (No tiene maximizar ni minimizar tamaño)
        self.window.resizable(0, 0)
        self.window.title("Cambiar Contraseña")  # Titulo de la ventana
        self.centrar(self.window)
        #  ----------------------- Agregamos el fondo  ------------------------------
        img = PhotoImage(file="Sprites/ChagePassword.png")
        lbl = Label(self.window, image=img).place(x=0, y=0)
        lbl2 = Label(self.window, text=A.FTP_USER, bg='#14405D',
                     fg='White', font="Black 12").place(x=270, y=90)
        #  --------------------------------------------------------------------------
        #  ---------------------------- Bonotes -------------------------------------
        img2 = PhotoImage(file="Sprites/back.png")
        btn1 = tkinter.Button(self.window, text="", bg='#14405D',
                              image=img2, borderwidth=0, command=lambda: self.menu(A))
        btn1.pack()
        btn1.place(x=358, y=355, height=45, width=45)

        btn1 = tkinter.Button(self.window, text="Cambiar",
                              borderwidth=0, command=lambda: self.change(A, passactual.get(), newpass.get()))
        btn1.pack()
        btn1.place(x=130, y=370, height=45, width=140)
        #  --------------------------------------------------------------------------
        passactual = tkinter.Entry(
            self.window, font="Helvetica 14", borderwidth=0)
        passactual.pack()
        passactual.place(x=110, y=220, height=30, width=140)

        newpass = tkinter.Entry(
            self.window, font="Helvetica 14", borderwidth=0)
        newpass.pack()
        newpass.place(x=340, y=220, height=30, width=140)

        self.window.mainloop()  # Muesta la ventana

########################################################################################################
########################################################################################################


class ChageFile:
    #  ----------- Centramos la Ventana en el medio------------------------------
    def centrar(self, window):
        pwidth = round(self.window.winfo_screenwidth()/2 - 900/2)
        pheight = round(self.window.winfo_screenheight()/2 - 500/2)
        window.geometry(str(900)+"x"+str(500)+"+"+str(pwidth)+"+"+str(pheight))

    def menu(self, A):
        self.window.destroy()
        Menu(A)
    #  --------------------------------------------------------------------------
    #  ------------------- Opciones de los Bonotes ------------------------------

    #  --------------------------------------------------------------------------
    #  --------------------------------------------------------------------------

    def __init__(self, A):
        self.window = Tk()  # Creo la ventana
        self.window.geometry("900x500")  # Doy dimensiones de la ventana
        # Ventana de tamaño fija (No tiene maximizar ni minimizar tamaño)
        self.window.resizable(0, 0)
        self.window.title("Cambiar Archivo")  # Titulo de la ventana
        self.centrar(self.window)
        #  ----------------------- Agregamos el fondo  ------------------------------
        img = PhotoImage(file="Sprites/ChageFile.png")
        lbl = Label(self.window, image=img).place(x=0, y=0)
        #  --------------------------------------------------------------------------
        #  ---------------------------- Bonotes -------------------------------------
        img2 = PhotoImage(file="Sprites/back.png")
        btn1 = tkinter.Button(self.window, text="", bg='#14405D',
                              image=img2, borderwidth=0, command=lambda: self.menu(A))
        btn1.pack()
        btn1.place(x=358, y=355, height=45, width=45)
        #  --------------------------------------------------------------------------

        self.window.mainloop()  # Muesta la ventana

########################################################################################################
########################################################################################################


class CreateFolder:
    #  ----------- Centramos la Ventana en el medio------------------------------
    def centrar(self, window):
        pwidth = round(self.window.winfo_screenwidth()/2 - 900/2)
        pheight = round(self.window.winfo_screenheight()/2 - 500/2)
        window.geometry(str(900)+"x"+str(500)+"+"+str(pwidth)+"+"+str(pheight))

    def menu(self, A):
        self.window.destroy()
        Menu(A)

    def create(self, A, texto):
        A.ftp.mkd(texto)
        messagebox.showinfo(message='Carpeta creada', title="Selección")

    #  --------------------------------------------------------------------------
    #  ------------------- Opciones de los Bonotes ------------------------------

    #  --------------------------------------------------------------------------
    #  --------------------------------------------------------------------------

    def __init__(self, A):
        self.window = Tk()  # Creo la ventana
        self.window.geometry("900x500")  # Doy dimensiones de la ventana
        # Ventana de tamaño fija (No tiene maximizar ni minimizar tamaño)
        self.window.resizable(0, 0)
        self.window.title("Crear Carpeta")  # Titulo de la ventana
        self.centrar(self.window)
        #  ----------------------- Agregamos el fondo  ------------------------------
        img = PhotoImage(file="Sprites/CreateFolder.png")
        lbl = Label(self.window, image=img).place(x=0, y=0)
        lbl2 = Label(self.window, text=A.FTP_USER, bg='#14405D',
                     fg='White', font="Black 12").place(x=285, y=90)
        #  --------------------------------------------------------------------------
        #  ---------------------------- Bonotes -------------------------------------
        img2 = PhotoImage(file="Sprites/back.png")
        btn1 = tkinter.Button(self.window, text="", bg='#14405D',
                              image=img2, borderwidth=0, command=lambda: self.menu(A))
        btn1.pack()
        btn1.place(x=358, y=355, height=45, width=45)

        btn_crear = tkinter.Button(self.window, text="Crear Carpeta",
                                   borderwidth=0, command=lambda: self.create(A, name.get()))
        btn_crear.pack()
        btn_crear.place(x=150, y=380, height=45, width=130)
        #  --------------------------------------------------------------------------
        #  ---------------------------- Bonotes -------------------------------------

        name = tkinter.Entry(
            self.window, font="Helvetica 14", borderwidth=0)
        name.pack()
        name.place(x=325, y=238, height=30, width=150)
        #  --------------------------------------------------------------------------

        self.window.mainloop()  # Muesta la ventana

########################################################################################################
########################################################################################################


class DeleteFolder:
    #  ----------- Centramos la Ventana en el medio------------------------------
    def centrar(self, window):
        pwidth = round(self.window.winfo_screenwidth()/2 - 900/2)
        pheight = round(self.window.winfo_screenheight()/2 - 500/2)
        window.geometry(str(900)+"x"+str(500)+"+"+str(pwidth)+"+"+str(pheight))

    def menu(self, A):
        self.window.destroy()
        Menu(A)
    #  --------------------------------------------------------------------------
    #  ------------------- Opciones de los Bonotes ------------------------------

    #  --------------------------------------------------------------------------
    #  --------------------------------------------------------------------------

    def __init__(self, A):
        window = Tk()  # Creo la ventana
        self.window.geometry("900x500")  # Doy dimensiones de la ventana
        # Ventana de tamaño fija (No tiene maximizar ni minimizar tamaño)
        self.window.resizable(0, 0)
        self.window.title("Eliminar Carpeta")  # Titulo de la ventana
        self.centrar(window)
        #  ----------------------- Agregamos el fondo  ------------------------------
        img = PhotoImage(file="Sprites/DeleteFolder.png")
        lbl = Label(self.window, image=img).place(x=0, y=0)
        #  --------------------------------------------------------------------------
        #  ---------------------------- Bonotes -------------------------------------
        img2 = PhotoImage(file="Sprites/back.png")
        btn1 = tkinter.Button(self.window, text="", bg='#14405D',
                              image=img2, borderwidth=0, command=lambda: self.menu(A))
        btn1.pack()
        btn1.place(x=358, y=355, height=45, width=45)
        #  --------------------------------------------------------------------------

        self.window.mainloop()  # Muesta la ventana

########################################################################################################
########################################################################################################


class ViewFolder:
    #  ----------- Centramos la Ventana en el medio------------------------------
    def centrar(self, window):
        pwidth = round(self.window.winfo_screenwidth()/2 - 900/2)
        pheight = round(self.window.winfo_screenheight()/2 - 500/2)
        window.geometry(str(900)+"x"+str(500)+"+"+str(pwidth)+"+"+str(pheight))

    def menu(self, A):
        self.window.destroy()
        A.ftp.cwd('../')
        Menu(A)

    def create(self, A):
        self.window.destroy()
        CreateFolder(A)
    #  --------------------------------------------------------------------------
    #  ------------------- Opciones de los Bonotes ------------------------------

    def show_selection(self, t1, A, dato):
        try:
            item1 = t1.selection()[0]
        except IndexError:
            messagebox.showwarning(
                message="Debe seleccionar un elemento.",
                title="No hay selección"
            )
        else:
            text = t1.item(item1, option="text")
            messagebox.showinfo(message=text, title="Selección")
            if (dato == 1):
                try:
                    A.deleteFile(text)
                except:
                    A.ftp.rmd(text)
            else:
                try:
                    A.ftp.cwd(text)
                    self.window.destroy()
                    ViewFolder(A)
                except:
                    messagebox.showinfo(
                        message='No selecciono una carpeta', title="Selección")

    def llenado_table(self, table, A):
        for A in A.ftp.nlst():
            table.insert("", END, text=A)

    #  --------------------------------------------------------------------------
    #  --------------------------------------------------------------------------

    def __init__(self, A):
        self.window = Tk()  # Creo la ventana
        self.window.geometry("900x500")  # Doy dimensiones de la ventana
        # Ventana de tamaño fija (No tiene maximizar ni minimizar tamaño)
        self.window.resizable(0, 0)
        self.window.title("Ver Carpeta")  # Titulo de la ventana
        self.centrar(self.window)
        #  ----------------------- Agregamos el fondo  ------------------------------
        img = PhotoImage(file="Sprites/ViewFolder.png")
        lbl = Label(self.window, image=img).place(x=0, y=0)
        lbl2 = Label(self.window, text=A.FTP_USER, bg='#14405D',
                     fg='White', font="Black 14").place(x=310, y=100)
        #  --------------------------------------------------------------------------
        #  ---------------------------- Bonotes -------------------------------------
        img2 = PhotoImage(file="Sprites/back.png")
        volver = tkinter.Button(self.window, text="", bg='#14405D',
                                image=img2, borderwidth=0, command=lambda: self.menu(A))
        volver.pack()
        volver.place(x=358, y=355, height=45, width=45)

        btn_mover = tkinter.Button(self.window, text="Mover",
                                   borderwidth=0, command=lambda: self.show_selection(files, A, 2))
        btn_mover.pack()
        btn_mover.place(x=150, y=300, height=40, width=130)

        btn_Crear = tkinter.Button(self.window, text="Crear Carpeta",
                                   borderwidth=0, command=lambda: self.create(A))
        btn_Crear.pack()
        btn_Crear.place(x=150, y=355, height=40, width=130)

        btn_eliminar = tkinter.Button(self.window, text="Eliminar Carpeta/Archivo",
                                      borderwidth=0, command=lambda: self.show_selection(files, A, 1))
        btn_eliminar.pack()
        btn_eliminar.place(x=150, y=410, height=40, width=130)

        #  --------------------------------------------------------------------------
        #  ----------------------- Agregamos la Tabla  ------------------------------

        files = ttk.Treeview(self.window, height=8)
        files.column("#0", width=200, anchor=CENTER)
        files.heading("#0", text="Archivos", anchor=CENTER)
        files.pack()
        files.place(x=310, y=150)
        self.llenado_table(files, A)

        self.window.mainloop()  # Muesta la ventana

########################################################################################################
########################################################################################################


if __name__ == "__main__":
    a = Login()
