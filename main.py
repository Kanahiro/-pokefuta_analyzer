import csv
import numpy as np
from scipy.spatial import distance
from ortoolpy import tsp

asahikawa_airport = [142.4541427, 43.6708414]
shinchitose_airport = [141.6811815, 42.7876057]
shinkansen_hokuto = [140.6486832, 41.9046279]

start_point = shinkansen_hokuto
nodes = [start_point]

with open('./pokefuta_coordinates.csv') as f:
    reader = csv.reader(f)
    header = next(f)
    for row in reader:
        nodes.append([ row[2], row[1] ])

print(nodes)
dist = distance.cdist(nodes, nodes)
print(tsp(nodes, dist))