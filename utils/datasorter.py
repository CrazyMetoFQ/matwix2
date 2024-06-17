import os
import shutil
from pprint import pprint


mpath = "C:/Users/alima/OneDrive/Documents/GitHub/Ai-proj-mthsymb/aipart/data/htmlsynthdata_sym_raw/"

fls = os.listdir(mpath)
fls.remove("sorter.py")
flsd = [i for i in fls]


# rmv folders
for f in flsd:
    if not os.path.isfile(mpath+f):
        fls.remove(f)
    # elif "(" in f:
    #     os.remove(mpath+f)
        
        


pfls = [i.replace(".png","").replace("img_","").replace(" (1)","99").split("_") for i in fls]

# print(pfls)

    
for f,p in zip(fls,pfls):
    print(f, " | ",(p[0]))
    
    # print("dir",mpath+p[0])
    # print("parth", mpath+p[0]+f"/{f}")
    
    if not os.path.isdir(mpath+p[0]):
        os.mkdir(mpath+p[0])
    else:
        pass
    
    shutil.move(mpath+f, mpath+p[0]+f"/{f}")

# # check discrrepency
# dp = {}
# for i in pfls:
    
#     if i[0] in dp.keys():
#         pass
#     else:
#         dp[i[0]] = []
    
#     dp[i[0]].append(i[1])

# for k in dp:
    
#     dp[k].sort(key = int)


# # print(len(dp))
# # print(dp.keys())

# for k in dp:
    
#     if len(dp[k]) < 30:
#         print(f"{k}: {len(dp[k])}")
#         print(set(range(30))-set([int(i) for i in dp[k]]))
    
    