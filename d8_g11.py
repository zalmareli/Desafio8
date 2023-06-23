from datetime import datetime
import os


def limpiar_consola():
    os.system("cls" if os.name == "nt" else "clear")


class Usuario:
    contador_ids = 1

    def __init__(self, nombre, apellido, telefono, username, email, contraseña):
        self.id = self.generar_id()
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono#hola
        self.username = username
        self.email = email
        self.contraseña = contraseña
        self.fecha_registro = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.avatar = None
        self.estado = "Activo"
        self.online = False

    @classmethod
    def generar_id(cls):
        id_generado = cls.contador_ids
        cls.contador_ids += 1
        return id_generado

    def login(self):
        self.online = True
        limpiar_consola()
        print("¡Inicio de sesión exitoso!")

    def logout(self):
        self.online = False
        limpiar_consola()
        print("¡Cierre de sesión exitoso!")


class Publico(Usuario):
    def __init__(self, nombre, apellido, telefono, username, email, contraseña):
        super().__init__(nombre, apellido, telefono, username, email, contraseña)
        self.es_publico = True

    def comentar(self):
        print("\n---- Comentar un artículo ----")
        if not articulos:
            limpiar_consola()
            print('='*30)
            print("No hay artículos disponibles.")
            print('='*30)
            return

        id_articulo = input("Ingrese el ID del artículo: ")
        for articulo in articulos:
            if str(articulo.id) == id_articulo:
                contenido = input("Ingrese su comentario: ")
                comentario = Comentario(
                    id_usuario=self.id, id_articulo=articulo.id, contenido=contenido)
                comentarios.append(comentario)
                limpiar_consola()
                print("¡Comentario agregado!")
                mostrar_menu_usuario(self)
                return
        limpiar_consola()
        print('='*30)
        print("No se encontró el artículo con el ID proporcionado.")
        print('='*30)
        mostrar_menu_usuario(self)


class Colaborador(Usuario):
    def __init__(self, nombre, apellido, telefono, username, email, contraseña):
        super().__init__(nombre, apellido, telefono, username, email, contraseña)
        self.es_colaborador = True

    def comentar(self):
        limpiar_consola()
        print("\n---- Comentar un artículo ----")
        if not articulos:
            limpiar_consola()
            print("No hay artículos disponibles.")
            return

        id_articulo = input("Ingrese el ID del artículo: ")
        for articulo in articulos:
            if str(articulo.id) == id_articulo:
                contenido = input("Ingrese su comentario: ")
                comentario = Comentario(
                    id_usuario=self.id, id_articulo=articulo.id, contenido=contenido)
                comentarios.append(comentario)
                limpiar_consola()
                print("¡Comentario agregado!")
                mostrar_menu_usuario(self)
                return

        print("No se encontró el artículo con el ID proporcionado.")
        mostrar_menu_usuario(self)

    def publicar(self):
        print("\n---- Publicar un artículo ----")
        titulo = input("Ingrese el título del artículo: ")
        resumen = input("Ingrese el resumen del artículo: ")
        contenido = input("Ingrese el contenido del artículo: ")
        imagen = input("Ingrese el nombre de la imagen: ")
        fecha_publicacion = datetime.now()
        
        estado = "Publicado"

        articulo = Articulo(id_usuario=self.id, titulo=titulo, resumen=resumen, contenido=contenido,
                            fecha_publicacion=fecha_publicacion, imagen=imagen, estado=estado)
        articulos.append(articulo)
        limpiar_consola()
        print("¡Artículo publicado!")
        mostrar_menu_usuario(self)


class Articulo:
    contador_ids = 1

    def __init__(self, id_usuario, titulo, resumen, contenido, fecha_publicacion, imagen, estado="Publicado"):
        self.id = self.generar_id()
        self.id_usuario = id_usuario
        self.titulo = titulo
        self.resumen = resumen
        self.contenido = contenido
        self.fecha_publicacion = fecha_publicacion
        self.imagen = imagen
        self.estado = estado

    @classmethod
    def generar_id(cls):
        id_generado = cls.contador_ids
        cls.contador_ids += 1
        return id_generado


class Comentario:
    contador_ids = 1

    def __init__(self, id_articulo, id_usuario, contenido, estado="Activo"):
        self.id = self.generar_id()
        self.id_articulo = id_articulo
        self.id_usuario = id_usuario
        self.contenido = contenido
        self.fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.estado = estado

    @classmethod
    def generar_id(cls):
        id_generado = cls.contador_ids
        cls.contador_ids += 1
        return id_generado


