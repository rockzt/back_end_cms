import psycopg2
import category

from psycopg2 import sql

# Aquí importa las funciones que has definido en tu aplicación, por ejemplo:
# from myapp import create_article, update_article, deactivate_article, get_all_articles, get_article, ...

# Conexión a la base de datos PostgreSQL
conn = psycopg2.connect(
    database="back_end_cms",
    user="postgres",
    password="mamita",
    host="localhost",  # Cambia esto a la ubicación de tu base de datos
    port="5432"  # Cambia esto al puerto de tu base de datos
)

# Crear un cursor para interactuar con la base de datos
cursor = conn.cursor()

# Función para imprimir el menú
def print_menu():
    print("\nMenú:")
    print("1. Crear un nuevo artículo")
    print("2. Modificar un artículo existente")
    print("3. Desactivar un artículo")
    print("4. Obtener la lista de todos los artículos")
    print("5. Obtener los datos de un artículo")
    print("6. Obtener los artículos de una categoría")
    print("7. Obtener los artículos activos/publicados")
    print("8. Obtener los artículos de un autor")
    print("9. Crear un nuevo autor")
    print("10. Modificar los datos de un autor existente")
    print("11. Obtener los datos de un autor")
    print("12. Crear una nueva categoría")
    print("13. Modificar los datos de una categoría")
    print("14. Obtener una lista de categorías")
    print("0. Salir")

# Función para solicitar una opción del menú al usuario
def get_menu_option():
    while True:
        try:
            option = int(input("\nIngrese el número de la opción que desea ejecutar: "))
            if 0 <= option <= 14:
                return option
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError:
            print("Entrada no válida. Ingrese un número válido.")

# Función principal
def main():
    while True:
        print_menu()
        option = get_menu_option()

        if option == 0:
            break
        elif option == 1:
            # Llamar a la función para crear un nuevo artículo
            pass
        elif option == 2:
            # Llamar a la función para modificar un artículo existente
            pass
        elif option == 3:
            # Llamar a la función para desactivar un artículo
            pass
        elif option == 4:
            # Llamar a la función para obtener la lista de todos los artículos
            pass
        elif option == 5:
            # Llamar a la función para obtener los datos de un artículo
            pass
        elif option == 6:
            # Llamar a la función para obtener los artículos de una categoría
            pass
        elif option == 7:
            # Llamar a la función para obtener los artículos activos/publicados
            pass
        elif option == 8:
            # Llamar a la función para obtener los artículos de un autor
            pass
        elif option == 9:
            # Llamar a la función para crear un nuevo autor
            pass
        elif option == 10:
            # Llamar a la función para modificar los datos de un autor existente
            pass
        elif option == 11:
            # Llamar a la función para obtener los datos de un autor
            pass
        elif option == 12:
            # Llamar a la función para crear una nueva categoría
            pass
        elif option == 13:
            # Llamar a la función para modificar los datos de una categoría
            pass
        elif option == 14:
            # Llamar a la función para obtener una lista de categorías
            pass

if __name__ == "__main__":
    main()

# Cerrar la conexión cuando hayas terminado
cursor.close()
conn.close()
