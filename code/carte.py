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
            # axs[row, col].annotate(grid[row,col], xy=(0.5, 0.1), xycoords='axes fraction')
            collegi=pd.DataFrame(id[id['id']==grid[row,col]])
            if collegi['partito politico'].item()=="monarchici":
                axs[row,col].set_facecolor('navy')
            elif collegi['partito politico'].item()=="socialisti":
                axs[row,col].set_facecolor('crimson')
            elif collegi['partito politico'].item()=="radicali":
                axs[row,col].set_facecolor('lime')
            elif collegi['partito politico'].item()=="clericali":
                axs[row,col].set_facecolor('gold')
            elif collegi['partito politico'].item()=="repubblicani":
                axs[row,col].set_facecolor('gray')

axs[17,25].annotate('Roma',xy=(0.5,0.5),xytext=(-1,-6),arrowprops=dict(facecolor='black', shrink=0.05),xycoords='axes fraction')
axs[5,13].annotate('Milano',xy=(0.5,0.5),xytext=(-3.5,4),arrowprops=dict(facecolor='black', shrink=0.05),xycoords='axes fraction')
axs[18,30].annotate('Napoli',xy=(0.5,0.5),xytext=(-1,-6),arrowprops=dict(facecolor='black', shrink=0.05),xycoords='axes fraction')

title= "Results of the Italian general election in 1913"
font_params = {'fontfamily':'serif',
               'fontname': 'Times New Roman',
               'fontsize': 20, 'weight': 'bold'}
fig.text(x=0.3,y=0.9,s=title, **font_params)

fig.text(0.15,0.40,'Results',fontsize=15,weight='bold',fontname='Times New Roman')
fig.text(0.15, 0.38, 'Monarchici : 309 seats',
         va='center', 
         fontsize=10, color='navy')
fig.text(0.15, 0.35, 'Socialisti : 79 seats',
         va='center',
         fontsize=10, color='crimson')
fig.text(0.15, 0.32, 'Radicali : 73 seats',
         va='center', 
         fontsize=10, color='lime') 
fig.text(0.15, 0.29, 'Clericali : 31 seats',
         va='center', 
         fontsize=10, color='gold')
fig.text(0.15, 0.26, 'Repubblicani : 16 seats',
         va='center', 
         fontsize=10, color='gray')

plt.show()