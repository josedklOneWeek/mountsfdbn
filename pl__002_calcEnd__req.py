

from tkinter import Button, Tk, Text, END, re



class Aplicacion():         
    def __init__(self):

        #self.ventana1 = tk.Tk()
        self.ventana1 = Tk()

        self.pantalla = Text(self.ventana1, state="normal", width=20, height=1, 
        #background="gray99", foreground="black", font=("helvetica",30))
        background="#cecece", foreground="black", font=("helvetica",30), pady=50)
        self.pantalla.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        self.operacion = ""

        boton1  = self.crearBoton("C",ancho=5) # =============
        boton2  = self.crearBoton("%",ancho=5)
        boton3  = self.crearBoton("/",ancho=5)
        #boton4  = self.crearBoton("\u232B", escribir=False) # delete
        boton4  = self.crearBoton("LL", escribir=False) # delete
        boton5  = self.crearBoton(7,ancho=5)
        boton6  = self.crearBoton(8,ancho=5)
        boton7  = self.crearBoton(9,ancho=5)
        #boton8  = self.crearBoton("\u00f7",ancho=5) # operador =
        boton8  = self.crearBoton("*",ancho=5) # operador =
                    
        #boton8  = self.crearBoton(u"\00f7") # operador =
        boton9  = self.crearBoton(4,ancho=5)
        boton10 = self.crearBoton(5,ancho=5)
        boton11 = self.crearBoton(6,ancho=5)
        boton12 = self.crearBoton("-",ancho=5)
        boton13 = self.crearBoton(1,ancho=5)
        boton14 = self.crearBoton(2,ancho=5)
        boton15 = self.crearBoton(3,ancho=5)
        boton16 = self.crearBoton("+",ancho=5)
        #boton17 = self.crearBoton("=", escribir=False, ancho=20, alto=2)
        #boton17 = self.crearBoton("=", escribir=False, ancho=5)
        boton17 = self.crearBoton(0, escribir=False, ancho=5)

        boton18 = self.crearBoton(0,ancho=5)
        boton19 = self.crearBoton(".",ancho=5)
        boton20 = self.crearBoton("=",ancho=5)
        


        botones  =  [boton1, boton2, boton3, boton4, boton5, boton6, boton7, boton8, 
        boton9, boton10, boton11, boton12, boton13, boton14, boton15, boton16, boton17, 
        boton18, boton19, boton20 ]

        
        contador=0

        for fila in range(1,5):
            for columna in range(4):
                botones[contador].grid(row=fila, column=columna)
                contador+=1

        #botones[16].grid(row=5, column=0, columnspan=4) # or

        #botones[17].grid(row=5, column=0, columnspan=1,padx=1) ?
        botones[17].grid(row=5, column=0, columnspan=1)
        botones[18].grid(row=5, column=0, columnspan=3)
        botones[19].grid(row=5, column=0, columnspan=5)
        

        ###
        #botones[10].grid(row=2, column=0, columnspan=2,padx=100) # R5
       
        #botones[6].grid(row=2, column=0, columnspan=2,padx=100) # ?
        #botones[7].grid(row=3, column=0, columnspan=2,padx=100) # ?

        #botones[13].grid(row=3, column=0, columnspan=2,padx=140) # ?
        #botones[14].grid(row=4, column=0, columnspan=2,padx=140) # 3
        ###

        #botones[17].grid(row=5, column=0, columnspan=3)
        #botones[18].grid(row=5, column=0, columnspan=4)
        

    def crearBoton(self, valor, escribir=True, ancho=9, alto=2):
        return Button(self.ventana1, text=valor, width=ancho, height=alto, font=("Helvetica", 15), command=lambda:self.click(valor, escribir) )



    # ----------------------------------------------------------------------------------------------------------------------


    def click(self, texto, escribir):
        #texto = self.pantalla
        sdds = 10
        resultado = ""
        dop = ""
        Pdekd = "manaos"
        if not escribir:
            if texto=="=" and self.operacion!="":
               #resultado = str(eval(self.operacion))
               dop += str(eval(self.operacion))
               self.operacion == ""

               print("___DFdfFSfds_1__" + dop )
               
               self.limpiar_pantalla()  
               #print(Pdekd.replace("man",""))
               self.mostrar_en_pantalla(dop)


        if texto == "LL": # delete            
            self.operacion=""
            self.limpiar_pantalla()
            #print(0)

        else:
            self.operacion += str(texto)
            #self.mostrar_en_pantalla(texto)            
            #self.mostrar_en_pantalla(False)            
            self.mostrar_en_pantalla(texto)
          


    def limpiar_pantalla(self):
        self.pantalla.configure(state="normal")
        self.pantalla.delete("0.0",END)
        self.pantalla.configure(state="normal") #disable
        pass

    def mostrar_en_pantalla(self, valor):
        self.pantalla.configure(state="normal") #disable
        #self.pantalla.insert(END,valor)
        self.pantalla.insert(END, valor)
        self.pantalla.configure(state="normal") #disable



        
# --------------------------------------------------------------------

app = Aplicacion()
app.ventana1.mainloop()             


