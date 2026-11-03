# Alonso Lopez Garcia NC = 0087 Fecha 03/11/2026
import matplotlib.pyplot as plt
materias = ["Vision A", "Machine L", "Ciencias N", "Lenguaje A", "Lengua y C"]
calificacion = [10, 9, 8, 10, 7]

plt.pie(calificacion, labels=materias, autopct="%1.1f%%")
plt.title("--- Ejemplo de gráfica pastel calificaciones materias--- 0087")
plt.show()
print("Alonso Lopez Garcia NC = 0087 Fecha 03/11/2026")