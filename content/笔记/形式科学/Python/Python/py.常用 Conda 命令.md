##### 常用 Conda 命令
```shell
# 进入当前环境的python解释器，默认base环境
python

# 创建环境
conda create --name [yourEnv] python=[version]
# conda create --name data python=3.8

# 移除环境
conda env remove --name [yourEnv]
# conda env remove --name data

# 环境列表
conda info -e
conda env list

# 复制环境信息为yaml
conda env export > environment.yml  

# 从yaml重建环境
conda env create -f environment.yml  

# 镜像源
conda config --show-sources

# 添加镜像源
conda config --add channels
# conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
# conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
# conda config –-add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/free/
# conda config --add channels http://mirrors.aliyun.com/pypi/simple/

# 激活切换环境
conda activate 
# conda activate env-name

# 退出当前环境
conda deactivate

# 包列表
conda list

# 安装包
conda install
conda install --file
# conda install numpy
# conda install pandas
```
