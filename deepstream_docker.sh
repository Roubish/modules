docker-compose --version
sudo curl -L "https://github.com/docker/compose/releases/download/1.27.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version


sudo apt install curl
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list
sudo apt-get install -y nvidia-docker2
sudo apt-get update && sudo apt-get install -y nvidia-container-toolkit
sudo systemctl restart docker
sudo xhost +
sudo docker run --gpus all -dit --name deepstream --rm --net=host --privileged -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY -w /opt/nvidia/deepstream/deepstream-6.1 nvcr.io/nvidia/deepstream:6.1-devel
sudo docker exec -it deepstream bash


mv ../../mahi_logi/ .
cd mahi_logi/nvdsinfer_custom_impl_Yolo/
make clean
make
cd ..
python3 deepstream_nvdsanalytics.py file:///opt/nvidia/deepstream/deepstream-6.1/sources/deepstream_python_apps/apps/mahi_logi/00000000173000200.mp4 


#%%  YOLOV5 DOCKER CONTAINER 

sudo docker run --gpus all --ipc=host --ulimit memlock=-1 --ulimit stack=67108864 -dit --name yolov5 --rm --net=host --privileged -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY  ultralytics/yolov5:latest
sudo docker exec -it yolov5 bash
