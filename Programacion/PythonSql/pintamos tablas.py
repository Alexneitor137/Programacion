import tinker as tk
from tinker import ttk

ventana = rk.tK()

ARBOL = ttk.Treeview(ventana, columns = ("nombre","apellidos"), show = "headings")
arbol.heading("nombre", text = "Nombre del cliente")
arbol.heading("apellidos", text = "Apellidos del cliente")

arbol.insert("", "end", values = ("Alejandro","Calderón Sánchez"))
arbol.insert("", "end", values = ("Manolo","Lopéz Moragon"))

arbol.pack(padx = 20, Pady = 20)

ventana.mainloop()