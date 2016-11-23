#Libreria a utilizar
import math
import cPickle
from Tkinter import *
from tkMessageBox import *
import sys
import os.path
import time

#Archivo de memoria
archivo = "memoria.mem"

#Metodo que crea la memoria
def crear():
    db = []
    cPickle.dump(db,open("memoria.mem","wb"))

#Condicion que evalua si existe la memoria y la abre, si no existe la crea
if os.path.exists(archivo):
    print "Abriendo memoria"
else:
    print "Creando memoria..."
    crear()   
    time.sleep(5)

#Matriz base de comparacion
matriz = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
#Se abre la memoria
memoria = cPickle.load(open("memoria.mem","rb"))

#Metodo para imprimir la matriz     
def imp(que,rango):
    ac = 0
    if ac==1:
        c = 0
        c1 = rango
                   
        print "=================="
        for i in range(0,rango):
            a = que[c:c1]
            k =  "       ".join(str(o)for o in a)
            print ""
            print k
            c +=rango
            c1+=rango
            print "========================"
    else:
        pass

#Metodo para imprimir la matriz auxiliar
def imp2(que,rango):
    ac = 1
    if ac==1:
        c = 0
        c1 = rango
                   
        print "=================="
        for i in range(0,rango):
            a = que[c:c1]
            k =  "       ".join(str(o)for o in a)
            print ""
            print k
            c +=rango
            c1+=rango
            print "========================"
    else:
        pass

#Neurona de auxilio en el analisis del patron similar
def neurona(entrada,peso):               #Valores de entradas y valores de peso
    c = 0                                #conteo
    multiplicados = []                   #buffer 1 "array"
    for entrada1 in entrada:             #itera sobre la entradas
        analisis1 = entrada1 * peso[c]   #multiplica las entradas por los pesos
        multiplicados.append(analisis1)  #la agrega al buffer "array"
        c +=1                            #aumento del conteo para ver el peso a medida que se repite el bucle
    suma = 0                             #buffer de suma "variable"       
    for i in multiplicados:              #itera sobre el array "multiplicados"
        suma+=i                          #va sumando a suma "variable" para sacar el resultado
    peso = math.tanh(suma)               #calculo funcional para reprimir el valor de suma ***tangente inversa de la suma***
    if suma == len(entrada):             #condicion para verfiricar si la suma es igual a la cantidad de valores entrada
        return suma                      #si es igual devolver la suma
    return peso                          #devuelve el peso calculado tres pasos atras

#Metodo con el que se concreta el analisis del patron     
def final():
    global candidatos,y					  #Variables globales para lo candidatos y una variable auxiliar
    candidatos = {}						  #Se convierte la variable candidatos
    z = 0								  #Conteo
    for i in memoria:					  #Itera sobre lo que tiene la memoria
        peso = neurona(memoria[z],matriz) #Se le asigna al peso lo resultante del metodo Neurona
        print "peso:",peso                #Se imprime el peso
        if peso <= 0.9999999999:#99999:   #Condicion para verificar si se acerca el peso a lo esperado
            pass                          #Pasa todo si es true
        else:                             #De lo contrario
            candidatos[peso] = memoria[z] #Se le asigna un valor a los candidatos en la posicion especifica
        z+=1                              #Se aumenta el contador Z
                   
    y = 0                                 #Se le asigna 0 Y
    for m in candidatos:                  #Itera sobre lo candidatos previamente calculados
        if m > y:                         #Condicion que verifica si el contador es mayor a la variable auxiliar
            y = 0                         #Si es true se le asigna 0 primero
            y +=m                         #Despues un valor que es igual al contador
        else:                             #De lo contrario
            pass                          #Pasa todo
                           
    if candidatos == {}:				  #Si los candidatos sigue siendo vacio se imprime el mensaje de que no hay conincidencias.
        print "No encontre coincidencias, lo lamento."
    else:								  #De lo contrario se manda llamar el metodo imp2 que sirve para imprimir la matriz resultante
        print "Comparando ",matriz," con ",candidatos[y]
        print "Matriz:",matriz
        print "RESULTADO:"
        imp2(candidatos[y],5)			  #Se manda llamar el metodo y se envian los candidatos a imprimir y el rango para las letras
    print candidatos					  #Se imprimen los candidatos

