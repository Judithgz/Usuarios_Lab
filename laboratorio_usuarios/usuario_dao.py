from cursor_pool import CursorPool
from logger_base import log
from usuario import Usuario

class UsuarioDAO:

    _SELECCIONAR = 'SELECT * FROM usuario ORDER BY id_usuario'
    _INSERTAR = 'INSERT INTO usuario(username, password) VALUES(%s, %s)'
    _ACTUALIZAR = 'UPDATE usuario SET username=%s, password=%s WHERE id_usuario=%s'
    _ELIMINAR = 'DELETE FROM usuario WHERE id_usuario=%s'



    @classmethod
    def seleccionar(cls):
        with CursorPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2])
                usuarios.append(usuario)
            return usuarios


    @classmethod
    def insertar(cls, usuario):
        with CursorPool() as cursor:
            log.info(f'Usuario a insertar: {usuario}')
            valores = (usuario.username, usuario.password)
            cursor.execute(cls._INSERTAR, valores)
            log.info(f'Se ingreso usuario: {usuario}')
            return cursor.rowcount


    @classmethod
    def actualizar(cls, usuario):
        with CursorPool() as cursor:
            log.info(f'Usuario a actualizar: {usuario}')
            valores = (usuario.username, usuario.password, usuario.id_usuario)
            cursor.execute(cls._ACTUALIZAR, valores)
            return cursor.rowcount

    @classmethod
    def eliminar(cls, usuario):
        with CursorPool() as cursor:
            log.info(f'Usuario a eliminar: {usuario}')
            valores = (usuario.id_usuario,)
            cursor.execute(cls._ELIMINAR, valores)
            log.info(f'Usuario eliminado_ {usuario}')
            return cursor.rowcount


if __name__ == '__main':
    usuario1 = Usuario(username='Judithgz', password='pink123')
    usuario_insertado = UsuarioDAO.insertar(usuario1)
    log.debug(f'Personas insertadas: {usuario_insertado}')
