from Vertice import Vertice
from random import randint


class GraphEstructure:

    def __init__ (self):
        self.vertices = {}    

    def showGraph(self):
        i = 0
        for x in self.vertices:
            print("")
            print("{} ==>>{}".format(i, self.vertices[x].name), end='')
            i += 1
            for y in self.vertices[x].subVertices:
                print(" --> {}".format(self.vertices[x].subVertices[y].name), end='')

    def adicionaVertice(self, name):
        if not self.existVert(name):
            v1 = Vertice()
            v1.name = name;
            self.vertices[v1.name] = v1
        else:
            print("Vertice {} já existe!".format(name))

    def conecta(self, fromm, to):
        if self.existVert(fromm) and self.existVert(to) and not self.existEdge(fromm, to):
            self.vertices[fromm].adicionaVertice(to)
        else:
            print("Aresta {}-->{} já existe!".format(fromm, to))

    def removeVertice(self, name):
        delList = []
        if self.existVert(name):
            for x in self.vertices:
                if self.vertices[x].existVert(name):
                    del(self.vertices[x].subVertices[name])
            del(self.vertices[name])
        else:
            print("Vertice {} não existe!".format(name))

    def desconecta(self, fromm, to):
        if self.existVert(fromm) and self.existVert(to) and self.existEdge(fromm, to):
            del(self.vertices[fromm].subVertices[to])
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

    def ordem(self):
        return len(self.vertices)
    
    #aqui ele só ta retornando um vertice sem suas arestas.
    def umVertice(self):
        v = Vertice()
        index = randint(0,self.ordem()-1)
        for x in self.vertices:
            if index == 0:
                v.name = self.vertices[x].name
                return v;
            index -= 1
        return v
    
    def grau(self, name):
        grau = 0
        for x in self.vertices[name].subVertices:
            grau += 1
        return grau

    def copyVertices(self):
        verticesCopy = {}
        for x in self.vertices:
            v = Vertice()
            v.name = self.vertices[x].name
            verticesCopy[v.name] = v
        return verticesCopy

    def adjacentes(self, name):
        verticesCopy = {}
        for x in self.vertices[name].subVertices:
            v = Vertice()
            v.name = self.vertices[x].name
            verticesCopy[v.name] = v
        return verticesCopy
