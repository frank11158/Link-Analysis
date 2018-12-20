def PageRank(graph, damp):
    pageRank = initializeRank(graph)
    
    while 1:
        result = {}
        diff = 0
        for key in pageRank:
            result[key] = 0
            for vertex in graph:
                links = len(graph[vertex])
                if key in graph[vertex]:
                    result[key] += pageRank[vertex]/links
            result[key] = (1-damp)*result[key] + damp*pageRank[key]
            # print(result)
            diff += abs(pageRank[key] - result[key])
        if diff > 0.001:
            pageRank = result.copy()
        else:
            break
    return pageRank

def initializeRank(graph):
    return dict(zip(graph.keys(), [1/len(graph)]*len(graph)))

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
    damp = 0.15
    graph = readGraph()
    print(graph)
    pageRank = PageRank(graph, damp)
    print("Page Rank: " + str(pageRank))
    for key in pageRank:
        print("%s: %f" % (key, pageRank[key]))

if __name__ == "__main__":
    main()