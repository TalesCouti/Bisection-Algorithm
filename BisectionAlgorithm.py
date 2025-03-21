import math
from openpyxl import Workbook

# Criação do arquivo Excel
import math
import openpyxl

# Função a ser analisada
def f(x):
    return x**2 + math.log(x)

# Cria o arquivo Excel e a aba ativa
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Resultados Bissecção"

# Cabeçalhos da planilha
ws.append(["Iteração", "x", "a", "b", "f(a)", "f(b)", "f(x)", "Sinal", "Erro"])

# Parâmetros iniciais
a = 0.1 
b = 5 
i = 1 

while b - a > 0.01:  # Precisão desejada
    x = (a + b) / 2
    fa = f(a)
    fb = f(b)
    fx = f(x)
    erro = abs(b - a)
    
    # Determinação do sinal
    if fa * fx < 0:
        sinal = "Negativo"
        b = x
    else:
        sinal = "Positivo"
        a = x

    # Adiciona a linha atual na planilha
    ws.append([i, x, a, b, fa, fb, fx, sinal, erro])

    i += 1

# Salva o arquivo Excel
wb.save("bisseccao_resultados.xlsx")
print(f"Arquivo 'bisseccao_resultados.xlsx' salvo com sucesso.")
