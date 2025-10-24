import tkinter as tk

ventana = tk.Tk()

marco = tk.Frame(ventana)

def insertar():
    print("Vamos a insertar un cliente")

tk.Label(marco,text="Introduce el dni/nie del cliente").pack(padx=10,pady=10)
dninie = tk.Entry(marco)
dninie.pack(padx=10,pady=10)

tk.Label(marco,text="Introduce el nombre del cliente").pack(padx=10,pady=10)
nombre = tk.Entry(marco)
nombre.pack(padx=10,pady=10)


tk.Label(marco,text="Introduce los apellidos del cliente").pack(padx=10,pady=10)
apellidos = tk.Entry(marco)
apellidos.pack(padx=10,pady=10)


tk.Label(marco,text="Introduce el email del cliente").pack(padx=10,pady=10)
email = tk.Entry(marco)
email.pack(padx=10,pady=10)

tk.Button(marco,text="insertar cliente",command = insertar).pack(padx=10,pady=10)

marco.pack(padx=20,pady=20)

ventana.mainloop()

