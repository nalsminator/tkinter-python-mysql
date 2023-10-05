from tkinter import *
from tkinter import ttk
from countries import *
from tkinter import messagebox

class Ventana(Frame):
    
    paises = Countries()
    
    def __init__(self, master=None):
        super().__init__(master, width=680, height=260)
        self.master = master
        self.pack()
        self.create_widgets()
        self.llenarTreview()
        self.habilitarCajas("disabled")
        self.habilitarBotonesMenu("normal")
        self.habilitarBotonesGuardar("disabled")
        self.id = -1
        
    #region Eventos del formulario
        def habilitarCajas(self, estado):
            self.txtISO3.configure(state=estado)
            self.txtName.configure(state=estado)
            self.txtCapital.configure(state=estado)
            self.txtCurrency.configure(state=estado)
        
        def habilitarBotonesMenu(self, estado):
            self.btnNuevo.configure(state=estado)
            self.btnModificar.configure(state=estado)
            self.btnEliminar.configure(state=estado)
            
        def habilitarBotonesGuardar(self, estado):
            self.btnGuardar.configure(state=estado)
            self.btnCancelar.configure(state=estado)
            
        def limpiarCajas(self):
            self.txtCapital.delete(0, END)
            self.txtCurrency.delete(0, END)
            self.txtISO3.delete(0, END)
            self.txtName.delete(0, END)
            
        def limpiarGrid(self):
            for item in self.grid.get_children():
                self.grid.delete(item)
    #endregion
   
        
    def llenarTreview(self):
        self.limpiarGrid()
        datos = self.paises.consulta_paises()
        for row in datos:
            self.grid.insert("", END, text=row[0], values=(row[1], row[2], row[3], row[4]))
        
        if len(self.grid.get_children()) > 0:
            #selecciona el primer elemento del grid
            self.grid.selection_set(self.grid.get_children()[0])

    #region Botones
        def fNuevo(self):
            self.habilitarCajas("normal")
            self.habilitarBotonesMenu("disabled")
            self.habilitarBotonesGuardar("normal")
            self.limpiarCajas()
            self.txtISO3.focus()
       
        def fGuardar(self):
            if self.id == -1:
                self.paises.inserta_pais(self.txtISO3.get(), self.txtName.get(), self.txtCapital.get(), self.txtCurrency.get())
                messagebox.showinfo("Insertar", "Elemento insertado correctamente.")
            else:
                self.paises.modifica_pais(self.id, self.txtISO3.get(), self.txtName.get(), self.txtCapital.get(), self.txtCurrency.get())
                messagebox.showinfo("Modificar", "Elemento modificado correctamente.")
                
            self.limpiarCajas()
            self.llenarTreview()
            self.habilitarBotonesMenu("normal")
            self.habilitarBotonesGuardar("disabled")
            self.habilitarCajas("disabled")
                
        def fModificar(self):
            selected = self.grid.focus()
            clave = self.grid.item(selected, 'text')
            if clave == '':
                messagebox.showwarning("Modificar", "Debes seleccionar un elemento.")
            else:
                valores = self.grid.item(selected, 'values')
                self.id = clave
                self.habilitarCajas("normal")
                self.limpiarCajas()
                self.txtISO3.insert(0, valores[0])
                self.txtName.insert(0, valores[1])
                self.txtCapital.insert(0, valores[2])
                self.txtCurrency.insert(0, valores[3])
                self.habilitarBotonesMenu("disabled")
                self.habilitarBotonesGuardar("normal")
                self.llenarTreview()
                self.txtISO3.focus()
            
        def fEliminar(self):
            selected = self.grid.focus()
            clave = self.grid.item(selected, 'text')
            
            if clave == '':
                messagebox.showwarning("Eliminar", "Debes seleccionar un elemento.")
            else:
                valores = self.grid.item(selected, 'values')
                data = str(clave) + ", " + valores[0] + ", " + valores[1] + ", " + valores[2]
                r = messagebox.askquestion("Eliminar", "Deseas eliminar el registro seleccionado?" + data)
                if r == messagebox.YES:
                    n = self.paises.elimina_pais(clave)
                    if n == 1:
                        messagebox.showinfo("Eliminar", "Elemento eliminado correctamente.")
                        self.llenarTreview()
                    else:
                        messagebox.showwarning("Eliminar", "No fue posible eliminar el elemento.")

        def fCancelar(self):
            r = messagebox.askquestion("Cancelar", "Esta seguro que desea cancelar la operación actual?")
            if r == messagebox.YES:
                self.limpiarCajas()
                self.limpiarGrid()
                self.llenarTreview()
                self.habilitarBotonesMenu("normal")
                self.habilitarBotonesGuardar("disabled")
                self.habilitarCajas("disabled")
    #endregion       
    
    def create_widgets(self):
        frame1 = Frame(self, bg="#bfdaff")
        frame1.place(x=0, y=0, width=93, height=259)
        
        #btnNuevo
        self.btnNuevo=Button(frame1, text="Nuevo", command=self.fNuevo, bg="blue", fg="white")
        self.btnNuevo.place(x=5, y=50, width=80, height=30)
        #btnModificar
        self.btnModificar=Button(frame1, text="Modificar", command=self.fModificar, bg="blue", fg="white")
        self.btnModificar.place(x=5, y=90, width=80, height=30)
        #btnEliminar
        self.btnEliminar=Button(frame1, text="Eliminar", command=self.fEliminar, bg="blue", fg="white")
        self.btnEliminar.place(x=5, y=130, width=80, height=30)
        #frame2
        frame2 = Frame(self, bg="#d3dde3")
        frame2.place(x=95, y=0, width=150, height=259)
        #txtISO3
        lbl1 = Label(frame2, text="ISO3: ")
        lbl1.place(x=3, y=5)
        self.txtISO3=Entry(frame2)
        self.txtISO3.place(x=3, y=25, width=50, height=20)
        #txtName
        lbl2 = Label(frame2, text="Country Name: ")
        lbl2.place(x=3, y=55)
        self.txtName=Entry(frame2)
        self.txtName.place(x=3, y=75, width=100, height=20)
        #txtCapital
        lbl3 = Label(frame2, text="Capital: ")
        lbl3.place(x=3, y=105)
        self.txtCapital=Entry(frame2)
        self.txtCapital.place(x=3, y=125, width=100, height=20)
        #txtCurrency
        lbl4 = Label(frame2, text="Currency Code: ")
        lbl4.place(x=3, y=155)
        self.txtCurrency=Entry(frame2)
        self.txtCurrency.place(x=3, y=175, width=50, height=20)
        #btnGuardar
        self.btnGuardar=Button(frame2, text="Guardar", command=self.fGuardar, bg="green", fg="white")
        self.btnGuardar.place(x=10, y=210, width=60, height=30)
        #btnCancelar
        self.btnCancelar=Button(frame2, text="Cancelar", command=self.fCancelar, bg="red", fg="white")
        self.btnCancelar.place(x=80, y=210, width=60, height=30)
        
        
        #frame3
        frame3 = Frame(self, bg="yellow")
        frame3.place(x=247, y=0, width=420, height=259)
        
        #grid
        self.grid = ttk.Treeview(frame3, columns=("col1", "col2", "col3", "col4"))
        self.grid.column("#0", width=60)
        self.grid.column("col1", width=70, anchor=CENTER)
        self.grid.column("col2", width=90, anchor=CENTER)
        self.grid.column("col3", width=90, anchor=CENTER)
        self.grid.column("col4", width=90, anchor=CENTER)
        self.grid.heading("#0", text="Id", anchor=CENTER)
        self.grid.heading("col1", text="ISO3", anchor=CENTER)
        self.grid.heading("col2", text="Country Name", anchor=CENTER)
        self.grid.heading("col3", text="Capital", anchor=CENTER)
        self.grid.heading("col4", text="Currency Code", anchor=CENTER)
        
        self.grid.pack(side=LEFT, fill=Y)
        sb = Scrollbar(frame3, orient=VERTICAL)
        sb.pack(side=RIGHT, fill = Y)
        self.grid.config(yscrollcommand=sb.set)
        sb.config(command=self.grid.yview)
        self.grid['selectmode'] = 'browse'