
def create_line(inital_coords, final_coords):
    all_coordinates = []
    x0 = inital_coords[0]
    y0 = inital_coords[1]
    x1 = final_coords[0]
    y1 = final_coords[1]
    dx = x1 - x0
    dy = y1 - y0
    if abs(dx) >= abs(dy):
        steps = abs(dx)
    else:
        steps = abs(dy)
    x_inc = dx/steps
    y_inc = dy/steps
    while x0<=x1  or y0<=y1:
        all_coordinates.append((x0, y0))
        x0 = round(x0 + x_inc)
        y0 = round(y0 + y_inc)
    return all_coordinates

initial_coords = (2,1)
final_coords = (4,5)
created_line = create_line(initial_coords,final_coords)
print("coordinates of created line =",created_line)