from Vertice import Vertice

class GraphEstructure:

    def __init__ (self):
        self.vertices = {}    

    def showGraph(self):
        for x in self.vertices:
            print("")
            print("{}".format(self.vertices[x].name), end='')
            for y in self.vertices[x].subVertices:
                print(" --> {}".format(self.vertices[x].subVertices[y].name), end='')

    def searchVert(self):
        return False
    
    def searchEdge(self):
        return False

    def addVert(self, name):
        if not self.existVert(name):
            v1 = Vertice()
            v1.name = name;
            self.vertices[v1.name] = v1
        else:
            print("Vertice {} já existe!".format(name))

    def addEdge(self, fromm, to):
        if self.existVert(fromm) and self.existVert(to) and not self.existEdge(fromm, to):
            self.vertices[fromm].addVert(to)
           # self.vertices[to].addVert(fromm)
        else:
            print("Aresta {}-->{} já existe!".format(fromm, to))

    def removeVert(self, name):
        if self.existVert(name):
            del(self.vertices[name])
        else:
            print("Vertice {} não existe!".format(name))

    def removeEdge(self, fromm, to):
        if self.existVert(fromm) and self.existVert(to) and self.existEdge(fromm, to):
            del(self.vertices[fromm].subVertices[to])
        #del(self.vertices[to].subVertices[fromm])
        else:
            print("Aresta {}-->{} não existe!".format(fromm, to))

    def existVert(self, name):
        try:
            if self.vertices[name].name != "":
                return True
        except:
            return False
    
    def existEdge(self, fromm, to):
        try:
            if self.vertices[fromm].subVertices[to].name != "":
                return True
        except:
            return False