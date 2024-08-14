def goto(x, y):
    yDist = get_pos_y() - y  # Positive if drone is north of the target space
    xDist = get_pos_x() - x  # Positive if drone is east of the target space
    halfWorldSize = get_world_size()/2
    while get_pos_y() != y:
        if yDist >= halfWorldSize or (-halfWorldSize <= yDist and yDist < 0):
            move(North)
        else:
            move(South)
    while get_pos_x() != x:
        if xDist >= halfWorldSize or (-halfWorldSize <= xDist and xDist < 0):
            move(East)
        else:
            move(West)


def fieldGrid(size, element):
    xArr = []
    for x in range(size):
        yArr = []
        for y in range(size):
            yArr.append(element)
        xArr.append(yArr)
    return xArr
    
def plant_grass():
	if get_ground_type() == Grounds.Soil:
		till()

def get_inventory():
	Inventory = []
	for I in Items:
		#print(I)
		if num_items(I) > 0:
			Inventory.append([I,num_items(I)])
	return Inventory

def is_over(E):	
		if get_entity_type() == E:
			return True
		elif get_ground_type() == E:
			return True
		else: 
			return False

