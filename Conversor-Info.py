import tkinter as tk

#importamos la conversiones matemáticas del otro archivo.
#Para la magnitud masa:
from ConversionesMatematicas import(kg_a_g, kg_a_lb, kg_a_utm, g_a_kg, g_a_lb, g_a_utm, lb_a_kg,
                                    lb_a_g, lb_a_utm, utm_a_kg, utm_a_g, utm_a_lb)

#Para la magnitud longitud:
#Para la magnitud fuerza:
#Para la magnitud temperatura:
#Para la magnitud energia:

ventana = tk.Tk()
ventana.title('Conversor-Info')
ventana.geometry('500x400')
ventana.config(bg='#063565')

texto_Ventprincipal = tk.Label(ventana, 
                               text='''                   
                   ...                  
                .........               
              .....   .....             
             ..   .. ..   ..            
            ... .... .... ...           
           ...  .... ....  ...          
          ...  ..... .....  ...         
         .... ..  .. ..  .. ...         
         ... ... ... .. .... ...        
        ... ... .... .. ..... ...       
       ...  .. ..... .. .....  ...      
      ...  ..  ..... .. ... ..  ...     
     ...  ..  ...... .. ... ... ....    
    .... ...  ...... .. ...  ... ...    
    ... ........     .. .... ...  ...   
    .....   ........ ..  ..   .......   
     .............   ..  ...........    
           ............ ......          
                   ..                   
''',
font=('Consolas', 8), fg='#FFFFFF', bg='#063565', justify='center')
texto_Ventprincipal.pack(pady=20)


magnitud_actual = None      #Variable global que recuerda que magnitud esta seleccionada el el menu.

def seleccionar_magnitud(magnitud): #Guarda que magnitud se eligio y muestra la interfaz del conversor.
    global magnitud_actual
    magnitud_actual = magnitud
    texto_Ventprincipal.pack_forget()
    frame_principal.pack(pady=20)

sistema_seleccionado = None #Variable global que recuerda el boton de sistema fue seleccionado

def seleccionar_sistema(sistema):      #Guarda que boton de sistema fue seleccionado
    global sistema_seleccionado
    sistema_seleccionado = sistema
    print(f'Sistema seleccionado: {sistema}')

#Funciones que conectan los botones con el archivo de conversionesmatematicas.py
#Realiza el calculo y muestra los resultados. Utilizamos condicionales.
#Para la magnitud masa seria:
def convertir_valor():
    try:
        valor = float(display.get()) #Lee el valor ingresado en el display

        if magnitud_actual =='Masa': #Verifica que magnitud se selecciono

            if valor<0:
                area_resultados.config(text='Error la masa no puede ser negativa')
                return
        
        if sistema_seleccionado is None: #Verificaca que se seleccionó un sistema.
            area_resultados.config(text='Selecciona un sistema primero')
            return
        
        if sistema_seleccionado == "SI": #Hace las conversiones segun el sistema seleccionado
            resultado_g = kg_a_g(valor)  #Convierte de Kilogramos a las demas unidades
            resultado_lb = kg_a_lb(valor)
            resultado_utm = kg_a_utm(valor)

            resultados = [
                f'SI:{valor} kg',
                f'CGS:{resultado_g:.2f} g',
                f'US:{resultado_lb:.2f} lb',
                f'Téc: {resultado_utm:.4f} utm'
            ]
            texto_resultados = '\n'.join(resultados)

        elif sistema_seleccionado == "CGS":
            resultado_kg = g_a_kg(valor)  #Convierte de gramos a las demas unidades
            resultado_lb = g_a_lb(valor)
            resultado_utm = g_a_utm(valor)

            resultados = [
                f'SI:{resultado_kg:.4f} kg',
                f'CGS:{valor} g',
                f'US:{resultado_lb:.4f} lb',
                f'Téc: {resultado_utm:.6f} utm'

            ]
            texto_resultados = '\n'.join(resultados)

        elif sistema_seleccionado == "US":
            resultado_kg = lb_a_kg(valor)  #Convierte de libras a las demas unidades
            resultado_g = lb_a_g(valor)
            resultado_utm = lb_a_utm(valor)

            resultados = [
                f'SI:{resultado_kg:.4f} kg',
                f'CGS:{resultado_g:.2f} g',
                f'US:{valor} lb',
                f'Téc: {resultado_utm:.4f} utm'

            ]
            texto_resultados = '\n'.join(resultados)
        
        elif sistema_seleccionado == "Téc":
            resultado_kg = utm_a_kg(valor)  #Convierte de utm a las demas unidades
            resultado_g = utm_a_g(valor)
            resultado_lb = utm_a_lb(valor)

            resultados = [
                f'SI:{resultado_kg:.4f} kg',
                f'CGS:{resultado_g:.2f} g',
                f'US:{resultado_lb:.2f} lb',
                f'Téc: {valor} utm'

            ]
            texto_resultados = '\n'.join(resultados)

        area_resultados.config(text=texto_resultados)
        
    except ValueError:
        area_resultados.config(text="Error. Ingrese número válido")


barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

menu_principal = tk.Menu(barra_menu)
barra_menu.add_cascade(label =
'Magnitudes', menu=menu_principal)

submenu = tk.Menu(menu_principal)
menu_principal.add_cascade(label =
'Opciones', menu=submenu)

submenu.add_command(label = 'Masa', command=lambda: seleccionar_magnitud('Masa'))
submenu.add_command(label = 'Longitud', command=lambda: seleccionar_magnitud('Longitud'))
submenu.add_command(label = 'Fuerza', command=lambda: seleccionar_magnitud('Fuerza'))
submenu.add_command(label = 'Temperatura', command=lambda: seleccionar_magnitud('Temperatura'))
submenu.add_command(label = 'Energia', command=lambda: seleccionar_magnitud('Energia'))

frame_principal = tk.Frame(ventana, bg='#2D2D2D', relief='raised', bd=5) #Contenedor donde van los elementos del conversor.
                                                                     
display = tk.Entry(frame_principal, font=('Arial', 18, 'bold'), #Display deonde ingresamos el valor numérico.
                   justify='right',
                   width=20, relief='sunken', bd=3,
                   bg='#001100', fg='#00FF00', 
                   insertbackground='#00FF00')
display.pack(pady=20)

frame_botones_sistema = tk.Frame(frame_principal, bg='#2D2D2D') #Contenedor para los botones de sistemas.
frame_botones_sistema.pack(pady=10)

botones_sistema = []                #Se crea una lista de los botones de seleccion de sistemas.
sistemas = ['SI', 'CGS', 'US', 'Téc']

for i, sistema in enumerate(sistemas):
    boton = tk.Button(frame_botones_sistema, text=sistema, bg='#FF9900',
    fg='#000000', relief='raised', bd=2, font=('Arial', 10, 'bold'),
    activebackground='#FFAA33', activeforeground='#000000', width=10,
    command=lambda s=sistema: seleccionar_sistema(s))

    boton.grid(row=0, column=i, padx=5, pady=5)
    botones_sistema.append(boton)


boton_convertir = tk.Button(frame_principal, text='CONVERTIR',      #Boton de convertir
                            bg='#FF9900', fg='#000000',
                            relief='raised', bd=2,
                            font=('Arial', 12, 'bold'),
                            activebackground='#FFAA33',
                            activeforeground='#000000',
                            width=15)
boton_convertir.pack(pady=10)

area_resultados = tk.Label(frame_principal, bg='#FFFFFF', #Area de resultados
                           fg='#000000', relief='sunken',
                           bd=3, font=('Courier New', 12),
                           width=30, height=6, justify='left',
                           anchor='nw')

area_resultados.pack(pady=10)

frame_principal.pack_forget() #Oculta la interfaz del conversor al inicio del programa.

boton_convertir.config(command=convertir_valor) #Conecta el boton convertir con las funciones que hacen los calculos.


ventana.mainloop()