usuarios = []
articulos = []
comentarios = []

def mostrar_menu():
    print("\n========= MENÚ PRINCIPAL DEL BLOG =========")
    print("1. Registrar usuario")
    print("2. Iniciar sesión")
    print("3. Salir")
    print("===========================================")


def mostrar_menu_usuario(usuario):
    print("\n---- MENU USUARIO ----")
    print("1. Comentar un artículo")
    print("2. Ver comentarios de un artículo")
    print("3. Ver artículos")
    if isinstance(usuario, Colaborador):
        print("4. Publicar un artículo")
    print("5. Cerrar sesión")


def registrar_usuario():
    limpiar_consola()
    print("\n---- Registro Usuario ----")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    telefono = input("Teléfono: ")
    username = input("Username: ")
    email = input("Email: ")
    contraseña = input("Contraseña: ")

    tipo_usuario = input("Tipo de usuario (1. Público / 2. Colaborador): ")
    while tipo_usuario != "1" and tipo_usuario != "2":
        print("Opción inválida. Intente nuevamente.")
        tipo_usuario = input("Tipo de usuario (1. Público / 2. Colaborador): ")

    if tipo_usuario == "1":
        usuario = Publico(nombre, apellido, telefono,
                          username, email, contraseña)
    else:
        usuario = Colaborador(nombre, apellido, telefono,
                              username, email, contraseña)

    usuarios.append(usuario)
    print('='*30)
    print("¡Registro exitoso!")
    print('='*30)
    mostrar_menu()


def iniciar_sesion():
    limpiar_consola()
    print('='*35)
    print("\tACCEDER AL SISTEMA")
    print('='*35)
    username = input("Usuario: ")
    contraseña = input("Contraseña: ")

    for usuario in usuarios:
        if usuario.username == username and usuario.contraseña == contraseña:
            usuario.login()
            mostrar_menu_usuario(usuario)
            menu_usuario(usuario)
            break
    else:
        limpiar_consola()
        print('='*30)
        print("Usuario o contraseña incorrectos.")
        print('='*30)
        mostrar_menu()


def menu_usuario(usuario):
    while True:
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            usuario.comentar()
            mostrar_menu_usuario(usuario)
        elif opcion == "2":
            ver_comentarios_articulo()
            mostrar_menu_usuario(usuario)
        elif opcion == "3":
            ver_articulos()
            mostrar_menu_usuario(usuario)
        elif opcion == "4" and isinstance(usuario, Colaborador):
            usuario.publicar()
            mostrar_menu_usuario(usuario)
        elif opcion == "5":
            usuario.logout()
            mostrar_menu()
            break
        else:
            print("Opción inválida.")


def obtener_comentarios_articulo(id_articulo):
    comentarios_articulo = []
    for comentario in comentarios:
        if comentario.id_articulo == id_articulo:
            comentarios_articulo.append(comentario)
    return comentarios_articulo


def ver_comentarios_articulo():
    if not articulos:
        limpiar_consola()
        print('='*30)
        print("No hay artículos disponibles.")
        print('='*30)
        return

    id_articulo = input("Ingrese el ID del artículo: ")
    for articulo in articulos:
        if str(articulo.id) == id_articulo:
            comentarios_articulo = obtener_comentarios_articulo(articulo.id)
            if comentarios_articulo:
                print("\nComentarios del artículo:")
                for comentario in comentarios_articulo:
                    print(
                        f"- Usuario ID: {comentario.id_usuario}, Contenido: {comentario.contenido}")
            else:
                print('='*30)
                print("No hay comentarios para este artículo.")
                print('='*30)
            return
    limpiar_consola()
    print('='*30)
    print("No se encontró el artículo con el ID proporcionado.")
    print('='*30)


def ver_articulos():
    if not articulos:
        limpiar_consola()
        print('='*30)
        print("No hay artículos disponibles.")
        print('='*30)
        return

    limpiar_consola()
    print("\nLista de artículos:")
    for articulo in articulos:
        print(f"- ID: {articulo.id}, Título: {articulo.titulo}")


def main():
    while True:
        limpiar_consola()
        mostrar_menu()
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            iniciar_sesion()
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.")


if __name__ == '__main__':
    main()

# DESAFIO 8 GRUPO 11
# Martin Elias Zalazar
# David Walter Vargas
# Fabian Alejandro Sanchez
# Gomez Miguel Alejandro