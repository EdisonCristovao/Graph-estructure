from SubVertice import SubVertice

class Vertice:

    def __init__(self):
        self.name = ""
        self.subVertices = {}

    def addVert(self, name):
        #falta verificar se o vertice existe
        v = SubVertice()
        v.name = name;
        self.subVertices[name] = v