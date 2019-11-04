
# coding: utf-8

# In[1]:


import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import keyboard
from pygame import mixer
import time

# Dependencias são das libs keyboard e da pygame


# In[2]:


mixer.init()

print('=============== COMANDOS ==============='
      '\n 1 - LER DESCRIÇÃO GRÁFICO 1'
      '\n 2 - LER DESCRIÇÃO GRÁFICO 2'
      '\n S - SAIR')


while True:  # Um loop que vai rodar até que se pressione a tecla "q"

    if keyboard.is_pressed('s'):  # Se pressionar a tecla q o programa fecha
        print('SAINDO')
        break  # finishing the loop

    if keyboard.is_pressed('1'):  # Se pressionar a tecla a
        print("TECLA 1 PRESSIONADA - LER DESCRIÇÃO GRÁFICO 1") # Printa algo pra identificar
        mixer.music.load("C:\\Users\\labvis\\Documents\\Dissertacao\\Morash\\Simples.mp3")  # Toca esse MP3
        mixer.music.play()
        time.sleep(0.5) # Isso aqui é só pra debouncing, evitar que cada tecla seja pressionada varias vezes enquanto não soltar a tecla

    if keyboard.is_pressed('2'):  # Se pressionar a tecla b
        print("TECLA 2 PRESSIONADA - LER DESCRIÇÃO GRÁFICO 2")  # Printa algo pra identificar
        mixer.music.load("C:\\Users\\labvis\\Documents\\Dissertacao\\Morash\\Agrupadas.mp3")  # Toca esse MP3
        mixer.music.play()
        time.sleep(0.5) # Isso aqui é só pra debouncing, evitar que cada tecla seja pressionada varias vezes enquanto não soltar a tecla
        


# In[ ]:



