
# coding: utf-8

# In[9]:


import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import keyboard
from pygame import mixer
import time

# Dependencias são das libs keyboard e da pygame


# In[12]:


mixer.init()

print('=============== COMANDOS ==============='
      '\n D - LER DESCRIÇÃO COMPLETA'
      '\n C - LER CATEGORIA'
      '\n L - LER LEGENDA DO GRÁFICO'
      '\n Y - LER LEGENDA DO EIXO Y'
      '\n X - LER LEGENDA DO EIXO X'
      '\n G - LER GRUPOS E SÉRIES'
      '\n M - LER VALORES DE MÍNIMO E MÁXIMO'
      '\n 1 - LER DADOS DO 1º GRUPO'
      '\n 2 - LER DADOS DA 2º GRUPO'
      '\n 3 - LER DADOS DA 3º GRUPO'
      '\n E - LER MÉDIA E DESVIO PADRÃO'
      '\n S - SAIR')


while True:  # Um loop que vai rodar até que se pressione a tecla "q"

    if keyboard.is_pressed('s'):  # Se pressionar a tecla q o programa fecha
        print('SAINDO')
        break  # finishing the loop

    if keyboard.is_pressed('c'):  # Se pressionar a tecla a
        print("TECLA C PRESSIONADA - LER CATEGORIA") # Printa algo pra identificar
        mixer.music.load("C:\\Users\\labvis\\Documents\\Dissertacao\\Mod_Todos\\Por_partes\\Agrupadas\\1.cat.mp3")  # Toca esse MP3
        mixer.music.play()
        time.sleep(0.5) # Isso aqui é só pra debouncing, evitar que cada tecla seja pressionada varias vezes enquanto não soltar a tecla

    if keyboard.is_pressed('l'):  # Se pressionar a tecla b
        print("TECLA L PRESSIONADA - LER LEGENDA DO GRÁFICO")  # Printa algo pra identificar
        mixer.music.load("C:\\Users\\labvis\\Documents\\Dissertacao\\Mod_Todos\\Por_partes\\Agrupadas\\2.legenda.mp3")  # Toca esse MP3
        mixer.music.play()
        time.sleep(0.5) # Isso aqui é só pra debouncing, evitar que cada tecla seja pressionada varias vezes enquanto não soltar a tecla
        
    if keyboard.is_pressed('y'):  # Se pressionar a tecla b
        print("TECLA Y PRESSIONADA - LER LEGENDA DO EIXO Y")  # Printa algo pra identificar
        mixer.music.load("C:\\Users\\labvis\\Documents\\Dissertacao\\Mod_Todos\\Por_partes\\Agrupadas\\3.eixo y.mp3")  # Toca esse MP3
        mixer.music.play()
        time.sleep(0.5)    
        
    if keyboard.is_pressed('x'):  # Se pressionar a tecla b
        print("TECLA X PRESSIONADA - LER LEGENDA DO EIXO X")  # Printa algo pra identificar
        mixer.music.load("C:\\Users\\labvis\\Documents\\Dissertacao\\Mod_Todos\\Por_partes\\Agrupadas\\4.eixo x.mp3")  # Toca esse MP3
        mixer.music.play()
        time.sleep(0.5)
        
    if keyboard.is_pressed('g'):  # Se pressionar a tecla b
        print("TECLAS G PRESSIONADA - LER GRUPOS E SÉRIES")  # Printa algo pra identificar
        mixer.music.load("C:\\Users\\labvis\\Documents\\Dissertacao\\Mod_Todos\\Por_partes\\Agrupadas\\5.grupos_series.mp3")  # Toca esse MP3
        mixer.music.play()
        time.sleep(0.5)
        
    if keyboard.is_pressed('m'):  # Se pressionar a tecla b
        print("TECLAS M PRESSIONADA - LER VALORES DE MÍNIMO E MÁXIMO")  # Printa algo pra identificar
        mixer.music.load("C:\\Users\\labvis\\Documents\\Dissertacao\\Mod_Todos\\Por_partes\\Agrupadas\\6.min_max.mp3")  # Toca esse MP3
        mixer.music.play()
        time.sleep(0.5)
        
    if keyboard.is_pressed('1'):  # Se pressionar a tecla b
        print("TECLA 1 PRESSIONADA - LER DADOS DO 1º GRUPO")  # Printa algo pra identificar
        mixer.music.load("C:\\Users\\labvis\\Documents\\Dissertacao\\Mod_Todos\\Por_partes\\Agrupadas\\7.1.mp3")  # Toca esse MP3
        mixer.music.play()
        time.sleep(0.5)
        
    if keyboard.is_pressed('2'):  # Se pressionar a tecla b
        print("TECLA 2 PRESSIONADA - LER DADOS DO 2º GRUPO")  # Printa algo pra identificar
        mixer.music.load("C:\\Users\\labvis\\Documents\\Dissertacao\\Mod_Todos\\Por_partes\\Agrupadas\\8.2.mp3")  # Toca esse MP3
        mixer.music.play()
        time.sleep(0.5)
        
    if keyboard.is_pressed('3'):  # Se pressionar a tecla b
        print("TECLA 3 PRESSIONADA - LER DADOS DO 3º GRUPO")  # Printa algo pra identificar
        mixer.music.load("C:\\Users\\labvis\\Documents\\Dissertacao\\Mod_Todos\\Por_partes\\Agrupadas\\9.3.mp3")  # Toca esse MP3
        mixer.music.play()
        time.sleep(0.5)
        
    if keyboard.is_pressed('e'):  # Se pressionar a tecla b
        print("TECLA E PRESSIONADA - LER MÉDIA E DESVIO PADRÃO")  # Printa algo pra identificar
        mixer.music.load("C:\\Users\\labvis\\Documents\\Dissertacao\\Mod_Todos\\Por_partes\\Agrupadas\\10.media_sd.mp3")  # Toca esse MP3
        mixer.music.play()
        time.sleep(0.5)
        
    if keyboard.is_pressed('d'):  # Se pressionar a tecla b
        print("TECLA D PRESSIONADA - LER A DESCRIÇÃO COMPLETA")  # Printa algo pra identificar
        mixer.music.load("C:\\Users\\labvis\\Documents\\Dissertacao\\Mod_Todos\\Completo\\Agrupadas.mp3")  # Toca esse MP3
        mixer.music.play()
        time.sleep(0.5)


# In[ ]:



