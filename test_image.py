# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import math


# %%
p1 = {'size': [640,320]}
p2 = {'size': [1980,1024]}
coords = [[[15,15],[50,50]],
         [[15,30],[50,250]],
         [[30,30],[250,250]],
         [[30,15],[250,50]]]
a_d = 5
d_d = 25


# %%
def transform(point, size_old, size_new):
    x_old = point[0]
    y_old = point[1]

    whidth_new = size_new[0]
    height_new = size_new[1]

    whidth_old = size_old[0]
    height_old = size_old[1]
    
    x_new = (x_old*whidth_new)/whidth_old
    y_new = (y_old*height_new)/height_old
    return [x_new, y_new]


# %%
def dot(vA, vB):
    return vA[0]*vB[0]+vA[1]*vB[1]
def ang(lineA, lineB):
    vA = [(lineA[0][0]-lineA[1][0]), (lineA[0][1]-lineA[1][1])]
    vB = [(lineB[0][0]-lineB[1][0]), (lineB[0][1]-lineB[1][1])]
    dot_prod = dot(vA, vB)
    magA = dot(vA, vA)**0.5
    magB = dot(vB, vB)**0.5
    cos_ = dot_prod/magA/magB
    angle = math.acos(dot_prod/magB/magA)
    ang_deg = math.degrees(angle)%360

    if ang_deg-180>=0:
        return 360 - ang_deg
    else: 

        return ang_deg


# %%
def validate(size_l, size_r, coords, angle_deviation_limit, dist_deviation_limit):
    coords_copy = coords.copy()
    for point_pair in coords_copy:
        point_pair[0] = transform(point_pair[0], size_l, size_r)    
    left = []
    right = []
    for pair in coords_copy:
        left.append(pair[0])
        right.append(pair[1])    
    sections_left = []
    for i in range(len(left)):
        sections_left.append([left[i-1], left[i]])
    sections_right = []
    for i in range(len(right)):
        sections_right.append([right[i-1], right[i]])       
    distances_left = []
    for sect in sections_left:
        distances_left.append(math.sqrt((sect[1][0] - sect[0][0])**2 + (sect[1][1] - sect[0][1])**2))
    distances_right = []
    for sect in sections_right:
        distances_right.append(math.sqrt((sect[1][0] - sect[0][0])**2 + (sect[1][1] - sect[0][1])**2))  
    for dist_pair in zip(distances_left, distances_right):
        dist_deviation = dist_pair[0]/dist_pair[1]*100
        if  dist_deviation > dist_deviation_limit:
            print(dist_deviation)
            raise Exception('distance deviation limit is exceeded')
    for i in zip(sections_left,sections_right):
        section_left, section_right = i
        angle = ang(section_left, section_right) 
        if angle > angle_deviation_limit:
            print(angle)
            raise Exception('angle deviation limit is exceeded')
    return True


# %%
validate(p1['size'], p2['size'], coords.copy(), a_d, d_d)




