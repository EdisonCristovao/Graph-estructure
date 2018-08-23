from Vertice import Vertice

class GraphEstructure:

    def __init__ (self):
        self.vertices = {}    

    def showGraph(self):
        for x in self.vertices:
            print("")
            print("{} ".format(self.vertices[x].name), end='')
            for y in self.vertices[x].subVertices:
                print("--> {}".format(self.vertices[x].subVertices[y].name), end='')

    def searchVert(self):
        return False
    
    def searchEdge(self):
        return False

    def addVert(self, name):
        #falta verificar se o vertice existe
        v1 = Vertice()
        v1.name = name;
        self.vertices[v1.name] = v1

    def addEdge(self, fromm, to):
        if self.existVert(fromm) and self.existVert(to):
            self.vertices[fromm].addVert(to)
            self.vertices[to].addVert(fromm)

    def removeVert(self, name):
        for x in self.vertices[name].subVertices:
            del(self.vertices[x].subVertices[name])
        del(self.vertices[name])

    def removeEdge(self, fromm, to):
        del(self.vertices[fromm].subVertices[to])
        del(self.vertices[to].subVertices[fromm])

    def existVert(self, name):
        if self.vertices[name].name != "":
            return True
        else:
            return False
    
    def existEdge(self):
        return False