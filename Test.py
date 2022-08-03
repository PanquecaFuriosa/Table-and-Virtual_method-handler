from ManejadorTablasClase import ManejadorTablas

def test():
    manejador = ManejadorTablas()
    assert manejador.definir(["A", "f", "g"])
    assert manejador.definir(["B", ":", "A", "f", "h"])
    assert not(manejador.definir(["B", ":", "A", "f", "h"]))
    assert not(manejador.definir(["C", ":", "M", "f", "h"]))
    assert not(manejador.definir(["C", ":", "A", "f", "f", "h"]))
    assert not(manejador.definir(["C", "f", "f", "h"]))

    assert manejador.describir("A") == "f -> A :: f\ng -> A :: g\n"
    assert manejador.describir("B") == "g -> A :: g\nf -> B :: f\nh -> B :: h\n"
    assert manejador.describir("C") == ""