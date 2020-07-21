
import numpy as np
import matplotlib.pyplot as plt

import svmbir


sino = np.load('data/sinodata.npy')
weight = np.load('data/weightdata.npy')

# svmbir_lib : contains system matrix : defaults to ~/svmbir_lib directory
# delete everything else by default

# x = svmbir.recon(sino, wght, angles, SigmaX=0.6350, T=0.000478, svmbir_lib=/depot/user/smajee/svmbir_lib)
# x = svmbir.recon(sino, wght, angles, SigmaX=0.6350, T=0.000478)


mbir_data_path='data/sv-mbirct_data/'
mbir_params_path='data/sv-mbirct_params/'
object_name='object'
NViews = 288
NSlices = 1
NChannels = 512

angles = np.linspace(0, np.pi, NViews, endpoint=False)

svmbir.init_geometry_data(mbir_data_path, mbir_params_path, object_name,
                angles=angles, NChannels=NChannels, NViews=NViews, NSlices=NSlices, 
                CenterOffset=-6, img_downsamp=4)

svmbir.gen_sysmatrix(mbir_data_path, mbir_params_path, object_name)

x = svmbir.recon(mbir_data_path, mbir_params_path, object_name, 
                sino=sino, wght=weight, SigmaX=0.6350, T=0.000478)

# display reconstruction
imgplot = plt.imshow(x[0])
imgplot.set_cmap('gray')
plt.colorbar()
plt.savefig('data/recon.png')
plt.show()

