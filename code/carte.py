import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

grid=pd.read_csv("../grid.csv",header=None)
id=pd.read_csv('../id.csv',dtype='string',usecols=[0,3])

nbrows,nbcols=grid.shape
fig, axs = plt.subplots(nrows=nbrows,ncols=nbcols, figsize=(12,6))

grid=grid.to_numpy()

rows_to_remove=[]

for i in range (nbrows):
    for j in range (nbcols):
        if grid[i,j]=="   ":
            rows_to_remove.append((i,j))
        else:
            rows_to_remove.append('')

# print(rows_to_remove)

for row in range(nbrows):
    for col in range(nbcols):
        if (row,col) in rows_to_remove:
            axs[row, col].axis('off')
        else :
            # axs[row, col].set_title(f"({row},{col})",fontsize=3)
            
            axs[row, col].set_xticks([])
            axs[row, col].set_yticks([])
            axs[row, col].annotate(grid[row,col], xy=(0.5, 0.1), xycoords='axes fraction')
            collegi=pd.DataFrame(id[id['id']==grid[row,col]])
            if collegi['partito politico '].item()=="monarchici":
                axs[row,col].set_facecolor('orange')

plt.show()