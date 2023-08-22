
import category as category
import articulo
import autor
import datetime


#from psycopg2 import sql

# Aquí importa las funciones que has definido en tu aplicación, por ejemplo:
# from myapp import create_article, update_article, deactivate_article, get_all_articles, get_article, ...

# Conexión a la base de datos PostgreSQL
'''
conn = psycopg2.connect(
    database="back_end_cms",
    user="postgres",
    password="mamita",
    host="localhost",  # Cambia esto a la ubicación de tu base de datos
    port="5432"  # Cambia esto al puerto de tu base de datos
)
'''
# Crear un cursor para interactuar con la base de datos
#cursor = conn.cursor()

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
    print("15. Nombre del autor y sus artículos")
    print("0. Salir")

# Función para solicitar una opción del menú al usuario
def get_menu_option():
    while True:
        try:
            option = int(input("\nIngrese el número de la opción que desea ejecutar: "))
            if 0 <= option <= 15:
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
            ct = datetime.datetime.now()
            print("Crear Articulo")
            title = input('\n \t \t Titulo: ')
            content = input('\n \t \t Contenido: ')
            autor_id = input('\n \t \t Autor id: ')
            category_id = input('\n \t \t Categoria id: ')
            pub_date = ct
            last_update = ct
            columns = ['titulo', 'conten', 'autor_id', 'categoria_id', 'pub_date', 'last_update' ,'active']
            values = (title, content, autor_id, category_id, pub_date, last_update, 1)
            result = articulo.create_artticle(columns,values)
            print(result)
        elif option == 2:
            # Llamar a la función para modificar un artículo existente}
            ct = datetime.datetime.now()
            print("Modifcar Articulo")
            article_id = input('\n \t \t Articulo ID: ')
            title = input('\n \t \t Titulo: ')
            content = input('\n \t \t Contenido: ')
            autor_id = input('\n \t \t Autor id: ')
            category_id = input('\n \t \t Categoria id: ')
            active = input('\n \t \t Activo: ')
            pub_date = ct
            last_update = ct
            columns = ['titulo', 'conten', 'autor_id', 'categoria_id', 'pub_date', 'last_update' ,'active']
            values = (title, content, autor_id, category_id, pub_date, last_update, active)
            articulo.modify_article(article_id, columns, values)
        elif option == 3:
            # Llamar a la función para desactivar un artículo
            print("Desactivar Articulo")
            articulo_id = input('\n \t \t Articulo ID: ')
            result = articulo.deactivate_article(articulo_id)
            print(result)
        elif option == 4:
            # Llamar a la función para obtener la lista de todos los artículos
            result = articulo.get_all_articles()
            print(result)
        elif option == 5:
            # Llamar a la función para obtener los datos de un artículo
            print("Datos de un Articulo")
            articulo_id = input('\n \t \t Articulo ID: ')
            result = articulo.get_article(articulo_id)
            print(result)
        elif option == 6:
            # Llamar a la función para obtener los artículos de una categoría
            print("Articulos de un Articulo")
            categoria_id = input('\n \t \t Categoria ID: ')
            result = articulo.get_article_by_category(categoria_id)
            print(result)
        elif option == 7:
            # Llamar a la función para obtener los artículos activos/publicados
            result = articulo.get_activated_articles()
            print(result)
        elif option == 8:
            # Llamar a la función para obtener los artículos de un autor
            result = articulo.get_article_by_author(1)
            print(result)
        elif option == 9:
            # Llamar a la función para crear un nuevo autor
            #values=("Daniel", "Azsamar","Dani@hotmail.com","123")
            values=autor.datos_autor()
            mi_resultado=autor.insert_autor(values)
            print(mi_resultado, ":", values)

        elif option == 10:
            # Llamar a la función para modificar los datos de un autor existente
            values=("Montse","mont@hotmail.com")
            columns=["first_name","email"]
            mi_result=autor.update_autor(columns,values,"6")

        elif option == 11:
            # Llamar a la función para obtener los datos de un autor
            id_autor = input('\n \t \t Id del Autor a consultar: ')
            mi_result=autor.get_autor(id_autor)
            for v in mi_result:
                print("\n \nId del Autor222: ",v[0])
                print("Nombre del Autor: ",v[1], " ",v[2])
                print("Email: ",v[3],"  ","Password:",v[4])
                print("\n")

        elif option == 12:
            # Llamar a la función para crear una nueva categoría
            print("Creemos juntos una nueva categoria")
            name=input("Dame un nombre para la categoria nueva:\n")
            description=input("Describe esta categoria:\n")
            columns = ['nom_cat', 'descrip_cate']
            values = (name, description)
            category.create_category(columns, values)

            # La lista de categoria es:

            print("La nueva lista es:\n")
            categories=category.get_all_categorias()
            for categoria in categories:
                print(categoria)

        elif option == 13:
            #Primero mostramos la lista actual
            print("La nueva lista es:\n")
            categories=category.get_all_categorias()
            for categoria in categories:
                print(categoria)

            catid=input("Que numero de categoria quieres modificar?\n")
            nombrecat=input("¿que nombre quieres darle?\n")
            descicat=input("¿Que descripcion quieres darle?\n")


            # Llamar a la función para modificar los datos de una categoría
            columns = ['nom_cat', 'descrip_cate']
            values = (nombrecat, descicat)
            category.modify_categoria(catid, columns, values)

            print("La nueva lista es:\n")
            categories=category.get_all_categorias()
            for categoria in categories:
                print(categoria)

        elif option == 14:
            # Obtener la lista de categorias.
            categories=category.get_all_categorias()
            for categoria in categories:
                print(categoria)

        elif option == 15:
            # Llamar a la función para ver los articulos de un Autor con Nombre
            id_autor = input('\n \t \t Id del Autor a consultar: ')
            mi_result=autor.get_arts(id_autor)
            #print(mi_result)
            for v in mi_result:
                print("\n \nId del Articulo: ",v[0])
                print("Titulo del Articulo: ",v[1])
                print("Fecha de Publicacion:",v[2])
                print("Id Autor:",v[3],"    Nombre del Autor: ",v[4], " ",v[5])

if __name__ == "__main__":
    main()

# Cerrar la conexión cuando hayas terminado
#cursor.close()
#conn.close()