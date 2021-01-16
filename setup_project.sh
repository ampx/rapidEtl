#!/bin/bash

mkdir -p `dirname "$0"`/lib/
echo "Downloading LakeTools library ..."
wget -O `dirname "$0"`/lib/LakeToolsCommon.jar "https://drive.google.com/uc?export=download&id=1gP7dvtFGzLvJ5LkR2qz_bmM1aYTeov3S"
