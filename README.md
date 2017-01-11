# segmentation
Deep learning is used for segmentation. This is based on caffe. Yon can do it as :
# 1.caffe 
# linux:
# 安装git：sudo apt-get install git
# 下载caffe： git clone https://github.com/BVLC/caffe.git
# 安装依赖项：sudo apt-get install libprotobuf-dev libleveldb-dev libsnappy-dev libopencv-dev libhdf5-serial-dev protobuf-compiler
# sudo apt-get install --no-install-recommends libboost-all-dev
# sudo apt-get install libatlas-base-dev
# sudo apt-get install python-dev
# sudo apt-get install libgflags-dev libgoogle-glog-dev liblmdb-dev
# sudo apt-get install python-lmdb

# 配置文件的修改
# cp Makefile.config.example Makefile.config
# 修改需编译的选项)(针对ubuntu15.04以及之后的版本，之前的版本不用修改，用于解决无法找到hdf5.h等文件)
# 在INCLUDE_DIR 后添加 /usr/lib/x86_64-linux-gnu/hdf5/serial/include
# LIBRARY_DIR /usr/lib/x86_64-linux-gnu/gnu/hdf5/serial

# 编译：
# make all -j4
# make test -j4
# make runtest
# python 接口
# make pycaffe
# export PYTHONPATH=/home/francis/caffe/python





https://github.com/yosinski/deep-visualization-toolbox

