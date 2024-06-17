import numpy as np
import matplotlib.pyplot as plt


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



def find_all_neighbours(img, points):   # need extra func cuz wierd behaviour in looped updating list
    # get neighbour of each in list
    
    extra = set()
    
    for item_index in points:
        extra = extra.union(find_neighbour(img, item_index))

    return extra # extra points found



def find_extra_lv3(img, extra_points_lv2, extra_points_lv1): # neatness

    extra_points_lv3 = find_all_neighbours(img, extra_points_lv2)
    extra_points_lv3 = extra_points_lv3.difference(extra_points_lv2).difference(extra_points_lv1)

    return extra_points_lv3



def show_points_onImg(img_og, points_list, special_point = None, vals=None, sval = None, cmap = "Spectral"):
      
    img = img_og.copy()
    
    if vals == None:
        vals = range(2, len(points_list)+2)
    else:
        pass
    
    if sval == None:
        sval = len(points_list) +3
        
    
    for val,points in zip(vals,points_list):
        for point in points:
    
            img[*point] = val
    
    if special_point != None:
        img[*special_point] = sval
    else:
        pass
    
    # Accent_r , OrRd
    plt.imshow(img*1, cmap=cmap) 
    plt.colorbar()
    plt.show()




def indsort(l): # L2R
    
    return sorted(l, key=lambda i: i[0]*100 + i[1])
    
    


def find_all_islands(img):

    xshape, yshape = img.shape

    
    all_islands = []

    for rowno in range(xshape):
        
        for colno in range(yshape):
            
            if img[rowno, colno] == 1 and not any((rowno, colno) in island for island in all_islands):
                
                current_index = (rowno, colno)
                all_neighbours = set([current_index])
                
    
                current_neighbours = set(find_neighbour(img, current_index))
                all_neighbours = all_neighbours.union(current_neighbours)
                

                nearby_points = find_all_neighbours(img, current_neighbours)
                nearby_points = nearby_points.difference(current_neighbours)
                all_neighbours = all_neighbours.union(nearby_points)
                

                
                extra_points_lv1 = current_neighbours.copy()
                extra_points_lv2 = nearby_points.copy()
                extra_points_lv3 = [None]
                
                cont = True
                while cont: 
                    
                    # print(f"in loop : lv3= {extra_points_lv3}")
                    extra_points_lv3 = find_extra_lv3(img, extra_points_lv2, extra_points_lv1)
                    all_neighbours = all_neighbours.union(extra_points_lv3)
                    
                    if extra_points_lv3 == set():
                        # print("HURRA")
                        cont = False
                        break
                    else:
                        pass
                    
                    extra_points_lv1 = extra_points_lv2
                    extra_points_lv2 = extra_points_lv3
                    
                all_islands.append(all_neighbours)
                    
                

            

    return all_islands


def convert_img_2bw(img): # grayscale inverse
    
    img = np.array(img)

    img = img/255
    img[img>0.5] = 1
    img[img<0.5] = 0
    img = (img-1) *-1
    img = img.astype(np.uint8)
    
    return img


def get_blob_info(blob):
    
    top = min(blob, key=lambda i: i[0])[0]
    bottom = max(blob, key=lambda i: i[0])[0]
    left = min(blob, key=lambda i: i[1])[1]
    right = max(blob, key=lambda i: i[1])[1]

    height = bottom-top
    width = right-left
    
    return ((height, width), (top, bottom, left, right))
    
    
def blob2img(blob, padding=3):
    
    (height, width), (top,bottom, left, right) = get_blob_info(blob)
    
    subimg = np.zeros((height+ 1+ padding*2, width+ 1+padding*2))
    
    for index in blob:
        
        subimg[index[0] - top + padding][index[1] - left + padding] = 1

    return subimg


def show_subimgs_onRow(subimgs):
    fig = plt.figure(figsize=(8, 8))

    columns = len(subimgs)
    rows = 1

    for i,subimg in zip(range(1, columns*rows +1), subimgs):
        
        fig.add_subplot(rows, columns, i)
        plt.imshow(subimg)
        plt.yticks([])
        plt.xticks([])

    plt.show()
    
    
# img = np.array(
#     [
#         [1,1,0,0,0],
#         [0,1,0,0,0],
#         [0,0,1,0,0],
#         [0,0,0,1,0],
#         [0,1,1,1,1]
        
#     ]
# )

# all_islands = find_all_islands(img)

# plt.imshow(img, cmap="binary")
# plt.show()
# show_points_onImg(img,all_islands, cmap="Spectral")