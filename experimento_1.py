"""
UNIVERSIDADE FEDERAL DO SUL E SUDESTE DO PARA
FACULDADE DE ENGENHARIA DA COMPUTAÇÃO
Disciplina: Téoria das comunicações
Prof(a). Dra. Cindy Stella Fernandes
Equipe: Alaim de Jesus Leão Costa; Henrique Pereira Viana; Klauber Araujo Sousa
Experimento: Modificações causadas pela canal
"""
import math, numpy
from cmath import sqrt
from scipy import signal
import matplotlib.pyplot as plot
import numpy as np

sinalGerado = numpy.linspace(0, 5, 100) # Gerado uma sequencia numerica
sinalOrigi = numpy.array([1 if math.floor(2 * t) % 2 == 0 else 0 for t in sinalGerado]) # retorna um array de zeros e uns, floor(arredendo para baixo um inteiro mais proximo)

numP = 0.1
tipoInterf = 0  # 0 - ruido no sinal
                # 1 - atenuação
                # 2 - distorção    
match tipoInterf:
    case 0:
        matAleat = np.random.randn(len(sinalOrigi)) # retorna uma matriz de n posições e preenchida com valores aleatorios
        x = sinalOrigi + sqrt(numP)*matAleat # saída é a soma do sinal original com o sinal aleatória * a raiz quadrada de numP
    case 1:
        x = sinalOrigi * 0.5 # função que ira atenuar o sinal
    case 2:
        respImpul = 0.4*np.array([0.2, 0.3, 0.5, 0.4, 0.35, 0.31, 0.27]) #gerador de sinal
        x = np.convolve(sinalOrigi.astype(float), respImpul) #realiza a convolução do sinal gerado com o sinal original

plot.plot(sinalOrigi,'b', label='Sinal Original') # exibe o sinal original
plot.plot(x,'r--', label='Sinal Modificado') # sinal com algum tipo de anomalia
plot.xlabel('Tempo')
plot.ylabel('Amplitude')
plot.title('Modificações do canal')
plot.legend(loc=2) # posição da legenda
plot.ylim(-0.5, 1.5) # especifica as metricas de plotagem do gráfico
plot.axhline(y = 0, color = 'k') # linha horizontal no gráfico
plot.grid()
plot.show()