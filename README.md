# Multiverse Network Simulator

GPU Accelerated Network Discrete-event Simulator

# How to use this repository

This repository is extended from madrona_simple_example.


# At the beggining, make sure that cuda == 12.1(recommended 12.1), torch, cmake>=3.24(reommended 3.27) in your enviroment:

## 1 check the version of cuda using "$nvcc --version", if cuda is not >= 12.1, check whether there is cuda 12.1 using "ls /usr/local/cuda*"

If cuda 12.1 exists, specify the version of cuda in ~/.bashrc：
```bash 
export PATH=/usr/local/cuda-12.1/bin${PATH:+:${PATH}}
export LD_LIBRARY_PATH=/usr/local/cuda-12.1/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
```
else install cuda 12.1. 

## 2 install torch
```bash 
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

## 3 install cmake3.27(recommended)：

Download cmake3.27 from https://github.com/Kitware/CMake/releases/download/v3.27.6/cmake-3.27.6-linux-x86_64.sh, then
```bash 
$bash cmake-3.27.6-linux-x86_64.sh
```
Specify the path of cmake in ~/.bashrc：
```bash 
export PATH=your_directory/cmake-3.27.6-linux-x86_64/bin:$PATH
```



# Next, you should fetch the madrona_simple_example repo:
```bash
git clone --recursive git@github.com:Harnets/multiverse_network.git
```

# Thirdly, for Linux and MacOS: Run `cmake` and then `make` to build the simulator:
```bash
mkdir build
cd build
cmake ..
make -j # cores to build with
cd ..
pip install -e .
```

# In the third pahse, you can test the simulator(fattree k=4, 16 NPUs) as follows
```bash
cd your_directory/madrona_simple_example/
bash run.sh (gpu version) or bash run_cpu.sh (cpu --version)
```
if no error happens, success!!！


# How to inject traffic flows
Use the system of "comm_set_flow". Every NPUs would execute the system at every frame.
For example, build up 15 flows( 
1-th flow: NPU 0 --> NPU 1
2-th flow: NPU 1 --> NPU 2 
...
15-th flow: NPU 14 --> NPU 15
):

```cpp
inline void comm_set_flow(Engine &ctx, NPU_ID _npu_id,
                       NewFlowQueue &_new_flow_queue, SimTime &_sim_time,
                       SimTimePerUpdate &_sim_time_per_update) {
    if (_npu_id.npu_id >= 15) return;

    uint32_t src = _npu_id.npu_id;
    uint32_t dst = _npu_id.npu_id+1;
    int64_t flow_size = 1000;
    FlowEvent flow_event = {0, src, dst, 1, 0, flow_size, _sim_time.sim_time+2000, 0, FlowState::UNCOMPLETE};
    _enqueue_flow(_new_flow_queue, flow_event);
}
```
