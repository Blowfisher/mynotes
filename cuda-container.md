Centos 系统 安装NVIDIA 驱动
========================
```
  驱动地址：https://www.nvidia.com/Download/index.aspx

  选择版本：Tesla Driver for Linux x64 Version: 410.129  CUDA Toolkit: 10.0

  410.129版本安装脚本地址:https://us.download.nvidia.com/tesla/410.129/NVIDIA-Linux-x86_64-410.129-diagnostic.run
  安装指引: https://docs.nvidia.com/datacenter/tesla/tesla-installation-notes/index.html

验证：
  nvidia-smi


Container使用 GPU
Centos安装 nvidia-container-runtime


yum源安装

配置Dockerd
sudo mkdir -p /etc/systemd/system/docker.service.d
sudo tee /etc/systemd/system/docker.service.d/override.conf <<EOF
[Service]
ExecStart=
ExecStart=/usr/bin/dockerd --host=fd:// --add-runtime=nvidia=/usr/bin/nvidia-container-runtime
EOF
sudo systemctl daemon-reload
sudo systemctl restart docker

github: https://github.com/NVIDIA/nvidia-container-runtime
## 添加 --add-runtime=nvidia=/usr/bin/nvidia-container-runtime

Dockerd daemon.json文件配置 添加：

sudo tee /etc/docker/daemon.json <<EOF
{
    "default-shm-size": "5G",
    "runtimes": {
        "nvidia": {
            "path": "/usr/bin/nvidia-container-runtime",
            "runtimeArgs": []
        }
    }
}
EOF

修改 /etc/nvidia-container-runtime/ 配置文件

验证：
docker run -it --rm --gpus all ubuntu nvidia-smi
```
