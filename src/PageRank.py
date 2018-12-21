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
