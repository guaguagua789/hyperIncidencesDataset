import numpy as np
import pickle
import scipy.sparse as sp

# 204、612、1020节点数量
node_num =[204,612,1020]
with open('hyperEdges_'+str(node_num[1])+'.pkl','rb') as file:
    hyperEdges = pickle.load(file)
[incidence_matrix, dic_hyper_num_random,
 indices_random, indices2_random,community_labels] = hyperEdges

#超关联矩阵csr格式，各类超边数量字典，节点类型编号，节点子类型编号，社区标签

a=1