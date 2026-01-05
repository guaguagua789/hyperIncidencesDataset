import numpy as np
import pickle
import scipy.sparse as sp


def load_hyper_data(target_node_num: int):
    """
    加载指定节点数量的超图数据

    参数:
        target_node_num: 目标节点数量，必须是 [204, 612, 1020] 中的一个

    返回:
        incidence_matrix: 超关联矩阵，csr稀疏格式
        dic_hyper_num_random: 各类超边数量的字典
        indices: 节点类型编号
        indices_sub: 节点子类型编号
        community_labels: 社区标签
    """
    # 校验输入的节点数量是否合法
    valid_node_nums = [204, 612, 1020]
    if target_node_num not in valid_node_nums:
        raise ValueError(f"节点数量必须是 {valid_node_nums} 中的一个，当前输入: {target_node_num}")

    # 构建文件名并尝试加载数据
    filename = f'hyperEdges_{target_node_num}.pkl'
    try:
        with open(filename, 'rb') as file:
            hyper_edges_data = pickle.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"未找到数据文件: {filename}，请检查文件是否存在")
    except Exception as e:
        raise RuntimeError(f"加载数据时发生错误: {str(e)}")

    # 校验数据结构完整性
    if len(hyper_edges_data) != 5:
        raise ValueError(f"数据文件格式错误，预期包含5个变量，实际包含: {len(hyper_edges_data)}个")

    # 解包并返回五个变量（与注释对应）
    incidence_matrix, dic_hyper_num_random, indices, indices_sub, community_labels = hyper_edges_data
    return incidence_matrix, dic_hyper_num_random, indices, indices_sub, community_labels


# 示例用法（可根据需要修改节点数量）
if __name__ == "__main__":
    try:
        # 加载612节点的数据
        inc_mat, hyper_num_dict, node_indices, node_subindices, comm_labels = load_hyper_data(612)
        print("数据加载成功:")
        print(f"超关联矩阵形状: {inc_mat.shape}")
        print(f"超边数量字典: {hyper_num_dict}")
        print(f"节点类型编号数量: {len(node_indices)}")
        print(f"节点子类型编号数量: {len(node_subindices)}")
        print(f"社区标签数量: {len(comm_labels)}")
    except Exception as e:
        print(f"操作失败: {e}")
