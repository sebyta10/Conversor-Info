#CONVERSIONES MATEMÁTICAS
#PARA LA MASA
#Para convertir del SI(kg) a los demas sistemas:
def kg_a_g(valor):
    return valor*1000 #convierte de kilogramos a gramos

def kg_a_lb(valor):
    return valor*2.20462 #convierte de kilogramos a libras

def kg_a_utm(valor):
    return valor/ 9.80665 #convierte de kilogramos a utm

#Para convertir del CGS(g) a los demas sistemas:
def g_a_kg(valor):
    return valor/1000 #convierte de gramo a kilogramo

def g_a_lb(valor):
    return valor/453.592 #convierte de gramo a libras

def g_a_utm(valor):
    return valor/9806.65 #convierte de gramo a utm

#Para convertir del US(lb) a los demas sistemas:
def lb_a_kg(valor):
    return valor/2.20462 #convierte de libra a kilogramo

def lb_a_g(valor):
    return valor*453.592 #convierte de libra a gramo

def lb_a_utm(valor):
    return valor/21.6186 #convierte de libra a utm

#Para convertir de Técnico(utm) a los demas sistemas:
def utm_a_kg(valor):
    return valor*9.80665 #convierte de utm a kilogramo

def utm_a_g(valor):
    return valor*9806.65 #convierte de utm a gramo

def utm_a_lb(valor):
    return valor*21.6186 #convierte de utm a libra

#----------------------------------------------------

# PARA LA LONGITUD
# Para convertir del SI(m) a los demas sistemas:
def m_a_cm(valor):
    return valor * 100  #convierte de metros a centímetros

def m_a_ft(valor):
    return valor * 3.28084  #convierte de metros a pies

def m_a_in(valor):  # ← AQUÍ DEBE LLAMARSE EXACTAMENTE m_a_in
    return valor * 39.3701  #convierte de metros a pulgadas

# Para convertir del CGS(cm) a los demas sistemas:
def cm_a_m(valor):
    return valor / 100  #convierte de centímetros a metros

def cm_a_ft(valor):
    return valor / 30.48  #convierte de centímetros a pies

def cm_a_in(valor):  # ← AQUÍ DEBE LLAMARSE EXACTAMENTE cm_a_in
    return valor / 2.54  #convierte de centímetros a pulgadas

# Para convertir del US(ft) a los demas sistemas:
def ft_a_m(valor):
    return valor / 3.28084  #convierte de pies a metros

def ft_a_cm(valor):
    return valor * 30.48  #convierte de pies a centímetros

def ft_a_in(valor):  # ← AQUÍ DEBE LLAMARSE EXACTAMENTE ft_a_in
    return valor * 12  #convierte de pies a pulgadas

# Para convertir de Técnico(in) a los demas sistemas:
def in_a_m(valor):  # ← AQUÍ DEBE LLAMARSE EXACTAMENTE in_a_m
    return valor / 39.3701  #convierte de pulgadas a metros

def in_a_cm(valor):  # ← AQUÍ DEBE LLAMARSE EXACTAMENTE in_a_cm
    return valor * 2.54  #convierte de pulgadas a centímetros

def in_a_ft(valor):  # ← AQUÍ DEBE LLAMARSE EXACTAMENTE in_a_ft
    return valor / 12  #convierte de pulgadas a pies
#PARA LA FUERZA

# Conversión desde el SI (Newton) a los demás sistemas:
def N_a_dyn(valor):
    return valor * 100000  # convierte de Newton a dina

def N_a_lbf(valor):
    return valor / 4.44822  # convierte de Newton a libra-fuerza

def N_a_kp(valor):
    return valor / 9.80665  # convierte de Newton a kilopond

# Conversión desde CGS (dina):
def dyn_a_N(valor):
    return valor / 100000  # convierte de dina a Newton

def dyn_a_lbf(valor):
    return valor / 444822  # convierte de dina a lbf

def dyn_a_kp(valor):
    return valor / 980665  # convierte de dina a kp

# Conversión desde US (lbf):
def lbf_a_N(valor):
    return valor * 4.44822  # convierte de lbf a Newton

