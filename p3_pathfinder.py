from heapq import heappush, heappop
from math import sqrt

def find_path(source_point, destination_point, mesh):
    # Dijkstra's currently acting as BFS
    def A_star(src, dst, graph):
        dist = {}
        prev = {}
        detail_points = {}
        q = []      # Note, treat q as a priority queue
        detail_points[src] = source_point
        detail_points[dst] = destination_point
        dist[src] = 0
        prev[src] = None
        heappush(q, (dist[src], src))

        while len(q) > 0:
            _, u = heappop(q)

            if u == dst:
                break

            neighborhood = graph['adj'].get(u, [])

            for neighbor in neighborhood:
                u_coord = detail_points[u]
                u_x = u_coord[0]
                u_y = u_coord[1]
                neighbor_x1 = neighbor[0]
                neighbor_x2 = neighbor[1]
                neighbor_y1 = neighbor[2]
                neighbor_y2 = neighbor[3]
                
                neighbor_coord = (min(neighbor_x2-1,max(neighbor_x1,u_x)), min(neighbor_y2-1,max(neighbor_y1,u_y)))
                detail_points[neighbor] = neighbor_coord
                
                alt = dist[u] + coordinate_distance(detail_points[u], detail_points[neighbor]) # Setting alt to 0 makes this behave like BFS
                
                if neighbor not in dist or alt < dist[neighbor]:
                    visited_nodes.append(neighbor)
                    dist[neighbor] = alt# 
                    prev[neighbor] = u
                    heappush(q, (alt + coordinate_distance(detail_points[neighbor], destination_point), neighbor))

        if u == dst:
            path = []
            detail_points[src] = source_point
            detail_points[dst] = destination_point
            while u:
                prev_u = prev[u]
                if prev_u is not None:
                    path.append((detail_points[u], detail_points[prev_u]))
                u = prev_u
            # path.reverse() Uncomment this if we ever want to print the path out for the user
            return path
        else:
            return []
            
    def coordinate_distance(coord1, coord2):
        x1 = coord1[0]
        x2 = coord2[0]

        y1 = coord1[1]
        y2 = coord2[1]

        return sqrt((x1-x2)**2+(y1-y2)**2)
            
    def is_in_box(point, box):
        x = point[0]
        y = point[1]
        box_x1 = box[0]
        box_x2 = box[1]
        box_y1 = box[2]
        box_y2 = box[3]
        if x > box_x1 and x <= box_x2 and y > box_y1 and y <= box_y2:
            return True
        else:
            return False
    
    path_list = []
    visited_nodes = []
    source_box = None
    destination_box = None
    found_source = False
    found_dest = False
    
    # Find source and destination points within mesh:
    for box in mesh['boxes']:
        if is_in_box(source_point, box) and not found_source:
            source_box = box
            path_list.append(source_point)
        if is_in_box(destination_point, box) and not found_dest:
            destination_box = box
            path_list.append(destination_point)
        if found_source and found_dest:
            break
    
    if source_box == destination_box:
        path_list = [source_point, destination_point]
        visited_nodes=[source_box]
    else:
        path_list = A_star(source_box, destination_box, mesh)
        
    if len(path_list) is 0:
        print "No path could be found!"
    return (path_list, visited_nodes)