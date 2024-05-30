def contar_colisiones(robots):
    # Inicializamos el contador de colisiones
    colisiones = 0
    
    # Convertimos la cadena de robots en una lista para manejarla más fácilmente
    robots = list(robots)
    
    # Iteramos a través de la lista de robots para detectar colisiones
    i = 0
    while i < len(robots) - 1:
        if robots[i] == 'R' and robots[i + 1] == 'L':
            # Colisión detectada
            colisiones += 1
            
            # Los robots cambian de dirección, por lo que intercambiamos 'R' por 'L' y viceversa
            robots[i] = 'L'
            robots[i + 1] = 'R'
            
            # Decrementamos i para verificar posibles colisiones anteriores
            if i > 0:
                i -= 2
            else:
                i = 0
        else:
            # Avanzamos al siguiente par de robots
            i += 1
    
    return colisiones

# Ejemplo de uso:
secuencia = "RLRLR"
print(contar_colisiones(secuencia))  # Debería imprimir el número de colisiones

