##  Model checkpoints
### ✍️ sam-3d-objects

```mermaid
graph TD
    A[download checkpoints<br>huggingface/modelscope] -->|copy/move| C
    B[sam-3d-objects] --> C[checkpoints/hf/]    
    C --> D[pipline.yaml]
    C --> E[Model Weights<br>.ckpt/.pt]
    C --> F[.yaml]
    
    %% 样式优化
    classDef dirStyle fill:#e1f5fe,stroke:#0277bd,stroke-width:2px,rounded:10px
    classDef coreDirStyle fill:#b3e5fc,stroke:#01579b,stroke-width:2px,rounded:10px
    classDef fileStyle fill:#f3e5f5,stroke:#7b1fa2,stroke-width:1px,rounded:5px
    class A,B,C dirStyle
    class D,E,F coreDirStyle
    class A fileStyle
```


---
### ✍️ moge:depth_model.model
Error for:
moge.model.v1.MoGeModel.from_pretrained
full_key: depth_model.model

HUGGINGFACE_HUB
- Windows: C:\Users\your_username\.cache\huggingface\hub\

# wait for modify local logic
### cacheed model Weights
```mermaid

graph TD
    A[HUGGINGFACE_HUB]-->|local cache|B[models--Ruicheng--moge-vitl/snapshots/]
    B-->C[like this:<br>979e84da9415762c30e6c0cf8dc<br>select to yourself]
    C-->D[model.pt]     
```
### local model Weights
you can set to yourself  path about model.pt
```mermaid
graph TD
    A[sam-3d-objects]-->|local|B[checkpoints/hf/]
    B-->C[pipeline.yaml]
    C-->E[model.pt]    


    C-->D[pretrained_model_name_or_path: Ruicheng/moge-vitl]
    D -->|modify| F["pretrained_model_name_or_path: checkpoints/hf/model.pt"]


      
```

***
### ✍️ facebookresearch/dinov2

TORCH_HUB
- Windows: C:\Users\your_username\\.cache\torch\hub\

>If error for downloading from github,do this. checkpoints will download auto


```mermaid

graph TD
    
     A-->|mannual|B2[facebookresearch_dinov2_main]       
    B2-->B21["facebookresearch/dinov2<br>source code"]

    A[TORCH_HUB]-->|auto|B1[checkpoints]
    B1-->B11[dinov2_vitl14_reg4_pretrain.pth]

   

 
        
```





## References
- [Acquiring Model Checkpoints](https://deepwiki.com/facebookresearch/sam-3d-objects/2.2-acquiring-model-checkpoints)
- [Ruicheng/moge-vitl](https://huggingface.co/Ruicheng/moge-vitl/resolve/main/model.pt)
- [facebookresearch/dinov2](https://github.com/facebookresearch/dinov2)

***