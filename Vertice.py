from SubVertice import SubVertice

class Vertice:

    def __init__(self):
        self.name = ""
        self.subVertices = {}

    def adicionaVertice(self, name):
        #falta verificar se o vertice existe
        v = SubVertice()
        v.name = name;
        self.subVertices[name] = v

    def existVert(self, name):
        try:
            if self.vertices[name].name != "":
                return True
        except:
            return False