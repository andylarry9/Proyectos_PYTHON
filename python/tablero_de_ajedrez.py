#Este programa ofrece una experiencia básica para interactuar con un tablero de ajedrez, 
#permitiendo tanto la colocación de piezas como la realización de movimientos.

class TableroAjedrez:
    def __init__(self):
        # Inicializa un tablero vacío de 8x8
        self.tablero = [[' ' for _ in range(8)] for _ in range(8)]
        self.piezas = {
            'r': 'Torre',
            'n': 'Caballo',
            'b': 'Alfil',
            'q': 'Reina',
            'k': 'Rey',
            'p': 'Peón'
        }

    def mostrar_tablero(self):
        print("  a b c d e f g h")
        for i, fila in enumerate(self.tablero):
            print(str(8 - i) + ' ' + ' '.join(fila) + ' ' + str(8 - i))
        print("  a b c d e f g h")

    def colocar_pieza(self, pieza, posicion):
        fila, columna = 8 - int(posicion[1]), ord(posicion[0]) - ord('a')
        if 0 <= fila < 8 and 0 <= columna < 8:
            self.tablero[fila][columna] = pieza
        else:
            print("Posición fuera del tablero. Inténtalo de nuevo.")

    def mover_pieza(self, inicio, fin):
        fila_inicio, col_inicio = 8 - int(inicio[1]), ord(inicio[0]) - ord('a')
        fila_fin, col_fin = 8 - int(fin[1]), ord(fin[0]) - ord('a')
        if (0 <= fila_inicio < 8 and 0 <= col_inicio < 8 and
            0 <= fila_fin < 8 and 0 <= col_fin < 8):
            pieza = self.tablero[fila_inicio][col_inicio]
            if pieza != ' ':
                self.tablero[fila_inicio][col_inicio] = ' '
                self.tablero[fila_fin][col_fin] = pieza
            else:
                print("No hay ninguna pieza en la posición de inicio.")
        else:
            print("Movimiento fuera del tablero. Inténtalo de nuevo.")

    def interactivo(self):
        while True:
            self.mostrar_tablero()
            print("\nOpciones: \n1. Colocar pieza \n2. Mover pieza \n3. Salir")
            opcion = input("Elige una opción (1/2/3): ").strip()

            if opcion == '1':
                print("\nPiezas disponibles: r (Torre), n (Caballo), b (Alfil), q (Reina), k (Rey), p (Peón)")
                pieza = input("Introduce la pieza a colocar (r/n/b/q/k/p): ").lower()
                if pieza not in self.piezas:
                    print("Pieza no válida. Inténtalo de nuevo.")
                    continue
                posicion = input("Introduce la posición (ej. e2): ").lower()
                if len(posicion) == 2 and posicion[0] in 'abcdefgh' and posicion[1] in '12345678':
                    self.colocar_pieza(pieza, posicion)
                else:
                    print("Posición no válida. Inténtalo de nuevo.")
            
            elif opcion == '2':
                inicio = input("Introduce la posición de inicio (ej. e2): ").lower()
                fin = input("Introduce la posición de destino (ej. e4): ").lower()
                if (len(inicio) == 2 and len(fin) == 2 and 
                    inicio[0] in 'abcdefgh' and inicio[1] in '12345678' and
                    fin[0] in 'abcdefgh' and fin[1] in '12345678'):
                    self.mover_pieza(inicio, fin)
                else:
                    print("Posición no válida. Inténtalo de nuevo.")
            
            elif opcion == '3':
                print("Gracias por jugar.")
                break
            
            else:
                print("Opción no válida. Inténtalo de nuevo.")

# Ejecución del programa
tablero = TableroAjedrez()
tablero.interactivo()
