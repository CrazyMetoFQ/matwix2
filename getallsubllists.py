# from pprint import pprint
# import matplotlib.pyplot as plt
import time

start = time.perf_counter()
def sublists(l):
    # suls = []
    # cnt = 0
    
    # for i in range(len(l)):
        
    #     for j in range(len(l)):
            
    #         j += i+1
    #         # print(i,j,l[i:j])
            
    #         suls.append(l[i:j])
    #         cnt+=1
    
    ln = range(len(l))
    suls = [[l[i:i+j+1] for j in ln] for i in ln]
    
    # print(f"LEN: {len(l)} | CNT = {sum([len(i) for i in suls])}") 

    # # rl = [list(i) for i in sorted(list(set((tuple(i) for i in suls))), key = lambda i: i[0]**3 * len(i) )]
    # rl = [list(set([tuple(j) for j in i])) for i in suls]
    # rl = sorted(rl, key = lambda i: i[0][0])
    # rl = [sorted(i, key = lambda c: len(c)) for i in rl]
    
    # rl = suls

    # return rl
    return suls


for _ in range(1):
    sublists(range(10000))

end = time.perf_counter()
print(f"time taken: {end-start}")


# l = range(1,101)
# # l = list(l)
# rl = sublists(l)
# # print([i for i  in l])
# # pprint(rl)
# print(rl)
# print(len(l))
# print(sum([len(i) for i in rl]))


# d = "".join(" ".join([str(i), str(len(sublists(range(i))))])+'\n' for i in range(10))
# print(d)

# d = [len(sublists(range(i))) for i in range(100)]


# print("\n".join([str(i) for i in d]))




# x,y = zip(*d)

# plt.plot(x, y)

# plt.show()
    
    