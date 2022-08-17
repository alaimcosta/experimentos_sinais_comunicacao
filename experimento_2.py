"""
UNIVERSIDADE FEDERAL DO SUL E SUDESTE DO PARA
FACULDADE DE ENGENHARIA DA COMPUTAÇÃO
Disciplina: Téoria das comunicações
Prof(a). Dra. Cindy Stella Fernandes
Equipe: Alaim de Jesus Leão Costa; Henrique Pereira Viana; Klauber Araujo Sousa
Experimento: Quantização de sinal de áudio
"""
import numpy as np
import matplotlib . pyplot as plt
import soundfile as sf

date, taxaAmost = sf.read('boate_azul.wav') # retorna a taxa de amostragem e um array dos dados
tempResp = 20
date = date[0:tempResp*taxaAmost, 0]  # multiplica a amostragem pelo tempo de resposta, na posição inicial do vetor

"""
Digitalização do Sinal
"""
#print("maximo", max(date))
valorQuat = (max(date)-min(date)) #Pico a Pico do Sinal
b=4 #Quantidade de Bits do Sinal
niveis=2**b #Quantidade de Niveis de Quantização
delta = valorQuat/(niveis-1) # Passo do quantizador, especifica a largura do nivel de Quantização
sinalAmostrado = date/delta 
sinalArr = np.around(sinalAmostrado)

"""
Plot do Sinal de Entrada e do Sinal Digitalizado
"""
plt.plot(8*date[18000:20000], 'b', label=' Original') # dados do arquivo de áudio
plt.plot(sinalArr[18000:20000], 'r--', label=' Quantizado')
plt.title ('Sinal Quantizado ')
plt.ylabel (" Amplitude do Sinal ") 
plt.xlabel (" Tempo ") 
plt.legend(loc=2)
plt.grid ()
plt.show()


