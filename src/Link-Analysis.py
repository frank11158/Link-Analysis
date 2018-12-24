import HITS
import PageRank
import SimRank
import sys
import pandas as pd
from optparse import OptionParser
import seaborn as sns
import matplotlib.pyplot as plt
import time

def parse_args():
    parser = OptionParser()
    parser.add_option('-f', '--inputFile',
                         dest='input',
                         help='File name',
                         default="../hw3dataset/graph_4.txt")
    parser.add_option('-m', '--method',
                         dest='method',
                         help='choose one algorithm of hits, pagerank, or simrank.',
                         default='hits')
    (options, args) = parser.parse_args()

    if options.input is not None:
            return options
    else:
            print('No specified dataset\n')
            sys.exit('System will exit')

def readGraph(filename):
    graph = {}
    f = open(filename, "r")
    loadData = f.read().splitlines()
    for line in loadData:
        a = line.split(",")
        if a[0] in graph.keys(): 
            graph[a[0]].append(a[1])
        else:
            graph[a[0]] = [a[1]]
    return graph

if __name__ == "__main__":
    options = parse_args()
    filename = options.input
    method = options.method
    # filename = "../hw3dataset/graph_3.txt"
    # method = 'pagerank'

    graph = readGraph(filename)
    if method == 'hits':
        tStart = time.time()
        (authority, hubness) = HITS.HITS(graph)
        tEnd = time.time()
        timeCost = tEnd - tStart
        with open("output.txt", 'w', encoding = 'UTF-8') as f:
            f.write("time cost: %f\n" % timeCost)
            f.write("HITS\n")
            f.write("   authority, hubness\n")
            for key in graph:
                f.write("%s: " % key)
                f.write("%f, " % authority[key])
                f.write("%f\n" % hubness[key])
        f.close()
    elif method == 'pagerank':    
        damp = 0.15
        tStart = time.time()
        pageRank = PageRank.PageRank(graph, damp)
        tEnd = time.time()
        timeCost = tEnd - tStart
        with open("output.txt", 'w', encoding = 'UTF-8') as f:
            f.write("time cost: %f\n" % timeCost)
            f.write("PageRank\n")
            for key in pageRank:
                f.write("%s: " % key)
                f.write("%f\n" % pageRank[key])
        f.close()
    elif method == 'simrank':
        c = 0.8 #decay factor
        tStart = time.time()
        simMatrix = SimRank.SimRank(graph, c)
        tEnd = time.time()
        timeCost = tEnd - tStart
        # df = pd.DataFrame.from_dict(simMatrix,orient='index').transpose()
        # # ax = sns.heatmap(df, cmap="YlGnBu", annot=True, fmt="f")
        # ax = sns.heatmap(df, cmap="YlGnBu")
        # label_y = ax.get_yticklabels()
        # plt.setp(label_y, rotation=45, horizontalalignment='right')
        # label_x = ax.get_xticklabels()
        # plt.setp(label_x, rotation=45, horizontalalignment='right')
        # plt.xlabel('vertex')
        # plt.ylabel('vertex')
        # plt.title('Heatmap')
        # plt.show()
        with open("output.txt", 'w', encoding = 'UTF-8') as f:
            f.write("time cost: %f\n" % timeCost)
            f.write("SimRank\n")
            for col in simMatrix:
                for row in simMatrix:
                    f.write("(%s, " % col)
                    f.write("%s): " % row)
                    f.write("%f\n" % simMatrix[col][row])
        f.close()
    else:
        print("invalid method.")
        sys.exit(0)

    