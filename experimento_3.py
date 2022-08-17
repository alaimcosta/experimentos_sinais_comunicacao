"""
UNIVERSIDADE FEDERAL DO SUL E SUDESTE DO PARA
FACULDADE DE ENGENHARIA DA COMPUTAÇÃO
Disciplina: Téoria das comunicações
Prof(a). Dra. Cindy Stella Fernandes
Equipe: Alaim de Jesus Leão Costa; Henrique Pereira Viana; Klauber Araujo Sousa
Experimento: Efeito rsr no sinal de áudio
"""

from array import array
from IPython.display import Audio
from statistics import median
import numpy as np
import sounddevice as sd
import soundfile as sf
import math



nPower = 0.0001
temp_Rep = 10 # acima desse valor ultrapassa o limite da matriz criada
arquivoAudio = 'boate_azul.wav'

data, taxaAmost = sf.read(arquivoAudio) #Faz a leitura do arquivo de audio e reorna a taxa de amostragem e um array dos dados

data = data[0:temp_Rep*taxaAmost, 0]

n = math.sqrt(nPower)*np.random.randn(temp_Rep*taxaAmost) #calculo a raiz quadrada de nPower e multiplico por randn que cria amostras pade distribuição padrão

sinalArr = np.around(data)

data_edit = data + n

Ps = np.mean(data**2) # potencia de interesse do sinal de áudio
Pn = np.var(n) # variancia dos valores de n que representam a potencia de ruído do sinal
RSR = Ps/Pn

print("Valor de relação sinal ruído", RSR)


sd.play(data, taxaAmost) # Reproduz o arquivo de audio original
status = sd.wait() # Aguarda o arquivo terminar de reproduzir 

sd.play(data_edit, taxaAmost)
status = sd.wait() 