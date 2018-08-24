from GraphEstructure import GraphEstructure

def main():

    graph = buildGraph()
    graph.showGraph()

    graph.removeVert("INE5404")
    print("")
    graph.showGraph()

def buildGraph():

    graph = GraphEstructure()
    
    graph.addVert("EEL5105") # v1
    graph.addVert("EEL5105") # v1

    graph.addVert("INE5401") # v2
    graph.addVert("INE5402") # v3
    graph.addVert("INE5403") # v4
    graph.addVert("MTM3100") # v5
    graph.addVert("MTM3101") # v6
    graph.addVert("INE5404") # v7
    graph.addVert("INE5405") # v8
    graph.addVert("INE5406") # v9
    graph.addVert("INE5407") # v10
    graph.addVert("MTM3102") # v11
    graph.addVert("MTM5512") # v12
    graph.addVert("INE5408") # v13
    graph.addVert("INE5409") # v14
    graph.addVert("INE5410") # v15
    graph.addVert("INE5411") # v16
    graph.addVert("MTM5245") # v17
    graph.addVert("INE5412") # v18
    graph.addVert("INE5413") # v19
    graph.addVert("INE5414") # v20
    graph.addVert("INE5415") # v21
    graph.addVert("INE5416") # v22
    graph.addVert("INE5417") # v23
    graph.addVert("INE5418") # v24
    graph.addVert("INE5419") # v25
    graph.addVert("INE5420") # v26
    graph.addVert("INE5421") # v27
    graph.addVert("INE5422") # v28
    graph.addVert("INE5423") # v29
    graph.addVert("INE5424") # v30
    graph.addVert("INE5425") # v31
    graph.addVert("INE5426") # v32
    graph.addVert("INE5427") # v33
    graph.addVert("INE5430") # v34
    graph.addVert("INE5453") # v35
    graph.addVert("INE5428") # v36
    graph.addVert("INE5429") # v37
    graph.addVert("INE5431") # v38
    graph.addVert("INE5432") # v39
    graph.addVert("INE5433") # v40
    graph.addVert("INE5434") # v41

    graph.addEdge("MTM3100","MTM3101");
    graph.addEdge("MTM3100","MTM3101");

    graph.addEdge("INE5402","INE5404");
    graph.addEdge("MTM3101","INE5405");
    graph.addEdge("EEL5105","INE5406");
    graph.addEdge("MTM3101","MTM3102");
    graph.addEdge("INE5404","INE5408");
    graph.addEdge("MTM5512","INE5409");
    graph.addEdge("MTM3102","INE5409");
    graph.addEdge("INE5404","INE5410");
    graph.addEdge("INE5406","INE5411");
    graph.addEdge("MTM5512","MTM5245");
    graph.addEdge("INE5410","INE5412");
    graph.addEdge("INE5411","INE5412");
    graph.addEdge("INE5403","INE5413");
    graph.addEdge("INE5408","INE5413");
    graph.addEdge("INE5404","INE5414");
    graph.addEdge("INE5403","INE5415");
    graph.addEdge("INE5408","INE5415");
    graph.addEdge("INE5408","INE5416");
    graph.addEdge("INE5408","INE5417");
    graph.addEdge("INE5412","INE5418");
    graph.addEdge("INE5414","INE5418");
    graph.addEdge("INE5417","INE5419");
    graph.addEdge("MTM3102","INE5420");
    graph.addEdge("INE5408","INE5420");
    graph.addEdge("MTM5245","INE5420");
    graph.addEdge("INE5415","INE5421");
    graph.addEdge("INE5414","INE5422");
    graph.addEdge("INE5408","INE5423");
    graph.addEdge("INE5412","INE5424");
    graph.addEdge("INE5405","INE5425");
    graph.addEdge("INE5421","INE5426");
    graph.addEdge("INE5417","INE5427");
    graph.addEdge("INE5405","INE5430");
    graph.addEdge("INE5413","INE5430");
    graph.addEdge("INE5416","INE5430");
    graph.addEdge("INE5417","INE5453");
    graph.addEdge("INE5407","INE5428");
    graph.addEdge("INE5403","INE5429");
    graph.addEdge("INE5414","INE5429");
    graph.addEdge("INE5414","INE5431");
    graph.addEdge("INE5423","INE5432");
    graph.addEdge("INE5453","INE5433");
    graph.addEdge("INE5427","INE5433");
    graph.addEdge("INE5433","INE5434");

    return graph

if __name__ == '__main__':
    main()
    