
def make_octal_part_of_circle(radius):
    x = 0
    y = radius
    x_offset = x + 1
    y_offset = y - 2
    all_coordinates = []
    marker = 1 - y
    while x < y:
        all_coordinates.append({marker:(x,y)})
        if marker < 0:
            marker = marker + 2*x_offset + 1    
            x = x + 1
            y  = y
        elif marker >= 0:
            marker = marker + 2*x_offset + 1 - 2*y_offset
            x = x + 1
            y = y - 1
        else:
            print("Invalid marker")
    return all_coordinates
create_circle = make_octal_part_of_circle(5)
print("octal part of created with points=", create_circle)