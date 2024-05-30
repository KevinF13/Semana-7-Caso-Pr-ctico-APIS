import tkinter as tk
from tkinter import ttk
import requests
import pyperclip


class InventarioCLI:
    def __init__(self, base_url):
        self.base_url = base_url

    def create(self, data):
        response = requests.post(f"{self.base_url}/inventario", json=data)
        return response.json()

    def get_all(self):
        response = requests.get(f"{self.base_url}/inventario")
        return response.json()

    def get_one(self, id):
        response = requests.get(f"{self.base_url}/inventario/{id}")
        return response.json()

    def update(self, id, data):
        response = requests.put(f"{self.base_url}/inventario/{id}", json=data)
        return response.json()

    def remove(self, id):
        response = requests.delete(f"{self.base_url}/inventario/{id}")
        return response.json()

def create_item():
    nombre = nombre_entry.get()
    descripcion = descripcion_entry.get()
    cantidad = cantidad_entry.get()
    precio = precio_entry.get()
    data = {"nombre": nombre, "descripcion": descripcion, "cantidad": cantidad, "precio": precio}
    
    try:
        response = inventario_cli.create(data)
        print("Item creado:", response)
    except Exception as e:
        print("Error al crear el item:", e)

def get_all_items():
    items = inventario_cli.get_all()
    print("Todos los items de inventario:")
    for item in items:
        print(item)

def get_item_by_id():
    id = id_entry.get()
    item = inventario_cli.get_one(id)
    print("Item de inventario encontrado:", item)

def update_item():
    id = id_update_entry.get()
    nombre = nombre_update_entry.get()
    descripcion = descripcion_update_entry.get()
    cantidad = cantidad_update_entry.get()
    precio = precio_update_entry.get()
    data = {"nombre": nombre, "descripcion": descripcion, "cantidad": cantidad, "precio": precio}
    response = inventario_cli.update(id, data)
    print("Item actualizado:", response)

def remove_item():
    id = id_remove_entry.get()
    response = inventario_cli.remove(id)
    print("Item eliminado:", response)

def create_tab1():
    global nombre_entry, descripcion_entry, cantidad_entry, precio_entry
    tab1 = ttk.Frame(tab_control)
    tab_control.add(tab1, text='Crear Item')
    
    nombre_label = ttk.Label(tab1, text="Nombre del item:")
    nombre_label.grid(row=0, column=0, padx=5, pady=5)
    nombre_entry = ttk.Entry(tab1)
    nombre_entry.grid(row=0, column=1, padx=5, pady=5)
    
    descripcion_label = ttk.Label(tab1, text="Descripción del item:")
    descripcion_label.grid(row=1, column=0, padx=5, pady=5)
    descripcion_entry = ttk.Entry(tab1)
    descripcion_entry.grid(row=1, column=1, padx=5, pady=5)
    
    cantidad_label = ttk.Label(tab1, text="Cantidad del item:")
    cantidad_label.grid(row=2, column=0, padx=5, pady=5)
    cantidad_entry = ttk.Entry(tab1)
    cantidad_entry.grid(row=2, column=1, padx=5, pady=5)
    
    precio_label = ttk.Label(tab1, text="Precio del item:")
    precio_label.grid(row=3, column=0, padx=5, pady=5)
    precio_entry = ttk.Entry(tab1)
    precio_entry.grid(row=3, column=1, padx=5, pady=5)
    
    crear_btn = ttk.Button(tab1, text="Crear Item", command=create_item)
    crear_btn.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

def create_tab2():
    tab2 = ttk.Frame(tab_control)
    tab_control.add(tab2, text='Obtener Todos')

    # Crear el Treeview
    tree = ttk.Treeview(tab2)
    tree["columns"] = ("Nombre", "Descripción", "Cantidad", "Precio")
    tree.heading("#0", text="ID")
    tree.heading("Nombre", text="Nombre")
    tree.heading("Descripción", text="Descripción")
    tree.heading("Cantidad", text="Cantidad")
    tree.heading("Precio", text="Precio")
    tree.pack(expand=True, fill="both")

    # Función para actualizar los datos del Treeview
    def update_treeview():
        # Eliminar todos los elementos del Treeview
        for item in tree.get_children():
            tree.delete(item)

        # Obtener todos los items y agregarlos al Treeview
        items = inventario_cli.get_all()
        for item in items:
            tree.insert("", "end", text=item["_id"], values=(item["nombre"], item["descripcion"], item["cantidad"], item["precio"]))

    # Agregar evento de selección de pestaña al Treeview
    def on_tab_selected(event):
        selected_tab = tab_control.select()
        tab_text = tab_control.tab(selected_tab, "text")
        if tab_text == "Obtener Todos":
            update_treeview()

    tab_control.bind("<<NotebookTabChanged>>", on_tab_selected)

    # Función para copiar el ID seleccionado al portapapeles
    def copy_id_to_clipboard(event):
        selected_item = tree.selection()
        if selected_item:
            item_id = tree.item(selected_item, "text")
            pyperclip.copy(item_id)

    # Agregar evento de clic al Treeview
    tree.bind("<ButtonRelease-1>", copy_id_to_clipboard)

    # Actualizar los datos del Treeview al iniciar la pestaña
    update_treeview()


