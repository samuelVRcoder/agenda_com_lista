try:
    import tkinter as tk
    from tkinter import messagebox as msg
    from tkinter.ttk import Combobox
    import os

    import sqlite3 as sql

    conn = sql.connect("contatos.sqlite3")

    cursor = conn.cursor()

    cursor.execute("create table if not exists users (nome varchar(255), telefone varchar(255)); ")

    frame = tk.Tk() 
    frame.title("Agenda") 
    frame.geometry('250x300')
    frame.resizable(False, False)
      
    def create(): 
        inp = inputnome.get(1.0, "end-1c")
        fone = inputfone.get(1.0, "end-1c")
        
        if len(inp) > 0:
                if len(fone) > 0:
                    cursor.execute(f"insert into users (nome, telefone) values (?, ?);",(inp, fone))
                    conn.commit()

    def update():
        inp = inputnome.get(1.0, "end-1c")
        fone = inputfone.get(1.0, "end-1c")
        if len(inp) > 0:
            if len(fone) > 0:
                cursor.execute(f"update users set telefone = ? where nome = ?",(fone, inp))
                conn.commit()
        
        

    def deleteNome(): 
        inp = inputnome.get(1.0, "end-1c") 
        
        cursor.execute("delete from users where nome = ? ;", (inp,))

    def deleteFone(): 
        inp = inputfone.get(1.0, "end-1c") 
        
        cursor.execute("delete from users where telefone = ? ;", (inp,))


    def read(): 
        inp = inputnome.get(1.0, "end-1c") 
        
        

        lista = list(cursor.execute("select * from users where nome = ? limit 5", (inp,)))

        lista_str = ''
        for i,a in lista:
            lista_str += i+","+a+"\n\n"
        msg.showinfo("Output", lista_str)

    def autor():
        msg.showinfo("Autor", "Samuel VR\n\nGitHub: samuelVRcoder\n\nEmail:samuelroberto03@hotmail.com")




    combo = Combobox(frame)
    combo['values']= list(cursor.execute("select * from users"))

    combo.pack()


    lblnome = tk.Label(frame, text = "Nome") 
    lblnome.pack()  
     
    inputnome = tk.Text(frame, 
                       height = 1, 
                       width = 20)
    inputnome.pack()

    lblfone = tk.Label(frame, text = "Fone") 
    lblfone.pack()


    inputfone = tk.Text(frame, 
                       height = 1, 
                       width = 20)
      
    inputfone.pack() 
      
     
    printButton = tk.Button(frame, 
                            text = "Salvar contato",  
                            command = create) 
    printButton.pack()


    printButton = tk.Button(frame, 
                            text = "Pesquisar por nome",  
                            command = read) 
    printButton.pack()


    printButton = tk.Button(frame, 
                            text = "Deletar por nome",  
                            command = deleteNome)
    printButton.pack()

    printButton = tk.Button(frame, 
                            text = "Deletar por telefone",  
                            command = deleteFone)

    printButton.pack()

    printButton = tk.Button(frame, 
                            text = "Atualizar telefone por nome",  
                            command = update)
    printButton.pack()

    printButton = tk.Button(frame, 
                            text = "Sobre o autor",  
                            command = autor)

    printButton.pack()
     
    lbl = tk.Label(frame, text = "") 
    lbl.pack()

    frame.mainloop()

except Exception as e:
    try:
        from tkinter import messagebox as msg
        msg.showerror("Erro", str(e))
    except:
        pass
