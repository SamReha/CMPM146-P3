from heapq import heappush, heappop

def find_path(source_point, destination_point, mesh):
    # Dijkstra's currently acting as BFS
    def dijk(src, dst, graph):
        dist = {}
        prev = {}
        q = []

        dist[src] = 0
        prev[src] = None
        heappush(q, (dist[src], src))

        while len(q) > 0:
            _, u = heappop(q)

            if u == dst:
                break

            neighborhood = graph['adj'][u]

            for neighbor in neighborhood:
                #alt = dist[u] + coordinate_distance(u, neighbor)
                if neighbor not in dist:# or alt < dist[neighbor]:
                    dist[neighbor] = alt
                    prev[neighbor] = u
                    heappush(q, (alt, neighbor))

        if u == dst:
            path = []
            while u:
                path.append(u)
                u = prev[u]
            # path.reverse() Uncomment this if we ever want to print the path out for the user
            return path
        else:
            return []
            
    def is_in_box(point, box):
        x = point[0]
        y = point[1]
        box_x1 = box[0]
        box_x2 = box[1]
        box_y1 = box[2]
        box_y2 = box[3]
        if x >= box_x1 and x <= box_x2 and y >= box_y1 and y <= box_y2:
            return True
        else:
            return False
    
    path=[]
    path_list = []
    visited_nodes=[]
    found_source = False
    found_dest = False
    
    # Find source and destination points within mesh:
    for box in mesh['boxes']:
        if is_in_box(source_point, box) and not found_source:
            path_list.append(source_point)
            visited_nodes.append(box)
        if is_in_box(destination_point, box) and not found_dest:
            path_list.append(destination_point)
            visited_nodes.append(box)
        if found_source and found_dest:
            break
            
    path_list = dijk(source_point, destination_point, mesh)
        
    path.append(path_list)
    return (path, visited_nodes)