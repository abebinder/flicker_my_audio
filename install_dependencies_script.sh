#!/bin/bash
sudo apt-get update &&
sudo apt-get install python3-pip &&
sudo apt-get install ffmpeg libavcodec-extra &&
pip3 install -r requirements.txt