import sys 
import numpy as np
import torch
import time
import math 
from datetime import datetime
import argparse

from madrona_simple_example import GridWorld

#num_worlds = math.ceil(port_num/2)

# num_packet_total = int(sys.argv[3]) # the number of packet (in multi-steps) in total will be sent
# num_packet_perSender = num_packet_total/port_num
# step_num = math.ceil(num_packet_perSender/10) # 10 = LOOKAHEADT_TIME in types.hpp




parser = argparse.ArgumentParser(description='Process some parameters.')

# 添加参数
parser.add_argument('--num_env', type=int, required=True, help='Number of environments')
parser.add_argument('--enable_gpu_sim', type=str, required=True, help='Enable GPU simulation (e.g., "cpu" or "gpu")')
parser.add_argument('--fattree_K', type=int, required=True, help='Fattree K value')
parser.add_argument('--cc_method', type=int, required=True, help='Congestion control method')

# 解析参数
args = parser.parse_args()

# 打印解析的参数
print(f"Number of environments: {args.num_env}")
print(f"Enable GPU simulation: {args.enable_gpu_sim}")
print(f"Fattree K: {args.fattree_K}")
print(f"CC Method: {args.cc_method}")


num_worlds = args.num_env

enable_gpu_sim = False
if args.enable_gpu_sim == 'gpu':
    enable_gpu_sim = True

fattree_K = args.fattree_K
cc_method = args.cc_method



array_shape = [5,6]
walls = np.zeros(array_shape)
rewards = np.zeros(array_shape)
walls[3, 2:] = 1
start_cell = np.array([4,5])
end_cell = np.array([[4,5]])
rewards[4, 0] = -1
rewards[4, 5] = 1

print("start: ", "\n")

grid_world = GridWorld(num_worlds, start_cell, end_cell, rewards, walls, enable_gpu_sim, 0, fattree_K, cc_method)

start_time = time.time()

step_num = 10000
for i in range(step_num):
    # print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
    # print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n\n")
    if i % 1 == 0:
        print(f"The {i}-th time frame:\n")
    grid_world.step()
    # print("\n\n")

end_time = time.time()

execution_time = end_time - start_time

print(datetime.now())
print("step_num: ", step_num, "\n")
print(f"step function took {execution_time:.5f} seconds to execute.")

with open('./new_res.log', 'a') as f:
    finish_time = datetime.now()
    f.write(f"finish_time: {finish_time}\n")
    f.write(f"num_worlds: {num_worlds}\n")
    # f.write(f"num_packet_total: {num_packet_total}\n")
    f.write(f"step_num: {step_num}\n")
    f.write(f"step function took {execution_time:.5f} seconds to execute.\n\n")
    
