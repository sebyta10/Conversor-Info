#COMVERSIONES MATEMÁTICAS
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

#PARA LA LONGITUD
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
#PARA LA ENERGIA



    
