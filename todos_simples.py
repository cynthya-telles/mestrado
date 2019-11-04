
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
      '\n T - LER TÍTULO'
      '\n Y - LER LEGENDA DO EIXO Y'
      '\n X - LER LEGENDA DO EIXO X'
      '\n M - LER VALORES DE MÍNIMO E MÁXIMO'
      '\n 1 - LER DADOS DA BARRA 1'
      '\n 2 - LER DADOS DA BARRA 2'
      '\n 3 - LER DADOS DA BARRA 3'
      '\n 4 - LER DADOS DA BARRA 4'
      '\n 5 - LER DADOS DA BARRA 5'
      '\n 6 - LER DADOS DA BARRA 6'
      '\n 7 - LER DADOS DA BARRA 7'
      '\n E - LER MÉDIA E DESVIO PADRÃO'
      '\n S - SAIR')


while True:  # Um loop que vai rodar até que se pressione a tecla "q"

    if keyboard.is_pressed('s'):  # Se pressionar a tecla q o programa fecha
        print('SAINDO')
        break  # finishing the loop

    if keyboard.is_pressed('c'):  # Se pressionar a tecla a
        print("TECLA C PRESSIONADA - LER CATEGORIA") # Printa algo pra identificar
        mixer.music.load("C:\\Users\\labvis\\Documents\\Dissertacao\\Mod_Todos\\Por_partes\\Simples\\1.cat.mp3")  # Toca esse MP3
        mixer.music.play()
        time.sleep(0.5) # Isso aqui é só pra debouncing, evitar que cada tecla seja pressionada varias vezes enquanto não soltar a tecla

    if keyboard.is_pressed('t'):  # Se pressionar a tecla b
        print("TECLA T PRESSIONADA - LER TÍTULO")  # Printa algo pra identificar
        mixer.music.load("C:\\Users\\labvis\\Documents\\Dissertacao\\Mod_Todos\\Por_partes\\Simples\\2.titulo.mp3")  # Toca esse MP3
        mixer.music.play()
        time.sleep(0.5) # Isso aqui é só pra debouncing, evitar que cada tecla seja pressionada varias vezes enquanto não soltar a tecla
        
    if keyboard.is_pressed('y'):  # Se pressionar a tecla b
        print("TECLA Y PRESSIONADA - LER LEGENDA DO EIXO Y")  # Printa algo pra identificar
        mixer.music.load("C:\\Users\\labvis\\Documents\\Dissertacao\\Mod_Todos\\Por_partes\\Simples\\3.eixo y.mp3")  # Toca esse MP3
        mixer.music.play()
        time.sleep(0.5)    
        
    if keyboard.is_pressed('x'):  # Se pressionar a tecla b
        print("TECLA X PRESSIONADA - LER LEGENDA DO EIXO X")  # Printa algo pra identificar
        mixer.music.load("C:\\Users\\labvis\\Documents\\Dissertacao\\Mod_Todos\\Por_partes\\Simples\\4.eixo x.mp3")  # Toca esse MP3
        mixer.music.play()
        time.sleep(0.5)
        
    if keyboard.is_pressed('m'):  # Se pressionar a tecla b
        print("TECLAS M PRESSIONADA - LER VALORES DE MÍNIMO E MÁXIMO")  # Printa algo pra identificar
        mixer.music.load("C:\\Users\\labvis\\Documents\\Dissertacao\\Mod_Todos\\Por_partes\\Simples\\5.min_max.mp3")  # Toca esse MP3
        mixer.music.play()
        time.sleep(0.5)
        
    if keyboard.is_pressed('1'):  # Se pressionar a tecla b
        print("TECLA 1 PRESSIONADA - LER DADOS DA 1ª BARRA")  # Printa algo pra identificar
        mixer.music.load("C:\\Users\\labvis\\Documents\\Dissertacao\\Mod_Todos\\Por_partes\\Simples\\6.1.mp3")  # Toca esse MP3
        mixer.music.play()
        time.sleep(0.5)
        
    if keyboard.is_pressed('2'):  # Se pressionar a tecla b
        print("TECLA 2 PRESSIONADA - LER DADOS DO 2ª BARRA")  # Printa algo pra identificar
        mixer.music.load("C:\\Users\\labvis\\Documents\\Dissertacao\\Mod_Todos\\Por_partes\\Simples\\7.2.mp3")  # Toca esse MP3
        mixer.music.play()
        time.sleep(0.5)
        
    if keyboard.is_pressed('3'):  # Se pressionar a tecla b
        print("TECLA 3 PRESSIONADA - LER DADOS DO 3ª BARRA")  # Printa algo pra identificar
        mixer.music.load("C:\\Users\\labvis\\Documents\\Dissertacao\\Mod_Todos\\Por_partes\\Simples\\8.3.mp3")  # Toca esse MP3
        mixer.music.play()
        time.sleep(0.5)
        
    if keyboard.is_pressed('4'):  # Se pressionar a tecla b
        print("TECLA 4 PRESSIONADA - LER DADOS DO 4ª BARRA")  # Printa algo pra identificar
        mixer.music.load("C:\\Users\\labvis\\Documents\\Dissertacao\\Mod_Todos\\Por_partes\\Simples\\9.4.mp3")  # Toca esse MP3
        mixer.music.play()
        time.sleep(0.5)
        
    if keyboard.is_pressed('5'):  # Se pressionar a tecla b
        print("TECLA 5 PRESSIONADA - LER DADOS DO 5ª BARRA")  # Printa algo pra identificar
        mixer.music.load("C:\\Users\\labvis\\Documents\\Dissertacao\\Mod_Todos\\Por_partes\\Simples\\10.5.mp3")  # Toca esse MP3
        mixer.music.play()
        time.sleep(0.5)
        
    if keyboard.is_pressed('6'):  # Se pressionar a tecla b
        print("TECLA 6 PRESSIONADA - LER DADOS DO 6ª BARRA")  # Printa algo pra identificar
        mixer.music.load("C:\\Users\\labvis\\Documents\\Dissertacao\\Mod_Todos\\Por_partes\\Simples\\11.6.mp3")  # Toca esse MP3
        mixer.music.play()
        time.sleep(0.5)
        
    if keyboard.is_pressed('7'):  # Se pressionar a tecla b
        print("TECLA 7 PRESSIONADA - LER DADOS DO 7ª BARRA")  # Printa algo pra identificar
        mixer.music.load("C:\\Users\\labvis\\Documents\\Dissertacao\\Mod_Todos\\Por_partes\\Simples\\12.7.mp3")  # Toca esse MP3
        mixer.music.play()
        time.sleep(0.5)
        
    if keyboard.is_pressed('e'):  # Se pressionar a tecla b
        print("TECLA E PRESSIONADA - LER MÉDIA E DESVIO PADRÃO")  # Printa algo pra identificar
        mixer.music.load("C:\\Users\\labvis\\Documents\\Dissertacao\\Mod_Todos\\Por_partes\\Simples\\13.media_sd.mp3")  # Toca esse MP3
        mixer.music.play()
        time.sleep(0.5)
        
    if keyboard.is_pressed('d'):  # Se pressionar a tecla b
        print("TECLA D PRESSIONADA - LER A DESCRIÇÃO COMPLETA")  # Printa algo pra identificar
        mixer.music.load("C:\\Users\\labvis\\Documents\\Dissertacao\\Mod_Todos\\Completo\\Simples.mp3")  # Toca esse MP3
        mixer.music.play()
        time.sleep(0.5)


# In[ ]:



