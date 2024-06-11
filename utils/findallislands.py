import numpy as np
import matplotlib.pyplot as plt



img = np.array(
    [
        [1,1,0,0,0],
        [0,1,0,0,0],
        [0,0,1,0,0],
        [0,0,0,1,0],
        [0,1,1,1,1]
        
    ]
)



def find_neighbour(img, index, to_detect =1): 
    
    row,col = index
    rowshape,colshape = img.shape
    neighbour_list = []
    
    # 8 possiblities
    
    # top left
    if row > 0 and col > 0 and  img[row-1, col-1] == to_detect:
        neighbour_list.append((row-1, col-1))
    else:pass
    
    # top middle
    if row > 0 and img[row-1, col] == to_detect:
        neighbour_list.append((row-1, col))
    else:pass
    
    # top right
    if row > 0 and col < colshape-1 and  img[row-1, col+1] == to_detect:
        neighbour_list.append((row-1, col+1))
    else:pass
    
    
    # middle left
    if col > 0 and  img[row, col-1] == to_detect:
        neighbour_list.append((row, col-1))
    else:pass
    
        # middle right
    if col < colshape-1 and  img[row, col+1] == to_detect:
        neighbour_list.append((row, col+1))
    else:pass
        
    
    # bottom left
    if row<rowshape-1 and col > 0 and  img[row+1, col-1] == to_detect:
        neighbour_list.append((row+1, col-1))
    else:pass
    
    # bottom middle
    if row<rowshape-1 and  img[row+1, col] == to_detect:
        neighbour_list.append((row+1, col))
    else:pass
    
    # bottom right
    if row<rowshape-1 and col < colshape-1 and  img[row+1, col+1] == to_detect:
        neighbour_list.append((row+1, col+1))
    else:pass
    

    return neighbour_list



def check_neighbour_of_neighbours(img, neighbours):   # need extra func cuz wierd behaviour in looped updating list
    
    extra = []
    
    for item_index in neighbours:
        
        print(f"FROM checkneihgbours func| checking neighbour {item_index}")
        
            
        extra.extend(find_neighbour(img, item_index))

        extra = list(set(extra))
        
        print(f"FROM checkneihgbours func| current neighbours {neighbours}")

    return extra


xshape,yshape = img.shape


neighbour_list = []

for row in range(xshape):
    print(f"r{row}")
    
    for col in range(yshape):
        print(f"c{col}")
        
        current_item = img[row][col]
        
        if current_item == 1 and not any((row,col) in sublist for sublist in neighbour_list):
            
            print(f"item found @ {(row,col)}")
            
            neighbours = find_neighbour(img, (row,col))
            neighbours.append((row,col))

            print(f"neighbours at start {[neighbours]}")
            
            extra = check_neighbour_of_neighbours(img, neighbours)
            neighbours.extend(extra)
            neighbours = list(set(neighbours))
            print("tri 2")
            extra = check_neighbour_of_neighbours(img, neighbours)
            neighbours.extend(extra)
            neighbours = list(set(neighbours))
            print("tri 3")
            extra = check_neighbour_of_neighbours(img, neighbours)
            neighbours.extend(extra)
            neighbours = list(set(neighbours))
            print("tri 4")
            extra = check_neighbour_of_neighbours(img, neighbours)
            neighbours.extend(extra)
            neighbours = list(set(neighbours))
            
            neighbours.sort(key=lambda i: (i[0]+i[1])*10 + i[0])
                
            
            neighbour_list.append(neighbours)
            
        


print(neighbour_list)

plt.imshow(img)
plt.show()


# neighbour_list = []

# for rs, row in enumerate(img):
#     print("r")

#     for rc, col in enumerate(row):
#         print("c")
        
#         if col == 1 and not any((rs, rc) in sublist for sublist in neighbour_list):
#             print("-"*8)

#             neighbours = find_neighbour(img, (rs,rc))
#             neighbours.append((rs,rc))
#             print("el og",(rs,rc))
#             for element_index in neighbours:
                
#                 print(element_index)
#                 neighbours.extend(find_neighbour(img, element_index))
                
#                 neighbours = list(set(neighbours))
            
#             # neighbour_list.append(neighbours)
#             neighbour_list.append(sorted(neighbours, key= lambda i: i[0]+i[1]))
            
            
                
            
        
    
# print(neighbour_list)

# plt.imshow(img)
# plt.show()