import numpy as np
import operator

def HITS(graph):
    graph = removeOutLinks(graph)
    authority = initializeAuthority(graph)
    hubness = None
    palink = gatParentLink(graph)
    authority_pre = None
    hubness_pre = None
    
    while 1:
        authority_new = {}
        hubness_new = {}
        authority_pre = authority.copy()
        if hubness != None:
            hubness_pre = hubness.copy()

        # calculate hubness
        for node in graph:
            hubness_new[node] = 0
            for child in graph[node]:
                hubness_new[node] += authority[child]
        hubness = normalize(hubness_new)

        # calculate authority
        for node in palink:
            authority_new[node] = 0
            for parent in palink[node]:
                authority_new[node] += hubness[parent]
        authority = normalize(authority_new)
        
        # caculate sum of difference
        diff = 0
        for item in authority:
            diff += abs(authority[item] - authority_pre[item])
            if hubness_pre != None:
                diff += abs(hubness[item] - hubness_pre[item])
        if diff < 0.001:
            break
        else:
            print(diff)
    return authority, hubness

def removeOutLinks(graph):
    for node in graph:
        outside_links = []
        for i in range(len(graph[node])):
            if graph[node][i] not in graph or graph[node][i] == node: outside_links.append(i)
        outside_links.reverse()
        for outside_link in outside_links:
            graph[node].pop(outside_link)
    return graph

def initializeAuthority(graph):
    return dict(zip(graph.keys(), [1]*len(graph)))

def gatParentLink(graph):
    parents = {}
    for node in graph:
        parents[node] = []
    for node in graph:
        for link in graph[node]:
            if link in parents.keys():
                parents[link].append(node)
            else:
                parents[link] = [node]
    print(parents)
    return parents

def normalize(obj):
    maxVal = obj[max(obj.items(), key=operator.itemgetter(1))[0]]
    for item in obj:
        obj[item] = float(obj[item])/maxVal
    return obj