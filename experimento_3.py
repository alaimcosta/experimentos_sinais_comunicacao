"""
UNIVERSIDADE FEDERAL DO SUL E SUDESTE DO PARA
FACULDADE DE ENGENHARIA DA COMPUTAÇÃO
Disciplina: Téoria das comunicações
Prof(a). Dra. Cindy Stella Fernandes
Equipe: Alaim de Jesus Leão Costa; Henrique Pereira Viana; Klauber Araujo Sousa
Experimento: Efeito rsr no sinal de áudio
"""

from IPython.display import Audio
import numpy as np
import sounddevice as sd
import soundfile as sf
import math 


nPower = 0.0001
temp_Rep = 20 # acima desse valor ultrapassa o limite da matriz criada
arquivoAudio = 'boate_azul.wav'

[data, taxaAmost] = sf.read(arquivoAudio) #Faz a leitura do arquivo de audio e reorna a taxa de amostragem e um array dos dados

n = math.sqrt(nPower)*np.random.randn(temp_Rep*taxaAmost, 1) #calculo a raiz quadrada de nPower e multiplico por randn que criar numeros aleatorios em uma matriz n por 1

#data = data*temp_Rep

#sinalRuido = data*n

sd.play(data, taxaAmost) # Reproduz o arquivo de audio original
status = sd.wait() # Aguarda o arquivo terminar de reproduzir 

#sd.play(sinalRuido, taxaAmost)
#status = sd.wait() # Aguarda o arquivo terminar de reproduzir 
