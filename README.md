Turn-o-Matic: The Simple Turn Generator

This is a simple console-based turn generator system designed for a retail store with different departments. It simulates the process of a customer getting a unique turn number for a specific department. The project is an excellent example of using generators in Python to create an efficient and clean solution for generating a sequence of unique numbers.

How It Works

The system is split into two files:

- numeros.py: This file contains generator functions (numeros_perfumeria, numeros_farmacia, numeros_cosmeticos) that produce a unique sequence of numbers for each department. Using generators is memory-efficient because they yield one number at a time instead of creating a large list in memory. The decorador function then retrieves the next available number for a given department.

- main.py: This file handles the user interaction. It prompts the customer to choose a department and then calls the decorador function to get and display their turn number. The program continues to ask if the customer wants another turn, making it a continuous service loop.

Key Features

- Generator-Based Numbering: Utilizes yield to create generators for each department, ensuring a continuous and memory-efficient supply of unique turn numbers.

- User-Friendly Interface: A clear and simple menu guides the user to select their desired department.

- Error Handling: Includes try-except blocks to handle invalid user input, ensuring the program doesn't crash if the user enters an incorrect option.

- Modular Design: The separation of logic into two files (main.py for UI and numeros.py for number generation) makes the code organized and easy to understand.

Usage

- Save the files: Save the provided code as main.py and numeros.py in the same directory.

- Open your terminal or command prompt.

- Run the script: Navigate to the directory and run the main file.

      Bash
      
      python main.py
  
- Follow the prompts: Choose your department by entering P, F, or C and receive your turn number.

Example Interaction

    Bienvenido a la tienda!!!
    [P] - Perfumeria
    [F] - Farmacia
    [C] - Cosmeticos
    Elija su rubro: F
    
    ***********************
    Su numero es:
    F - 1
    Espere su turno
    ***********************
    
    Quieres sacar otro turno? [S] o [N]: S
    Bienvenido a la tienda!!!
    [P] - Perfumeria
    [F] - Farmacia
    [C] - Cosmeticos
    Elija su rubro: P
    
    ***********************
    Su numero es:
    P - 1
    Espere su turno
    ***********************
    
    Quieres sacar otro turno? [S] o [N]: N
    Gracias por su visita

"The code in this repository is based on lessons from Federico Garay's course."
