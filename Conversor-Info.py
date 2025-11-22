import tkinter as tk

#importamos la conversiones matemáticas del otro archivo.
#Para la magnitud masa:
from ConversionesMatematicas import(kg_a_g, kg_a_lb, kg_a_utm, g_a_kg, g_a_lb, g_a_utm, lb_a_kg,
                                    lb_a_g, lb_a_utm, utm_a_kg, utm_a_g, utm_a_lb,
#Para la magnitud longitud:
                                    m_a_cm, m_a_ft, m_a_in, cm_a_m, cm_a_ft, cm_a_in, 
                                    ft_a_m, ft_a_cm, ft_a_in, in_a_m, in_a_cm, in_a_ft)

#Para la magnitud fuerza:
#Para la magnitud temperatura:
#Para la magnitud energia:

ventana = tk.Tk()
ventana.title('Conversor-Info')
ventana.geometry('500x500')
ventana.config(bg='#000000') #063565

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
font=('Consolas', 10), fg='#FFFFFF', bg='#000000', justify='center')
texto_Ventprincipal.pack(pady=20)

texto_Ventprincipal2 = tk.Label(ventana, text= 'CONVERSOR-INFO', font=('Bauhaus 93', 25),
                                    fg='#FFFFFF', bg='#000000', justify='center')
texto_Ventprincipal2.pack(pady=5)


magnitud_actual = None      #Variable global que recuerda que magnitud esta seleccionada el el menu.

def seleccionar_magnitud(magnitud): #Guarda que magnitud se eligio y muestra la interfaz del conversor.
    global magnitud_actual
    magnitud_actual = magnitud
    texto_Ventprincipal.pack_forget()
    texto_Ventprincipal2.pack_forget()

    if magnitud == 'Masa':
        texto_unidades.config(text='kg              g               lb              utm')

    elif magnitud == 'Longitud':
        texto_unidades.config(text='m               cm              ft              in')

    elif magnitud == 'Fuerza':
        texto_unidades.config(text='N               dyn             lbf             kp')

    elif magnitud == 'Temperatura':
        texto_unidades.config(text='K               °C              °F              °C')

    elif magnitud == 'Energia':
        texto_unidades.config(text='J              erg            ft.lb              Kpm')

    Contenedor_principal.pack(pady=20)

sistema_seleccionado = None #Variable global que recuerda el boton de sistema fue seleccionado

def seleccionar_sistema(sistema):      #Guarda que boton de sistema fue seleccionado
    global sistema_seleccionado
    sistema_seleccionado = sistema

