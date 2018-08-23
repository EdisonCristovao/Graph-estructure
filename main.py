from GraphEstructure import GraphEstructure

def main():
    graph = GraphEstructure()
    graph.addVert("v1")
    graph.addVert("v2")
    graph.addVert("v3")
    graph.addVert("v4")
    graph.addVert("v5")

    graph.addEdge("v1", "v2")
    graph.addEdge("v1", "v3")
    graph.addEdge("v1", "v5")
    graph.showGraph();
    print("")
    graph.removeEdge("v1", "v2")
    graph.showGraph();
    graph.removeVert("v1")
    
    print("")
    graph.showGraph();

if __name__ == '__main__':
    main()
    