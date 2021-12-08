#----------------------------------------------------------------------------
# Este archivo producto.py contiene la implementación de la clase Horario.
#----------------------------------------------------------------------------
# @author: Antonio Caño @eantoniocalo18 
# @created_date: 29/11/2021
# @version: '2.0'
# ---------------------------------------------------------------------------


class Horario:
    """
    Clase utilizada para representar un Horario.
    ...
    Atributos
    ----------
   
    Publicos
    id: str
        uuid o id que identifica cada horario único
    usuario_relacionado : str
        uuid o id que identifica el usuario asociado al
    horas_semanales: int
        entero que determinará las horas que tiene que trabajar un usuario en una semana
    horas_trabajadas : int
	entero que lleva la sumatoria de las horas que ha ido trabajando un usuario

    """
    def __init__(self, id, usuario_relacionado,horas_semanales, horas_trabajadas):
        self.id = id
        self.nombre = usuario_relacionado
 	self.horas_semanales = horas_semanales
	self.horas_trabajadas = horas_trabajadas

