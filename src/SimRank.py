def SimRank(graph, c):
    (transMatrix, simMatrix) = getInitMatrics(graph)
    result = getEmptyMatrix(graph)
    temp = getEmptyMatrix(graph)
    
    while 1:
        diff = 0
        # temp =  W^T * S
        for row in temp:
            for col in temp:
                _sum = 0
                for ele in transMatrix[row]:
                    _sum += transMatrix[row][ele]*simMatrix[col][ele]
                temp[col][row] = _sum
        # result = temp * W
        for row in simMatrix:
            for col in simMatrix:
                _sum = 0
                for ele in transMatrix[col]:
                    _sum += temp[ele][row]*transMatrix[col][ele]
                result[col][row] = _sum * c
                result[col][row] += (1-c) if col == row else 0
                diff += abs(simMatrix[col][row] - result[col][row])
        if diff > 0.001:
            simMatrix = result.copy()
            # print(simMatrix)
        else:
            break
    return simMatrix

def getEmptyMatrix(graph):
    matrix = {}
    for vertex1 in graph:
        matrix[vertex1] = {}
        for vertex2 in graph:
            matrix[vertex1][vertex2] = 0
    return matrix

def getInitMatrics(graph):
    transMatrix = {}
    simMatrix = {}
    parents = gatParentLink(graph)
    for key in parents:
        transMatrix[key] = {}
        for vertex in graph:
            transMatrix[key][vertex] = 1/len(parents[key]) if vertex in parents[key] else 0
    # simMatrix is initialized as an identity matrix
    for vertex1 in graph:
        simMatrix[vertex1] = {}
        for vertex2 in graph:
            simMatrix[vertex1][vertex2] = 1.0 if vertex1 == vertex2 else 0
    return transMatrix, simMatrix

def gatParentLink(graph):
    parents = {}
    for vertex in graph:
        parents[vertex] = []
    for vertex in graph:
        for link in graph[vertex]:
            if link in parents.keys():
                parents[link].append(vertex)
            else:
                parents[link] = [vertex]
    return parents

def readGraph():
    graph = {}
    f = open("../hw3dataset/graph_4.txt", "r")
    loadData = f.read().splitlines()
    for line in loadData:
        a = line.split(",")
        if a[0] in graph.keys(): 
            graph[a[0]].append(a[1])
        else:
            graph[a[0]] = [a[1]]
    return graph

def main():
    graph = readGraph()
    print(graph)
    simMatrix = SimRank(graph, 0.6)
    for col in simMatrix:
        for row in simMatrix:
            print("(%s, %s): %f" % (col, row, simMatrix[col][row]))

if __name__ == "__main__":
    main()