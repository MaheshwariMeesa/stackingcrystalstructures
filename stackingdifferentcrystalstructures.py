import os
import sys
import pandas as pd
import numpy as np
import dpdata

df1  = pd.DataFrame()
df2  = pd.DataFrame()
#################POSCAR_1################################

d_poscar1 = dpdata.System('POSCAR_73_1', fmt = 'vasp/poscar')
d_poscar2 = dpdata.System('POSCAR_73_2', fmt = 'vasp/poscar')
atom_types1 = d_poscar1['atom_types']
atom_types2 = d_poscar2['atom_types']
coord1 = d_poscar1['coords']
coord2 = d_poscar2['coords']


#df1 = pd.DataFrame(atom_types1, columns =['atomtype'])
df1['atom_type'] = atom_types1
df1['x'] = coord1[0,:,0]
df1['y'] = coord1[0,:,1]
df1['z'] = coord1[0,:,2] + 10.28572625

#df2= pd.DataFrame(atom_types1, columns =['atomtype'])
df2['atom_type'] = atom_types2
df2['x'] = coord2[0,:,0]
df2['y'] = coord2[0,:,1]
df2['z'] = coord2[0,:,2]
df3 = df1.append(df2, ignore_index=True)


df4 = df3.sort_values(by=['atom_type'])
df4.pop('atom_type')
np.savetxt(r'POSCAR', df4.values, fmt='%14.8f')