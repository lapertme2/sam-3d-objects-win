## install environments
```bash
conda create -n sam-3d python=3.11
conda activate sam-3d

pip install cython requests zstandard 

pip install torch==2.5.1 torchvision==0.20.1 torchaudio==2.5.1 --index-url https://download.pytorch.org/whl/cu121

```
```bash
git config --global http.sslVerify false

pip install -r requirements-customed.txt

git config --global http.sslVerify true
```
 
 ```bash
pip install kaolin==0.18.0 -f https://nvidia-kaolin.s3.us-east-2.amazonaws.com/torch-2.5.1_cu121/kaolin-0.18.0-cp311-cp311-win_amd64.whl
pip install https://github.com/MiroPsota/torch_packages_builder/releases/download/pytorch3d-0.7.8%2B5043d15/pytorch3d-0.7.8%2B5043d15pt2.5.1cu121-cp311-cp311-win_amd64.whl
```

## model checkpoints
#### sam-3d-objects/checkpoints
>use huggingface to download or modelscope to download
move all download files to sam-3d-objects\checkpoints\hf\


#### use local moge model checkpoints

```bash
# If error for downloading full_key: depth_model.model
# Mannual download from huggingface
#https://huggingface.co/Ruicheng/moge-vitl/resolve/main/model.pt?download=true
# move to checkpoints/hf/
# pretrained_model_name_or_path: Ruicheng/moge-vitl
# modify "pretrained_model_name_or_path"   of checkpoints\hf\pipeline.yaml like this
pretrained_model_name_or_path: checkpoints/hf/model.pt

```


#### modify notebook/inference.py like this
```bash

BLACKLIST_FILTERS = [
    lambda target: get_method(target)
    in {
        builtins.exec,
        builtins.eval,
        builtins.__import__,
        os.kill,
        os.system,
        os.putenv,
        os.remove,
        os.removedirs,
        os.rmdir,
        #os.fchdir,
        #os.setuid,
        #os.fork,
        #os.forkpty,
        #os.killpg,
        os.rename,
        os.renames,
        os.truncate,
        os.replace,
        os.unlink,
        #os.fchmod,
        #os.fchown,
        #os.chmod,
        #os.chown,
        #os.chroot,
        #os.fchdir,
        #os.lchown,
        os.getcwd,
        #os.chdir,
        shutil.rmtree,
        shutil.move,
        shutil.chown,
        subprocess.Popen,
        builtins.help,
    },
]
```
## RUN DEMO
```bash
python demo.py
```