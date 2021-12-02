import numpy as np


def pic2data(img):
    """
    传入图片前景为255（白），背景为0（黑），将图片信号转换为采样信号
    :param img:
    :return:
    """
    nonzero_count = np.count_nonzero(img, axis=0).tolist()  # 找到传入图片中，每一列不为0数值的个数
    ecg_original_data = []  # 用来存储心电信号采样幅值的信息
    flag = True  # 用来标志当前的点是不是信号的第一个点
    for i in range(len(nonzero_count)):
        if nonzero_count[i] == 0:  # 如果为0，说明该列全部为背景，或是存在断点
            ecg_original_data.append(-1)
        else:
            max_index = img[:, i].nonzero()[0].max()
            min_index = img[:, i].nozero()[0].min()  # 求得当前列非0的最大最小行索引
            if flag:
                ecg_original_data.append(max_index)
                flag = False
            else:  # 还未考虑存在断点的情况
                k = (max_index - ecg_original_data[-1])  # 以前一个点为基准，计算当前点的斜率，两点在列索引上相差1
                if k <= 0:  # 斜率小于0，则说明该段处于上半部分
                    ecg_original_data.append(min_index)
                else:
                    ecg_original_data.append(max_index)  # 若不为0，说明该列有前景数据，将不为0数值行索引的最大值作为该点的幅值
    start = np.where(np.array(ecg_original_data) != -1)[0][0]
    end = np.where(np.array(ecg_original_data) != -1)[0][-1]  # 去除信号开始及结束之后的背景部分

    return ecg_original_data[start:end+1]