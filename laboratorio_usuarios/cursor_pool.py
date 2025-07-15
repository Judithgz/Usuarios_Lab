from conexion import Conexion
from logger_base import log


class CursorPool:
    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        log.debug(f'Inicio del metodo with __enter__')
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self, tipo_exc, valor_exc, detalle_exc):
        log.debug(f'Se ejecuta metodo __exit__')
        if valor_exc:
            self._conexion.rollback()
            log.error(f'Ocurrio una excepcion, se hace rollback: {valor_exc} {tipo_exc} {detalle_exc}')
        else:
            self._conexion.commit()
            log.debug(f'Commit de la transaccion')
        self._cursor.close()
        Conexion.liberarConexion(self._conexion)

if __name__ == '__main__':
    with CursorPool() as cursor:
        log.debug('Dentro del bloque with')
        cursor.execute('SELECT * FROM usuario')
        log.debug(cursor.fetchall())