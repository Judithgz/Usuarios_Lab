from usuario import Usuario
from usuario_dao import UsuarioDAO
from logger_base import log

opcion = None
while opcion != 5:
    print('Opciones: ')
    print('1. Listar usuarios')
    print('2. Agregar usuario')
    print('3. Modificar usuario')
    print('4. Eliminar usuario')
    print('5. Salir')

    opcion = int(input('Elige tu opcion: '))
    if opcion == 1:
        usuarios = UsuarioDAO.seleccionar()
        for usuario in usuarios:
            log.info(usuario)
    elif opcion == 2:
        # Insertar usuario
        valor_username = input('Ingresa el username: ')
        valor_password = input('Ingresar contraseña: ')
        usuario = Usuario(username=valor_username, password=valor_password)
        usuario_ingresado = UsuarioDAO.insertar(usuario)
        log.info(f'Usuario ingresado: {usuario_ingresado}')
    elif opcion == 3:
        # Actualizar un usuario
        valor_id = int(input('Ingresa el id del usuario a modificar: '))
        valor_username = input('Ingresa el nuevo username: ')
        valor_password = input('Ingresa la nueva contraseña: ')
        usuario = Usuario(id_usuario=valor_id, username=valor_username, password=valor_password)
        usuario_actualizado = UsuarioDAO.actualizar(usuario)
        log.info(f'Usuario actualizado: {usuario}')
    elif opcion == 4:
        # Eliminar un registro
        valor_id = int(input('Ingresa el id del usuario a eliminar: '))
        usuario = Usuario(id_usuario=valor_id)
        usuario_eliminado = UsuarioDAO.eliminar(usuario)
        log.info(f'Usuario eliminado: {usuario_eliminado}')
else:
    log.info('Salimos de la aplicación..')