def create_tab3():
    tab3 = ttk.Frame(tab_control)
    tab_control.add(tab3, text='Obtener por ID')

    id_label = ttk.Label(tab3, text="Ingrese el ID del item:")
    id_label.pack(pady=10)
    id_entry = ttk.Entry(tab3)
    id_entry.pack(pady=10)

    # Función para obtener el item por ID
    def get_item():
        id = id_entry.get()
        item = inventario_cli.get_one(id)
        if item:
            item_details_label.config(text=f"Detalles del Item:\nNombre: {item['nombre']}\nDescripción: {item['descripcion']}\nCantidad: {item['cantidad']}\nPrecio: {item['precio']}")
        else:
            item_details_label.config(text="Item no encontrado")

    # Botón para obtener el item por ID
    get_by_id_btn = ttk.Button(tab3, text="Obtener Item por ID", command=get_item)
    get_by_id_btn.pack(pady=10)

    # Etiqueta para mostrar los detalles del item
    item_details_label = ttk.Label(tab3, text="")
    item_details_label.pack(pady=10)


def create_tab4():
    tab4 = ttk.Frame(tab_control)
    tab_control.add(tab4, text='Actualizar por ID')

    # Campos de entrada para el ID del item y los nuevos valores
    id_label = ttk.Label(tab4, text="ID del item a actualizar:")
    id_label.grid(row=0, column=0, padx=5, pady=5)
    id_update_entry = ttk.Entry(tab4)
    id_update_entry.grid(row=0, column=1, padx=5, pady=5)

    nombre_update_label = ttk.Label(tab4, text="Nuevo nombre del item:")
    nombre_update_label.grid(row=1, column=0, padx=5, pady=5)
    nombre_update_entry = ttk.Entry(tab4)
    nombre_update_entry.grid(row=1, column=1, padx=5, pady=5)

    descripcion_update_label = ttk.Label(tab4, text="Nueva descripción del item:")
    descripcion_update_label.grid(row=2, column=0, padx=5, pady=5)
    descripcion_update_entry = ttk.Entry(tab4)
    descripcion_update_entry.grid(row=2, column=1, padx=5, pady=5)

    cantidad_update_label = ttk.Label(tab4, text="Nueva cantidad del item:")
    cantidad_update_label.grid(row=3, column=0, padx=5, pady=5)
    cantidad_update_entry = ttk.Entry(tab4)
    cantidad_update_entry.grid(row=3, column=1, padx=5, pady=5)

    precio_update_label = ttk.Label(tab4, text="Nuevo precio del item:")
    precio_update_label.grid(row=4, column=0, padx=5, pady=5)
    precio_update_entry = ttk.Entry(tab4)
    precio_update_entry.grid(row=4, column=1, padx=5, pady=5)

    # Función para actualizar el item
    def update_item():
        id = id_update_entry.get()
        nombre = nombre_update_entry.get()
        descripcion = descripcion_update_entry.get()
        cantidad = cantidad_update_entry.get()
        precio = precio_update_entry.get()
        data = {"nombre": nombre, "descripcion": descripcion, "cantidad": cantidad, "precio": precio}
        response = inventario_cli.update(id, data)
        print("Item actualizado:", response)

    # Botón para ejecutar la actualización
    update_btn = ttk.Button(tab4, text="Actualizar Item", command=update_item)
    update_btn.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

def create_tab5():
    tab5 = ttk.Frame(tab_control)
    tab_control.add(tab5, text='Eliminar por ID')

    # Campo de entrada para el ID del item a eliminar
    id_remove_label = ttk.Label(tab5, text="ID del item a eliminar:")
    id_remove_label.grid(row=0, column=0, padx=5, pady=5)
    id_remove_entry = ttk.Entry(tab5)
    id_remove_entry.grid(row=0, column=1, padx=5, pady=5)

    # Función para eliminar el item
    def remove_item():
        id = id_remove_entry.get()
        response = inventario_cli.remove(id)
        print("Item eliminado:", response)

    # Botón para ejecutar la eliminación
    remove_btn = ttk.Button(tab5, text="Eliminar Item", command=remove_item)
    remove_btn.grid(row=1, column=0, columnspan=2, padx=5, pady=5)


# Crear la ventana principal
root = tk.Tk()
root.title("Gestión de Inventario")

# Crear el control de pestañas
tab_control = ttk.Notebook(root)

# Crear instancia de la clase InventarioCLI
inventario_cli = InventarioCLI("http://localhost:3000")  # Cambia la URL por la correcta

# Crear las pestañas
create_tab1()
create_tab2()
create_tab3()
create_tab4()
create_tab5()

# Empacar el control de pestañas
tab_control.pack(expand=1, fill="both")

# Ejecutar la ventana
root.mainloop()