def lbf_a_dyn(valor):
    return valor * 444822  # convierte de lbf a dina

def lbf_a_kp(valor):
    return valor * 0.453592  # convierte de lbf a kilopond

# Conversión desde Técnico (kp):
def kp_a_N(valor):
    return valor * 9.80665  # convierte de kp a Newton

def kp_a_dyn(valor):
    return valor * 980665  # convierte de kp a dina

def kp_a_lbf(valor):
    return valor / 0.453592  # convierte de kp a lbf



#PARA LA FUERZA

# Conversión desde el SI (Newton) a los demás sistemas:
def N_a_dyn(valor):
    return valor * 100000  # convierte de Newton a dina

def N_a_lbf(valor):
    return valor / 4.44822  # convierte de Newton a libra-fuerza

def N_a_kp(valor):
    return valor / 9.80665  # convierte de Newton a kilopond

# Conversión desde CGS (dina):
def dyn_a_N(valor):
    return valor / 100000  # convierte de dina a Newton

def dyn_a_lbf(valor):
    return valor / 444822  # convierte de dina a lbf

def dyn_a_kp(valor):
    return valor / 980665  # convierte de dina a kp

# Conversión desde US (lbf):
def lbf_a_N(valor):
    return valor * 4.44822  # convierte de lbf a Newton

def lbf_a_dyn(valor):
    return valor * 444822  # convierte de lbf a dina

def lbf_a_kp(valor):
    return valor * 0.453592  # convierte de lbf a kilopond

# Conversión desde Técnico (kp):
def kp_a_N(valor):
    return valor * 9.80665  # convierte de kp a Newton

def kp_a_dyn(valor):
    return valor * 980665  # convierte de kp a dina

def kp_a_lbf(valor):
    return valor / 0.453592  # convierte de kp a lbf



#PARA LA TEMPERATURA
def kel_a_cel(valor):  # kelvin (K) a celsius (°C)
    return valor - 273.15  

def kel_a_fah(valor):  # kelvin (K) a Fahrenheit (°F)
    return (valor - 273.15) * 1.8 + 32

def cel_a_kel(valor):  # Celsius (°C) a Kelvin (K)
    return valor + 273.15

def cel_a_fah(valor):  # Celsius (°C) a Fahrenheit (°F)
    return valor * 1.8 + 32

def fah_a_cel(valor):  # Fahrenheit (°F) a Celsius (°C)
    return  (valor - 32) / 1.8

def fah_a_kel(valor):  # Fahrenheit (°F) a Kelvin (K)
    return  (valor - 32) / 1.8 + 273.15



#PARA LA ENERGIA

def jul_a_erg(valor):  # Julio (J) a Ergio (erg)
    return valor * 10000000

def jul_a_lbf(valor):
    return valor * 0.737562 # Julio (J) a Pie-libra (ft·lbf)

def jul_a_kpm(valor):   # Julio (J) a Kilopondímetro (kpm)
    return valor / 9.80665


def erg_a_jul(valor):  #Ergio (erg) a Julio (J)
    return valor / 10000000

def erg_a_lbf(valor):   #Ergio (erg) Pie-libra (ft·lbf)
    return valor / 13558179

def erg_a_kpm(valor):  #Ergio (erg) a Kilopondímetro (kpm)
    return valor / 98066500


def lbf_a_jul(valor):   #Pie-libra (ft·lbf) a Julio (J)
    return valor * 1.35582

def lbf_a_erg(valor):    #Pie-libra (ft·lbf) a Ergio (erg)
    return valor * 13558179

def lbf_a_kpm(valor):     #Pie-libra (ft·lbf) a Kilopondímetro (kpm)
    return valor * 0.138255


def kpm_a_jul(valor):    #Kilopondímetro (kpm) a Julio (J)
    return valor * 9.80665

def kpm_a_erg(valor):   #Kilopondímetro (kpm) a Ergio (erg)
    return valor * 98066500 

def kpm_a_lbf(valor):  #Kilopondímetro (kpm) a Pie-libra (ft·lbf)
    return valor * 7.23301 
