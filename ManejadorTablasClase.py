class Nodo: 
    """Clase que sirve como un nodo o clase
    """
    def __init__(self, valor, ls, padre, m):
        """Inicialización del nodo

        Args:
            valor (str): Es el nombre de la clase
            ls (list): Es una lista con los hijos de la clase (herencia), al comienzo es vacía
            padre (Nodo): Es una clase base para en Nodo actual
            m (list): Lista de métodos de la clase
        """
        self.valor = valor
        self.hijos = ls
        self.padre = padre
        self.metodos = self.busca_metodos(m)
        if padre != None:
            self.padre.hijos.append(self)

    def busca_metodos(self, m) -> list:
        """Función que busca los métodos totales del Nodo
        que hereda y los originales del mismo

        Args:
            m (list): Métodos originales del Nodo

        Returns:
            list: Lista con todos los métodos (heredados y no heredados)
        """
        met = []
        padre = self.padre

        while (padre != None):
            for i in range(len(padre.metodos)):
                if (m.count(padre.metodos[i][0]) == 0):
                    met.append(padre.metodos[i])
            padre = padre.padre
        
        for i in m:
            met.append((i, self.valor))
    
        return met
       
class ManejadorTablas:
    """Clase que implementa el manjador de tablas de clases
    """
    clases = {}

    def verifica_metodos(self, m) -> bool:
        """Verifica si los métodos de entrada son válidos

        Args:
            m (list): Lista de métodos dada para una clase

        Returns:
            bool: True si la lista dada es válida, False en caso contrario
        """
        for i in m:
            if m.count(i) > 1:
                return False
        return True

    def definir(self, ls) -> bool:
        """Función que permite definir una nueva clase

        Args:
            ls (list): Lista que contiene los datos de dicha clase

        Returns:
            bool: True si se pudo completar la definición, False si no.
        """
        if (self.clases.get(ls[0]) != None):
            print("Error, el nombre ", ls[0], "ya está definido.")
            return False
        if (ls[1] == ":"):
            base = self.clases.get(ls[2])
            if (base == None):
                print("Error, el nombre ", ls[2], "no está definido.")
                return False
            if not(self.verifica_metodos(ls[3:])):
                print("Error, el uno de los métodos está repetido.")
                return False
            self.clases.update({ls[0] : Nodo(ls[0], [], base, ls[3:])})
        else:
            if not(self.verifica_metodos(ls[1:])):
                print("Error, el uno de los métodos está repetido.")
                return False
            self.clases.update({ls[0] : Nodo(ls[0], [], None, ls[1:])})
        return True

    def describir(self, nombre) -> str:
        """Función que describe una clase especificada.

        Args:
            nombre (str): Nombre de la clase

        Returns: 
            str: Cadena con la descripción de la clase, si es encontrada,
            si no lo es, la cadena devuelta es vacía.
        """
        c = self.clases.get(nombre)
        if (c == None):
            print("Error, la clase especificada no está definida.")
            return ""
        s = ""
        for i in range(len(c.metodos)):
            s += str(c.metodos[i][0]) + " -> " + str(c.metodos[i][1]) + " :: " + str(c.metodos[i][0]) + "\n"
        return s
