class Grafo:
    def __init__(self):
        self.aristas =[]
        self.vertices ={}
        
    def agregar_vertice(self,nombre):
        self.vertices[nombre] ={}
        
    def agregar_arista(self,origen,destino,peso=1):
        self.aristas.append((origen,destino,peso))
        if origen not in self.vertices:
            self.agregar_vertice(origen)
        if destino not in self.vertices:
            self.agregar_vertice(destino)
        self.vertices[origen][destino] = peso
        self.vertices[destino][origen] = peso
        
    def obtener_aristas(self):
        return self.aristas
    
    def obtener_vertices(self):
        return list(self.vertices.keys())

#Creacion de un grafo con bucle
def redBucle1():
    red = Grafo()
    red.agregar_arista("Ethernet1", "Switch3", 1)
    red.agregar_arista("Switch3", "Switch5", 1)
    red.agregar_arista("Switch3", "Switch2", 1)
    red.agregar_arista("Switch5", "Switch1", 1)
    red.agregar_arista("Switch5", "Switch7", 1)
    red.agregar_arista("Switch2", "Switch1", 1) 	
    red.agregar_arista("Switch1", "Switch6", 1) 
    red.agregar_arista("Switch1", "Switch4", 1)
    red.agregar_arista("Switch1", "Switch7", 1)
    red.agregar_arista("Switch6", "Switch4", 1) 
    red.agregar_arista("Switch4", "Ethernet3", 1)	
    red.agregar_arista("Switch7", "Ethernet2", 1) 
    
    return red

def spanningTreeAlgorithm(grafo):
    # Guardamos los vertices y aristas del grafo original 
    vertices = grafo.obtener_vertices()
    aristas = grafo.obtener_aristas()
    # Instanciamos un grafo vacio para almacenar aristas, vertices y pesos del grafo una vez se ejecute el algoritmo
    redSinBucle = Grafo()
    # Creamos un diccionario para representar cada subgrafo como una lista de vertices
    subGrafo = {}
    for v in vertices:
        subGrafo[v] = [v]
        # Agregamos cada vertice al nuevo grafo
        redSinBucle.agregar_vertice(v)
    for a in aristas:
        origen, destino, peso = a
        Origen = subGrafo[origen]
        Destino = subGrafo[destino]   
        # Si los vertices de origen y destino no estan en el mismo subgrafo se agrega la arista al nuevo grafo con toda su informacion
        if Origen != Destino:
            redSinBucle.agregar_arista(origen, destino, peso)         
            # Se crea un nuevo subgrafo con los vértices del subgrafo tanto de origen como destino
            nuevoVertice = Origen + Destino   
            # Se actualiza el diccionario con los subgrafos para que todos los vértices cambien al nuevo subgrafo
            for v in nuevoVertice:
                subGrafo[v] = nuevoVertice
    return redSinBucle

redBucles = redBucle1()
print("Red con bucles original:")
for arista in redBucles.obtener_aristas():
    print(arista)
    
redSinBucles = spanningTreeAlgorithm(redBucles)
print("Red sin bucles despues del algoritmo de Spanning Tree:")
for arista in redSinBucles.obtener_aristas():
    print(arista)