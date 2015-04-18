def find_path(source_point, destination_point, mesh):
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
        
    path.append(path_list)
    return (path, visited_nodes)