#Funciones que conectan los botones con el archivo de conversionesmatematicas.py
#Realiza el calculo y muestra los resultados. Utilizamos condicionales.
def convertir_valor():
    try:
        valor = float(display.get())  # Lee el valor ingresado en el display

        if magnitud_actual == 'Masa':  # Verifica que magnitud se seleccionó

            if valor < 0:
                area_resultados.config(text='Error la masa no puede ser negativa')
                return
            
            if sistema_seleccionado is None:  # Verifica que se seleccionó un sistema.
                area_resultados.config(text='Selecciona un sistema primero')
                return
            
            if sistema_seleccionado == "SI":  # Hace las conversiones según el sistema seleccionado
                resultado_g = kg_a_g(valor)   # Convierte de Kilogramos a las demás unidades
                resultado_lb = kg_a_lb(valor)
                resultado_utm = kg_a_utm(valor)

                resultados = [
                    f'SI:{valor} kg',
                    f'CGS:{resultado_g:.3f} g',
                    f'US:{resultado_lb:.3f} lb',
                    f'Téc: {resultado_utm:.3f} utm'
                ]
                texto_resultados = '\n'.join(resultados)

            elif sistema_seleccionado == "CGS":
                resultado_kg = g_a_kg(valor)  # Convierte de gramos a las demás unidades
                resultado_lb = g_a_lb(valor)
                resultado_utm = g_a_utm(valor)

                resultados = [
                    f'SI:{resultado_kg:.3f} kg',
                    f'CGS:{valor} g',
                    f'US:{resultado_lb:.3f} lb',
                    f'Téc: {resultado_utm:.3f} utm'
                ]
                texto_resultados = '\n'.join(resultados)

            elif sistema_seleccionado == "US":
                resultado_kg = lb_a_kg(valor)  # Convierte de libras a las demás unidades
                resultado_g = lb_a_g(valor)
                resultado_utm = lb_a_utm(valor)

                resultados = [
                    f'SI:{resultado_kg:.3f} kg',
                    f'CGS:{resultado_g:.3f} g',
                    f'US:{valor} lb',
                    f'Téc: {resultado_utm:.3f} utm'
                ]
                texto_resultados = '\n'.join(resultados)
            
            elif sistema_seleccionado == "Téc":
                resultado_kg = utm_a_kg(valor)  # Convierte de utm a las demás unidades
                resultado_g = utm_a_g(valor)
                resultado_lb = utm_a_lb(valor)

                resultados = [
                    f'SI:{resultado_kg:.3f} kg',
                    f'CGS:{resultado_g:.3f} g',
                    f'US:{resultado_lb:.3f} lb',
                    f'Téc: {valor} utm'
                ]
                texto_resultados = '\n'.join(resultados)

            area_resultados.config(text=texto_resultados)

        elif magnitud_actual == "Longitud":

            if sistema_seleccionado is None:
                area_resultados.config(text='Selecciona un sistema primero')
                return

            if sistema_seleccionado == "SI":
                resultado_cm = m_a_cm(valor)
                resultado_ft = m_a_ft(valor)
                resultado_in = m_a_in(valor)

                resultados = [
                    f'SI:{valor} m',
                    f'CGS:{resultado_cm:.2f} cm',
                    f'US:{resultado_ft:.2f} ft',
                    f'Téc: {resultado_in:.2f} in'
                ]
                texto_resultados = "\n".join(resultados)

            elif sistema_seleccionado == "CGS":
                resultado_m = cm_a_m(valor)
                resultado_ft = cm_a_ft(valor)
                resultado_in = cm_a_in(valor)

                resultados = [
                    f'SI:{resultado_m:.4f} m',
                    f'CGS:{valor} cm',
                    f'US:{resultado_ft:.4f} ft',
                    f'Téc: {resultado_in:.2f} in'
                ]
                texto_resultados = '\n'.join(resultados)

            elif sistema_seleccionado == "US":
                resultado_m = ft_a_m(valor)
                resultado_cm = ft_a_cm(valor)
                resultado_in = ft_a_in(valor)

                resultados = [
                    f'SI:{resultado_m:.4f} m',
                    f'CGS:{resultado_cm:.2f} cm',
                    f'US:{valor} ft',
                    f'Téc: {resultado_in:.2f} in'
                ]
                texto_resultados = '\n'.join(resultados)
            
            elif sistema_seleccionado == "Téc":
                resultado_m = in_a_m(valor)
                resultado_cm = in_a_cm(valor)
                resultado_ft = in_a_ft(valor)

                resultados = [
                    f'SI:{resultado_m:.4f} m',
                    f'CGS:{resultado_cm:.2f} cm',
                    f'US:{resultado_ft:.4f} ft',
                    f'Téc: {valor} in'
                ]
                texto_resultados = '\n'.join(resultados)

            area_resultados.config(text=texto_resultados)

        elif magnitud_actual == 'Fuerza':

            if sistema_seleccionado is None:
                area_resultados.config(text='Selecciona un sistema primero')
                return

            if sistema_seleccionado == "SI":
                resultado_dyn = N_a_dyn(valor)
                resultado_lbf = N_a_lbf(valor)
                resultado_kp = N_a_kp(valor)

                resultados = [
                    f'SI:{valor} N',
                    f'CGS:{resultado_dyn:.3f} dyn',
                    f'US:{resultado_lbf:.3f} lbf',
                    f'Téc:{resultado_kp:.3f} kp'
                ]
                texto_resultados = '\n'.join(resultados)

            elif sistema_seleccionado == "CGS":
                resultado_N = dyn_a_N(valor)
                resultado_lbf = dyn_a_lbf(valor)
                resultado_kp = dyn_a_kp(valor)

                resultados = [
                    f'SI:{resultado_N:.3f} N',
                    f'CGS:{valor} dyn',
                    f'US:{resultado_lbf:.3f} lbf',
                    f'Téc:{resultado_kp:.3f} kp'
                ]
                texto_resultados = '\n'.join(resultados)

            elif sistema_seleccionado == "US":
                resultado_N = lbf_a_N(valor)
                resultado_dyn = lbf_a_dyn(valor)
                resultado_kp = lbf_a_kp(valor)

                resultados = [
                    f'SI:{resultado_N:.3f} N',
                    f'CGS:{resultado_dyn:.3f} dyn',
                    f'US:{valor} lbf',
                    f'Téc:{resultado_kp:.3f} kp'
                ]
                texto_resultados = '\n'.join(resultados)

            elif sistema_seleccionado == "Téc":
                resultado_N = kp_a_N(valor)
                resultado_dyn = kp_a_dyn(valor)
                resultado_lbf = kp_a_lbf(valor)

                resultados = [
                    f'SI:{resultado_N:.3f} N',
                    f'CGS:{resultado_dyn:.3f} dyn',
                    f'US:{resultado_lbf:.3f} lbf',
                    f'Téc:{valor} kp'
                ]
                texto_resultados = '\n'.join(resultados)

            area_resultados.config(text=texto_resultados)

    except ValueError:
        area_resultados.config(text="Error. Ingrese número válido")

        
