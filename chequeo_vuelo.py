# --- SISTEMA DE ALERTA DE CABINA ---
def revisar_sistema():
    combustible = 15 
    if combustible < 20:
        print("¡ALERTA CRÍTICA! Combustible bajo.")
    else:
        print("Vuelo seguro.")

revisar_sistema()
