# Welcome to GitHub Desktop!

This is your README. READMEs are where you can communicate what your project is and how to use it.

Write your name on line 6, save it, and then head back to GitHub Desktop.
Cesar

ENGLISH

🏰 Procedural Dungeon Crawler Generator

This is a console-based game engine written in Python. It implements procedural map generation, matrix navigation, and a basic physics and collision system.

📝 Description

The project simulates the exploration of a randomly generated dungeon. Every time the program starts, a unique map with variable dimensions (between 7x7 and 16x16) is created, featuring walls, treasures, and empty spaces.

The player controls a character ("😎") and must navigate the environment while respecting the physical limits of the world.

🚀 Key Features

Procedural Generation: An algorithm utilizing random to build unique maps upon each execution, randomly placing obstacles (🧱) and loot (🧰).

Physics Engine (Collisions): An anticipatory validation system that prevents the player from walking through walls.

World Limits: Boundary Checking logic to ensure the player does not exit the matrix, preventing IndexError exceptions.

State Persistence: The map is held in memory and updates in real-time, clearing the player's trail as they move.

Console Rendering: Graphical visualization of the matrix using emojis for an enhanced User Experience (UX).

🎮 Controls

The game uses the standard WASD input system:

w: Move Up ⬆️

s: Move Down ⬇️

a: Move Left ⬅️

d: Move Right ➡️

🛠️ Technologies Used

Language: Python 3.x

Libraries:

random (Randomness generation)

os (Screen clearing for fluid rendering)

📋 How to Run

Make sure you have Python installed.

Clone this repository or download the file.

Run the script in your terminal:

Bash

python mazmorra.py
Author: Cesar Project developed as part of the intensive training on Programming Logic and Data Structures.

ESPAÑOL

🏰 Generador de Mazmorras Procedurales (Dungeon Crawler)

Este es un motor de juego basado en consola escrito en Python. Implementa generación procedural de mapas, navegación por matrices y un sistema básico de físicas y colisiones.

📝 Descripción

El proyecto simula la exploración de una mazmorra generada aleatoriamente. Cada vez que se inicia el programa, se crea un mapa único de dimensiones variables (entre 7x7 y 16x16) con paredes, tesoros y espacios vacíos.

El jugador controla un personaje ("😎") y debe navegar por el entorno respetando los límites físicos del mundo.

🚀 Características Principales (Features)

Generación Procedural: Algoritmo que utiliza random para construir mapas únicos en cada ejecución, colocando obstáculos (🧱) y botín (🧰) de forma aleatoria.

Motor de Físicas (Colisiones): Sistema de validación anticipada que impide al jugador atravesar paredes.

Límites del Mundo: Lógica de Boundary Checking para asegurar que el jugador no salga de la matriz, evitando errores de índice (IndexError).

Persistencia de Estado: El mapa se mantiene en memoria y se actualiza en tiempo real, limpiando el rastro del jugador al moverse.

Renderizado en Consola: Visualización gráfica de la matriz utilizando emojis para una mejor experiencia de usuario (UX).

🎮 Controles

El juego utiliza el sistema de entrada estándar WASD:

w: Mover Arriba ⬆️

s: Mover Abajo ⬇️

a: Mover Izquierda ⬅️

d: Mover Derecha ➡️

🛠️ Tecnologías Utilizadas

Lenguaje: Python 3.x

Librerías:

random (Generación de aleatoriedad)

os (Limpieza de pantalla para renderizado fluido)

📋 Cómo Ejecutar

Asegúrate de tener Python instalado.

Clona este repositorio o descarga el archivo.

Ejecuta el script en tu terminal:

python mazmorra.py


Autor: Cesar
Proyecto desarrollado como parte del entrenamiento intensivo de Lógica de Programación y Estructuras de Datos.