#Metodo de aprendizaje del sistema
def aprender():
    def memorizar(palabra,lon):						  #Metodo memorizar que se llama dentro del metodo aprender
        matriz=[]									  #Variable matriz igual a array
        c = 0										  #Contador 1 
        c1= 0										  #Contador 2
        for i in range(0,len(palabra)):				  #Itera sobre el tamano de la palabra
            for i in palabra:						  #Itera sobre la palabra
                matriz.append(palabra[c1]*palabra[c]) #Se agrega un valor a la matriz
                c+=1								  #Se autoincrementa en 1 en contador 1
            c = 0									  #Al terminar se vuelve a asignar a 0 el contador 1
            c1+=1									  #El contador 2 se autoincrementa en 1
        imp(matriz,lon)								  #Se manda llamar el metodo imp para imprimir la matriz
        return matriz                                 #Se retorna la matriz
    a =  memorizar(matriz,25)						  #Se asigna a una variable el resultado del metodo memorizar
    memoria.append(a[0:25])							  #Se le agrega a la memoria el valor de la variable
    memoria.reverse()								  #Se invierte la memoria
    print "Matriz aprendida:"
    for t in memoria:								  #Itera sobre la memoria
        print t
    cPickle.dump(memoria,open("memoria.mem","wb"))    #Se abre la memoria para almacenar el valor
    resetear_tabla()								  #Se limpia la matriz

#Metodo que llama otros metodos para realizar el proceso de analizar un patron     
def analizar():
    final()
    resetear_tabla()
    rellenar()
     
                   
#**************INTERFAZ GRAFICA*************************
#Ventanas
ventana = Tk()
ventana2 = Tk()

#Clase nume que pinta el boton y retorna el dato necesario
class  nume:
    def una(self):
        matriz[0] = 1
        button1.config(bg="#0000FF")
        imp(matriz,5)
    def dos(self):
        matriz[1] = 1
        button2.config(bg="#0000FF")
        imp(matriz,5)
    def tres(self):
        matriz[2] = 1
        button3.config(bg="#0000FF")
        imp(matriz,5)
    def cuatro(self):
        matriz[3] = 1
        button4.config(bg="#0000FF")
        imp(matriz,5)
    def cinco(self):
        matriz[4] = 1
        button5.config(bg="#0000FF")
        imp(matriz,5)
    def seis(self):
        matriz[5] = 1
        button6.config(bg="#0000FF")
        imp(matriz,5)
    def siete(self):
        matriz[6] = 1
        button7.config(bg="#0000FF")
        imp(matriz,5)
    def ocho(self):
        matriz[7] = 1
        button8.config(bg="#0000FF")
        imp(matriz,5)
    def nueve(self):
        matriz[8] = 1
        button9.config(bg="#0000FF")
        imp(matriz,5)
    def diez(self):
        matriz[9] = 1
        button10.config(bg="#0000FF")
        imp(matriz,5)
    def once(self):
        matriz[10] = 1
        button11.config(bg="#0000FF")
        imp(matriz,5)
    def doce(self):
        matriz[11] = 1
        button12.config(bg="#0000FF")
        imp(matriz,5)
    def trece(self):
        matriz[12] = 1
        button13.config(bg="#0000FF")
        imp(matriz,5)
    def catorce(self):
        matriz[13] = 1
        button14.config(bg="#0000FF")
        imp(matriz,5)
    def quince(self):
        matriz[14] = 1
        button15.config(bg="#0000FF")
        imp(matriz,5)
    def diesiseis(self):
        matriz[15] = 1
        button16.config(bg="#0000FF")
        imp(matriz,5)
    def diesisiete(self):
        matriz[16] = 1
        button17.config(bg="#0000FF")
        imp(matriz,5)
    def diesiocho(self):
        matriz[17] = 1
        button18.config(bg="#0000FF")
        imp(matriz,5)
    def diesinueve(self):
        matriz[18] = 1
        button19.config(bg="#0000FF")
        imp(matriz,5)
    def veinte(self):
        matriz[19] = 1
        button20.config(bg="#0000FF")
        imp(matriz,5)
    def veintiuno(self):
        matriz[20] = 1
        button21.config(bg="#0000FF")
        imp(matriz,5)
    def veintidos(self):
        matriz[21] = 1
        button22.config(bg="#0000FF")
        imp(matriz,5)
    def veintitres(self):
        matriz[22] = 1
        button23.config(bg="#0000FF")
        imp(matriz,5)
    def veinticuatro(self):
        matriz[23] = 1
        button24.config(bg="#0000FF")
        imp(matriz,5)    
    def veinticinco(self):
        matriz[24] = 1
        button25.config(bg="#0000FF")
        imp(matriz,5)

#Variable core que almacena lo que viene de la clase nume.
core = nume()

#Metodo que sirve para borrar lo seleccionado de la matriz.
def resetear_tabla():
    c = 0
    for i in matriz:
        matriz[c] = -1
        c+=1
    for t in botones:
        t.config(bg="#FFFFFF")

#Metodo que sirve para borar la memoria del programa y cerrar el programa.
def borrar_memoria():
    memoria = []
    cPickle.dump(memoria,open("memoria.mem","wb"))
    sys.exit(0)
 
#Metodo que sirve para rellenar la mtriz y mostrar el resultado del analisis de lo previamente aprendido  
def rellenar():
    c = 0
    if candidatos == {}:
        return 0
    for i in candidatos[y]:
                   
        if c == len(botones):
            break
        if i == 1:
           botones[c].config(bg="#01D826")
        if i == -1:
            pass
        c+=1
     
     
#Propiedades de las ventanas
ventana.title("Matriz de aprendizaje")
ventana.config(bg="#000000")
ventana.geometry("300x300+100+100")
ventana2.geometry("180x125+450+350")
ventana2.title("Panel")     
ventana2.config(bg="#000000")


#Botones de inertaccion con la ventana de panel
aprender=Button(ventana2,text='Aprender',command=aprender,width=455).pack()
aprender=Button(ventana2,text='Analizar',command=analizar,width=455).pack()
aprender=Button(ventana2,text='Limpiar matriz',command=resetear_tabla,width=455).pack()
#Etiqueta para separar las acciones basicas de eliminar la memoria
Label(ventana2,text="-----------------------------------").pack()
aprender=Button(ventana2,text='Borrar memoria y cerrar',command=borrar_memoria,width=455).pack()

