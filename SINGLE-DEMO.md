# Run notebook demo
##### *Make sure you can connect to huggingface when you run jupyter notebook or lab.*


## Run demo_single_object.ipynb

### Dependencies
#### pip install and uninstall gsplat

```bash

pip install omegaconf
pip uninstall gsplat

# If necessory, run lower setuptools version to test
# pip install setuptools==72.1.0

```
#### Build and Install gsplat Mannually
##### Build gsplat
```bash
# gitclone gsplat
git clone https://github.com/nerfstudio-project/gsplat.git
git checkout 2323de5905d5e90e035f792fe65bad0fedd413e7
git submodule update --init --recursive

# Build gsplat
# Build  visual studio installer 2022  C++ 桌面开发
# select core/win 10/11 sdk/c++ build tools/c++ core features
# I use "x64 Native Tools Command Prompt for VS 2022" to build gsplat

# Set Environment Variable
# python -c "import torch; print('GPU 型号:', torch.cuda.get_device_name(0)); print('CUDA 架构:', torch.cuda.get_device_capability(0))"
# GPU 型号: NVIDIA GeForce RTX 3050 4GB Laptop GPU
# CUDA 架构: (8, 6)   -> set TORCH_CUDA_ARCH_LIST=8.6

# GPU 型号: NVIDIA GeForce RTX 4090
# CUDA 架构: (8, 9)    -> set TORCH_CUDA_ARCH_LIST=8.9
set SETUPTOOLS_USE_DISTUTILS="stdlib"
set TORCH_CUDA_ARCH_LIST=8.9


```

##### Install gsplat
```bash
pip install . --no-build-isolation
```

#### Run 
```bash
# Add conda env 'sam-3d' to jupyter kernel
python -m ipykernel install --user --name=sam-3d

# jupyter kernelspec uninstall sam-3d

# sam-3d-objects
jupyter notebook notebook/demo_single_object.ipynb
# Select Kernel sam-3d
```


## Run demo_multi_object.ipynb

### Watting for update...
