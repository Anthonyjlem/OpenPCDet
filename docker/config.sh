#! /usr/bin/env bash

# Build component versions
CMAKE_VERSION=3.16
CMAKE_BUILD=5
PYTHON_VERSION=3.6
TORCH_VERSION=1.7
TORCHVISION_VERSION=0.8.1

# Workspace structure in docker
PCDET_ROOT=/root/pcdet
NUSC_ROOT=/root/nusc
CADC_ROOT=/root/cadc
KITTI_ROOT=/root/kitti
LOGDIR=/root/logdir

# Workspace structure on host machine
HOST_PCDET_ROOT=/home/anthony/Documents/OpenPCDet
HOST_NUSC_ROOT=/media/diskstation/datasets/nuScenes
HOST_CADC_ROOT=/media/diskstation/datasets/cadcd
HOST_KITTI_ROOT=/media/diskstation/datasets/KITTI
HOST_LOGDIR=/home/anthony/Documents/OpenPCDet/log

