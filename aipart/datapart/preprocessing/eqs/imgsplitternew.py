import PIL.Image
import imgtoolscustum
import PIL
import os
import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint


# img = PIL.Image.open(r'c:\Users\alima\OneDrive\Documents\GitHub\matwix2\aipart\datapart\preprocessing\eqs\img_1(23[multiply]6_goofrmv3.png').convert('L')
img = PIL.Image.open(r'C:\Users\alima\OneDrive\Documents\GitHub\matwix2\aipart\datapart\preprocessing\eqs\img_4)581=64_goofrmv2.png').convert('L')

img = imgtoolscustum.convert_img_2bw(img)


# plt.imshow(img)
# plt.show()


segments = imgtoolscustum.find_all_islands(img)


segments = sorted(segments, key= lambda i: min(i, key=lambda ind: ind[1])[1])


subimgs = [imgtoolscustum.blob2img(blob) for blob in segments]


prev_subimg_ = subimgs[0]
for sn, subimg in enumerate(subimgs[1:], start=1):
    
    if np.array_equal(prev_subimg_,subimg):
        print("match")
        
        # subimgs[sn] = segments
        blob1_info = imgtoolscustum.get_blob_info(segments[sn])
        blob2_info = imgtoolscustum.get_blob_info(segments[sn-1])
        
        ntop = blob1_info[1][0]
        nbottom = blob2_info[1][1]
        nleft = blob1_info[1][2]   #since same selft right shuld be same for both ?
        nright = blob2_info[1][3]
        
        nheight = ntop -nbottom
        nwidth = nright-nleft
        
        print(nheight, nwidth)
        print(ntop, nbottom, nleft, nright)
        
        new_subimg = np.zeros(( nheight + 6, nwidth + 6))
    
        for index in segments[sn].union(segments[sn-1]):
            
            new_subimg[index[0] - ntop + 3][index[1] - nleft + 3] = 1
        

        subimgs[sn] = new_subimg
        subimgs.pop(sn-1)
        
    
    else:
        pass
    
    prev_subimg_ = subimg
    
    
    

# for subimg in subimgs:
    
#     plt.imshow(subimg)
#     plt.show()



imgtoolscustum.show_subimgs_onRow(subimgs)

    
    


imgtoolscustum.show_points_onImg(img, segments)







