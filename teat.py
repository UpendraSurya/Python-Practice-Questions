def filtering(namesss,max_length):
    return list(filter(lambda name: len(name)<=max_length,namesss))

namesss_k=["John","Smith","yuva","alex","narayana"]
short_ee=filtering(namesss_k,4)
print(short_ee)
#%%
