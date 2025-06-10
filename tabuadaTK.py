import tkinter as tk

janela = tk.Tk()
janela.title('Minha tabuada!')
janela.geometry('300x500')

def tabuada():
    numero = int(entrada.get())
    for t in range(1, 11):
        resultado = tk.Label(janela, text=(f'{t} x {numero} = {t*numero}'), font=('Arial', 10))
        resultado.pack(pady=6)
    return

titulo = tk.Label(janela, text='Tabuada!', font=('Arial', 12, 'bold'))
titulo.pack(pady=10)

instrução = tk.Label(janela, text='Digite um número:', font=('Arial', 10))
instrução.pack()

entrada = tk.Entry(janela, width=4, justify=tk.CENTER)
entrada.pack(pady=4, anchor='center')

botao = tk.Button(janela, text='Calcular', width=7, bg='LightBlue', command=tabuada)
botao.pack(pady=4)

janela.mainloop()