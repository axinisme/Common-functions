import numpy as np
import math


def resamp_fun(data, target_freq, original_freq):
    print('开始重采样')
    print('原始采样频率：{}，目标采样频率：{}'.format(original_freq, target_freq))
    target_point_time = 1 / target_freq  # 目标采样频率，采样点间的时间间隔
    original_point_time = 1 / original_freq  # 原始采样频率，采样点间的时间间隔
    data_len = len(data)
    new_data = []
    # 下采样部分
    if original_freq > target_freq:
        portion = target_point_time / original_point_time
        i = 0  # 记录当前获取采样点的位置
        while i < data_len:  # 采样点位置不能超过数据的长度
            new_data.append(data[i])
            i = math.ceil(i + portion)

    return new_data
