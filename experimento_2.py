"""
UNIVERSIDADE FEDERAL DO SUL E SUDESTE DO PARA
FACULDADE DE ENGENHARIA DA COMPUTAÇÃO
Disciplina: Téoria das comunicações
Prof(a). Dra. Cindy Stella Fernandes
Equipe: Alaim de Jesus Leão Costa; Henrique Pereira Viana; Klauber Araujo Sousa
Experimento: Quantização de sinal de áudio
"""
import numpy as np
from scipy.io import wavfile
import matplotlib . pyplot as plt
import soundfile as sf


[date, taxaAmost] = sf.read('boate_azul.wav') # retorna a taxa de amostragem e um array dos dados


plt.plot(date[18000:20000]) # dados do arquivo de áudio
plt.title (" Sinal de Entrada ")
plt.ylabel (" Amplitude do Sinal ") 
plt.xlabel (" Tempo ") 
plt.grid ()
plt.show()


"""
Caracteristicas de Quantização
"""


PP = 2
#PP = max([date])-min([date]); #Pico a Pico do Sinal
b=1 #Quantidade de Bits do Sinal
L=2**b #Quantidade de Niveis de Quantização
v= PP/(L-1) #Largura de Niveis de Quantização


np.logical_and(min([date]),max([date]))

n = np.linspace(min([date]),max([date])+v, num=v, dtype='float') #Niveis de quantização, v é  passo 



"""
Digitalização do Sinal
"""

digita = np.zeros(len(date))

for i in range (len(date)):
    for j in range (L):
        if date[i]>=n[j] and date[i]<=n[j+1]:
            digita[i]=n[j]
            


"""
Plot do Sinal de Entrada e do Sinal Digitalizado
"""

plt.plot(date[17000:20000], 'r --')
#plt.plot(digita)
plt.title ('Sinal Quantizado a uma Taxa de % bits ')
plt.ylabel (" Amplitude do Sinal ") 
plt.xlabel (" Tempo ") 
plt.grid ()
plt.show()


