import tkinter as tk

def agregar_caracter(caracter):
    entrada.insert(tk.END, caracter)

def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except Exception as e:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Error")

def limpiar():
    entrada.delete(0, tk.END)


ventana = tk.Tk()
ventana.title("Calculadora2.0")


entrada = tk.Entry(ventana, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
entrada.grid(row=0, column=0, columnspan=4)


botones = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

fila = 1
columna = 0

for boton in botones:
    if boton == 'C':
        tk.Button(ventana, text=boton, width=5, height=2, command=limpiar).grid(row=fila, column=columna)
    elif boton == '=':
        tk.Button(ventana, text=boton, width=5, height=2, command=calcular).grid(row=fila, column=columna)
    else:
        tk.Button(ventana, text=boton, width=5, height=2, command=lambda b=boton: agregar_caracter(b)).grid(row=fila, column=columna)
    
    columna += 1
    if columna > 3:
        columna = 0
        fila += 1

ventana.mainloop()
