
def create_line(inital_coords, final_coords):
    all_coordinates = []
    x0 = inital_coords[0]
    y0 = inital_coords[1]
    x1 = final_coords[0]
    y1 = final_coords[1]
    dx = x1 - x0
    dy = y1 - y0
    offset = 2*dy - dx
    print(dx)
    for i in range(dx):
        all_coordinates.append((x0, y0))
        if offset < 0:
            x0=x0+1
            y0=y0
            offset = offset + 2*dy
        else:
            x0=x0+1
            y0=y0+1
            offset = offset + 2*dy - 2*dx
    return all_coordinates
initial_coords = (1,2)
final_coords = (6,8)
created_line = create_line(initial_coords, final_coords)
print("created line coordinates = ", created_line)