def volver_a_principal():
    global sistema_seleccionado
    sistema_seleccionado = None
    display.delete(0, tk.END)
    area_resultados.config(text='')
    Contenedor_principal.pack_forget()
    texto_Ventprincipal.pack(pady=20)
    texto_Ventprincipal2.pack(pady=5)


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

Contenedor_principal = tk.Frame(ventana, bg='#2D2D2D', relief='raised', bd=5) #Contenedor donde van los elementos del conversor.
                                                                     
display = tk.Entry(Contenedor_principal, font=('Courier New', 20, 'bold'), #Display deonde ingresamos el valor numérico.
                   justify='right',
                   width=20, relief='sunken', bd=3,
                   bg='#001100', fg='#00FF00', 
                   insertbackground='#00FF00')
display.pack(pady=25)

texto_unidades = tk.Label(Contenedor_principal, text='', font=('Consolas', 9), #Texto vacio indica que unidades utiliza cada sistema.
                          fg="#000000",bg='#2D2D2D')
texto_unidades.pack(pady=2)

Contenedor_botones_sistema = tk.Frame(Contenedor_principal, bg='#2D2D2D') #Contenedor para los botones de sistemas.
Contenedor_botones_sistema.pack(pady=5)

botones_sistema = []                #Se crea una lista de los botones de seleccion de sistemas.
sistemas = ['SI', 'CGS', 'US', 'Téc']

for i, sistema in enumerate(sistemas):
    boton = tk.Button(Contenedor_botones_sistema, text=sistema, bg='#FF9900',
    fg='#000000', relief='raised', bd=2, font=('Arial', 10, 'bold'),
    activebackground='#FFAA33', activeforeground='#000000', width=10,
    command=lambda s=sistema: seleccionar_sistema(s))

    boton.grid(row=0, column=i, padx=5, pady=5)
    botones_sistema.append(boton)


boton_convertir = tk.Button(Contenedor_principal, text='CONVERTIR',      #Boton de convertir
                            bg='#FF9900', fg='#000000',
                            relief='raised', bd=2,
                            font=('Arial', 12, 'bold'),
                            activebackground='#FFAA33',
                            activeforeground='#000000',
                            width=15,
                            command=convertir_valor)
boton_convertir.pack(pady=10)



area_resultados = tk.Label(Contenedor_principal, bg='#001100', #Area de resultados
                           fg='#00FF00', relief='sunken',
                           bd=3, font=('Courier New', 12, 'bold'),
                           width=30, height=6, justify='left',
                           anchor='nw')
area_resultados.pack(pady=10)

Contenedor_principal.pack_forget() #Oculta la interfaz del conversor al inicio del programa.

boton_volver = tk.Button(Contenedor_principal, text='Volver', 
                         command=volver_a_principal,
                         bg='#FF0000', fg='#FFFFFF',
                         relief='raised', bd=2,
                         font=('Arial', 10, 'bold'), width=10)
boton_volver.pack(pady=10)

ventana.mainloop()
