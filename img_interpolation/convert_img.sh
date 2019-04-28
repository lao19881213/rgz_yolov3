#!/bin/bash 

# Peel, selfcal and image data

#SBATCH --partition=gpu
#SBATCH --time=23:00:00
#SBATCH --job-name=convert
#SBATCH --nodes=1
#SBATCH --mem=60gb
#SBATCH --output=/mnt/beegfs/home/blao/kch/keras-yolo3/VOC2007/convert.o%A_%a
#SBATCH --error=/mnt/beegfs/home/blao/kch/keras-yolo3/VOC2007/convert.e%A_%a
#SBATCH --export=all


source /mnt/beegfs/home/blao/kch/bashrc

python /mnt/beegfs/home/blao/kch/keras-yolo3/VOC2007/covert_img.py
