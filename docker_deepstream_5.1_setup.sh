sudo docker pull nvcr.io/nvidia/deepstream:5.1-21.02-devel
sudo docker run --gpus all -dit --name deepstream --rm --net=host --privileged -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY -w /opt/nvidia/deepstream/deedeepstream-5.1 nvcr.io/nvidia/deepstream:5.1-21.02-devel
sudo xhost +
sudo docker exec -it deepstream bash
apt-get update
apt install python3-gi python3-dev python3-gst-1.0 -y
apt-get install python3-pip python-dev -y
apt-get install -y build-essential
pip3 install --upgrade pip
apt-get update && apt-get install -y --no-install-recommends apt-utils
pip install setuptools --upgrade
apt-get install libglib2.0 libglib2.0-dev
apt-get install libjansson4  libjansson-dev
pip install pymongo
apt-get install -y python3-opencv
pip install pyyaml
apt install python3-pip -y
git clone https://github.com/NVIDIA-AI-IOT/deepstream_python_apps
apt install -y python3-gi python3-dev python3-gst-1.0 python-gi-dev git python-dev python3 python3-pip python3.8-dev cmake g++ build-essential libglib2.0-dev libglib2.0-dev-bin python-gi-dev libtool m4 autoconf automake
cd deepstream_python_apps/bindings/
git submodule update --init
apt-get install -y apt-transport-https ca-certificates -y
update-ca-certificates
cd ../3rdparty/gst-python/
./autogen.sh
make && make install
ldconfig
cd ../../bindings
mkdir build && cd build
cmake ..
make
apt install libgirepository1.0-dev libcairo2-dev -y
pip install ./pyds-1.1.3-py3-none-linux_x86_64.whl
cd ../../../