#Botones de la matriz
#5
button25=Button(ventana,text='25',command=core.veinticinco,bg="#FFFFFF")
button25.place(relx=0.73, rely=0.77, relwidth=0.13, relheight=0.15)
button24=Button(ventana,text='24',command=core.veinticuatro,bg="#FFFFFF")
button24.place(relx=0.58, rely=0.77, relwidth=0.13, relheight=0.15)
button23=Button(ventana,text='23',command=core.veintitres,bg="#FFFFFF")
button23.place(relx=0.43, rely=0.77, relwidth=0.13, relheight=0.15)
button22=Button(ventana,text='22',command=core.veintidos,bg="#FFFFFF")
button22.place(relx=0.28, rely=0.77, relwidth=0.13, relheight=0.15)
button21=Button(ventana,text='21',command=core.veintiuno,bg="#FFFFFF")
button21.place(relx=0.12, rely=0.77, relwidth=0.13, relheight=0.15)
#4
button20=Button(ventana,text='20',command=core.veinte,bg="#FFFFFF")
button20.place(relx=0.73, rely=0.60, relwidth=0.13, relheight=0.15)
button19=Button(ventana,text='19',command=core.diesinueve,bg="#FFFFFF")
button19.place(relx=0.58, rely=0.60, relwidth=0.13, relheight=0.15)
button18=Button(ventana,text='18',command=core.diesiocho,bg="#FFFFFF")
button18.place(relx=0.43, rely=0.60, relwidth=0.13, relheight=0.15)
button17=Button(ventana,text='17',command=core.diesisiete,bg="#FFFFFF")
button17.place(relx=0.28, rely=0.60, relwidth=0.13, relheight=0.15)
button16=Button(ventana,text='16',command=core.diesiseis,bg="#FFFFFF")
button16.place(relx=0.12, rely=0.60, relwidth=0.13, relheight=0.15)
#3
button15=Button(ventana,text='15',command=core.quince,bg="#FFFFFF")
button15.place(relx=0.73, rely=0.43, relwidth=0.13, relheight=0.15)
button14=Button(ventana,text='14',command=core.catorce,bg="#FFFFFF")
button14.place(relx=0.58, rely=0.43, relwidth=0.13, relheight=0.15)
button13=Button(ventana,text='13',command=core.trece,bg="#FFFFFF")
button13.place(relx=0.43, rely=0.43, relwidth=0.13, relheight=0.15)
button12=Button(ventana,text='12',command=core.doce,bg="#FFFFFF")
button12.place(relx=0.28, rely=0.43, relwidth=0.13, relheight=0.15)
button11=Button(ventana,text='11',command=core.once,bg="#FFFFFF")
button11.place(relx=0.12, rely=0.43, relwidth=0.13, relheight=0.15)
#2
diez = button10=Button(ventana,text='10',command=core.diez,bg="#FFFFFF")
button10.place(relx=0.73, rely=0.26, relwidth=0.13, relheight=0.15)
nueve = button9=Button(ventana,text='9',command=core.nueve,bg="#FFFFFF")
button9.place(relx=0.58, rely=0.26, relwidth=0.13, relheight=0.15)
ocho = button8=Button(ventana,text='8',command=core.ocho,bg="#FFFFFF")
button8.place(relx=0.43, rely=0.26, relwidth=0.13, relheight=0.15)
siete = button7=Button(ventana,text='7',command=core.siete,bg="#FFFFFF")
button7.place(relx=0.28, rely=0.26, relwidth=0.13, relheight=0.15)
seis = button6=Button(ventana,text='6',command=core.seis,bg="#FFFFFF")
button6.place(relx=0.12, rely=0.26, relwidth=0.13, relheight=0.15)
#1
cinco1 = button5=Button(ventana,text='5',command=core.cinco,bg="#FFFFFF")
button5.place(relx=0.73, rely=0.09, relwidth=0.13, relheight=0.15)
cuatro1 = button4=Button(ventana,text='4',command=core.cuatro,bg="#FFFFFF")
button4.place(relx=0.58, rely=0.09, relwidth=0.13, relheight=0.15)
tres1 = button3=Button(ventana,text='3',command=core.tres,bg="#FFFFFF")
button3.place(relx=0.43, rely=0.09, relwidth=0.13, relheight=0.15)
dos1 = button2=Button(ventana,text='2',command=core.dos,bg="#FFFFFF")
button2.place(relx=0.28, rely=0.09, relwidth=0.13, relheight=0.15)
uno1 = button1=Button(ventana,text='1',command=core.una,bg="#FFFFFF")
button1.place(relx=0.12, rely=0.09, relwidth=0.13, relheight=0.15)

#Arreglo con todos los botones
botones = [button1,button2,button3,button4,button5,button6,button7,button8,button9,button10,button11,button12,button13,button14,button15,button16,button17,button18,button19,button20,button21,button22,button23,button24,button25]

#Se inicializan las pantallas de interaccion
ventana2.mainloop()
ventana.mainloop()