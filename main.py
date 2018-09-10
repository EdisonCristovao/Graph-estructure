#OK = G.adicionaVértice(v)	        "Adiciona um novo vértice em G"
#OK = G.removeVértice(v)	        "Remove um  vértice de G, juntamente com todas as conexões"
#OK = G.conecta(v1,v2)	            "Conecta os vértices v1 e v2 em G"
#OK = G.desconecta(v1,v2)	        "Desconecta os vértices v1 e v2 em G"
#OK = G.ordem  Inteiro	            "Retorna o número de vértices de G"
#OK = G.umVértice  Vertice	        "Retorna um vértice qualquer de G"
#OK = G.grau(v)Inteiro	            "Retorna o número de vértices adjacentes a v em G" Ações Derivadas
#OK = G.vértices  Conjunto	        "Retorna um conjunto contendo os vértices de G"
#OK = G.adjacentes(v)Conjunto	    "Retorna um conjunto contendo os vértices adjacentes a v em G"



#G.éRegularBoolean	            "Verifica se todos os vértices de G possuem o mesmo grau"
#G.éCompletoBoolean	            "Verifica se cada vértice de G está conectados  a todos os outros vértices"
#G.fechoTransitivo(v)Conjunto	"Retorna um conjunto contendo todos os vértices de G que são transitivamente alcancáveis partindo-se de v"
#G.éConexoBoolean	            "Verifica se existe pelo menos um caminho que entre cada par de vértices de G"
#G.éÁrvoreBoolean	            "Verifica se não há ciclos em G"

from GraphEstructure import GraphEstructure

def main():

    g = buildGraph()
    g.showGraph()

    g.removeVertice("INE5404")
    print("")
    g.showGraph()
    print("")
    print("")
    print("Seu grafo tem {} vertices".format(g.ordem()))
    print("")
    verticeQulquer = g.umVertice().name
    print("Um vertice qualquer --> {}".format(verticeQulquer))
    print("Grau do vertice qualquer --> {}".format(g.grau(verticeQulquer)))
    print("")
    print("{}".format(g.copyVertices()))
    print("")
    print("{}".format(g.adjacentes(verticeQulquer)))

    

def buildGraph():

    g = GraphEstructure()
    
    g.adicionaVertice("EEL5105") # v1
    g.adicionaVertice("EEL5105") # v1

    g.adicionaVertice("INE5401") # v2
    g.adicionaVertice("INE5402") # v3
    g.adicionaVertice("INE5403") # v4
    g.adicionaVertice("MTM3100") # v5
    g.adicionaVertice("MTM3101") # v6
    g.adicionaVertice("INE5404") # v7
    g.adicionaVertice("INE5405") # v8
    g.adicionaVertice("INE5406") # v9
    g.adicionaVertice("INE5407") # v10
    g.adicionaVertice("MTM3102") # v11
    g.adicionaVertice("MTM5512") # v12
    g.adicionaVertice("INE5408") # v13
    g.adicionaVertice("INE5409") # v14
    g.adicionaVertice("INE5410") # v15
    g.adicionaVertice("INE5411") # v16
    g.adicionaVertice("MTM5245") # v17
    g.adicionaVertice("INE5412") # v18
    g.adicionaVertice("INE5413") # v19
    g.adicionaVertice("INE5414") # v20
    g.adicionaVertice("INE5415") # v21
    g.adicionaVertice("INE5416") # v22
    g.adicionaVertice("INE5417") # v23
    g.adicionaVertice("INE5418") # v24
    g.adicionaVertice("INE5419") # v25
    g.adicionaVertice("INE5420") # v26
    g.adicionaVertice("INE5421") # v27
    g.adicionaVertice("INE5422") # v28
    g.adicionaVertice("INE5423") # v29
    g.adicionaVertice("INE5424") # v30
    g.adicionaVertice("INE5425") # v31
    g.adicionaVertice("INE5426") # v32
    g.adicionaVertice("INE5427") # v33
    g.adicionaVertice("INE5430") # v34
    g.adicionaVertice("INE5453") # v35
    g.adicionaVertice("INE5428") # v36
    g.adicionaVertice("INE5429") # v37
    g.adicionaVertice("INE5431") # v38
    g.adicionaVertice("INE5432") # v39
    g.adicionaVertice("INE5433") # v40
    g.adicionaVertice("INE5434") # v41

    g.conecta("MTM3100","MTM3101");
    g.conecta("MTM3100","MTM3101");

    g.conecta("INE5402","INE5404");
    g.conecta("MTM3101","INE5405");
    g.conecta("EEL5105","INE5406");
    g.conecta("MTM3101","MTM3102");
    g.conecta("INE5404","INE5408");
    g.conecta("MTM5512","INE5409");
    g.conecta("MTM3102","INE5409");
    g.conecta("INE5404","INE5410");
    g.conecta("INE5406","INE5411");
    g.conecta("MTM5512","MTM5245");
    g.conecta("INE5410","INE5412");
    g.conecta("INE5411","INE5412");
    g.conecta("INE5403","INE5413");
    g.conecta("INE5408","INE5413");
    g.conecta("INE5404","INE5414");
    g.conecta("INE5403","INE5415");
    g.conecta("INE5408","INE5415");
    g.conecta("INE5408","INE5416");
    g.conecta("INE5408","INE5417");
    g.conecta("INE5412","INE5418");
    g.conecta("INE5414","INE5418");
    g.conecta("INE5417","INE5419");
    g.conecta("MTM3102","INE5420");
    g.conecta("INE5408","INE5420");
    g.conecta("MTM5245","INE5420");
    g.conecta("INE5415","INE5421");
    g.conecta("INE5414","INE5422");
    g.conecta("INE5408","INE5423");
    g.conecta("INE5412","INE5424");
    g.conecta("INE5405","INE5425");
    g.conecta("INE5421","INE5426");
    g.conecta("INE5417","INE5427");
    g.conecta("INE5405","INE5430");
    g.conecta("INE5413","INE5430");
    g.conecta("INE5416","INE5430");
    g.conecta("INE5417","INE5453");
    g.conecta("INE5407","INE5428");
    g.conecta("INE5403","INE5429");
    g.conecta("INE5414","INE5429");
    g.conecta("INE5414","INE5431");
    g.conecta("INE5423","INE5432");
    g.conecta("INE5453","INE5433");
    g.conecta("INE5427","INE5433");
    g.conecta("INE5433","INE5434");

    return g

if __name__ == '__main__':
    main()
    