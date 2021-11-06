from tkinter import Frame, Tk,Canvas,Label ,Frame, Entry, Button,W,E,Listbox,END, Toplevel
from tkinter.constants import E
import psycopg2

root = Tk()
root.title("Taller3")
def error_mesage():
    print("Error try again")
    ventana_error = Toplevel()
    ventana_error.geometry("200x100")
    ventana_error.title("Login Error")
    label = Label(ventana_error,text='Error, password incorrect ')
    label.grid(row = 0 , column= 3)

    button = Button(ventana_error,text="Please try again !!",command = ventana_error.destroy).grid(row=1,column=3)

def autenticate(password,name):
    conn = psycopg2.connect(
    dbname = "taller3",
    user = "postgres",
    password = "root",
    host = "localhost",
    port = "5432"
    )

    cursor = conn.cursor()
    query = '''SELECT * FROM entrenador WHERE password = %s AND nombre = %s'''
    cursor.execute(query,(password , name ))

    row = cursor.fetchone()

    if row is not None:
        print(row)
        
        pantalla_principal()
    else:
        error_mesage()
    conn.commit()
    conn.close()
def pantalla_principal():
    principal = Toplevel()
    principal.geometry("500x500")
    principal.title("Comienza el puto game")
def pantallLogin():

    #canvas

    canvas = Canvas(root,height=380,width=400)
    canvas.pack()

    frame = Frame()
    frame.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)
    #nombre
    label = Label(frame,text = 'User Login')
    label.grid(row=0,column = 1)

    label = Label(frame,text= ' User_name : ')
    label.grid(row=1,column=0)

    entry_name = Entry(frame)
    entry_name.grid(row=1,column=1)


    label = Label(frame,text = ' Password :')
    label.grid(row=2,column = 1)

    label = Label(frame,text= ' Password : ')
    label.grid(row=2,column=0)

    entry_pass = Entry(frame)


    entry_pass.grid(row=2,column=1)


    button = Button(frame, text="Login", command=lambda: autenticate(
        entry_pass.get(),
        entry_name.get()
        ))

    button.grid(row=4,column=1,sticky=W+E)

pantallLogin()
root.mainloop()