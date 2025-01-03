#!/bin/bash

# Setup script for WhisperX

# Tested for PyTorch 2.0, Python 3.10 (use other versions at your own risk!)
# GPU execution requires the NVIDIA libraries cuBLAS 11.x and cuDNN 8.x to be installed on the system.
# Please refer to the CTranslate2 documentation: https://opennmt.net/CTranslate2/installation.html

# 1. Create Python3.10 environment
echo "Creating Python 3.10 environment named 'whisperx'..."
conda create --name whisperx python=3.10
conda activate whisperx

# 2. Install PyTorch, e.g. for Linux and Windows CUDA11.8
echo "Installing PyTorch 2.0.0 with CUDA 11.8..."
conda install pytorch==2.0.0 torchaudio==2.0.0 pytorch-cuda=11.8 -c pytorch -c nvidia

# 3. Install WhisperX
echo "Installing WhisperX from PyPI..."
pip install whisperx

echo "Setup complete. You can now run WhisperX in the 'whisperx' conda environment and use this repo to name title for multiple Videos!"
