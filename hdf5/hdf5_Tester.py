#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 10:47:31 2016

@author: Nathan A Cheadle
"""

import h5py
import numpy as np

f = h5py.File("mytestfile.hdf5", "w")

dset = f.create_dataset("mydataset", (100,), dtype='i')

print(dset.shape)
print(dset.dtype)

dset[...] = np.arange(100)
print(dset[0])
print(dset[10])
print(dset[0:100:10])