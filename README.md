# Install Cuda Libraries
> Dependecies CUDA 10.0 & CuDNN v7.5.
## Installing Cuda 
1. [Download Cuda](https://developer.nvidia.com/cuda-10.0-download-archive)
2. Select Linux and ubuntu and follow all steps
3.  From the terminal:
    
    ```
    nano /home/username/.bashrc
    
    # or
    
    nano /home/$USER/.bashrc
    
    ```
    
4.  Inside there add the following:
    
    ```
    export PATH=/usr/local/cuda-10.0/bin${PATH:+:${PATH}}$ 
    export LD_LIBRARY_PATH=/usr/local/cuda-10.0/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
    ```
## Install CUDNN v7.5
1. [Get the CUDNN Package From Here](https://developer.nvidia.com/rdp/cudnn-archive#a-collapse750-10)
2. Unzip the tar file
3. Copy the following files into the CUDA Toolkit directory, and change the file permissions.
```
$ sudo cp cuda/include/cudnn.h /usr/local/cuda/include
$ sudo cp cuda/lib64/libcudnn* /usr/local/cuda/lib64
$ sudo chmod a+r /usr/local/cuda/include/cudnn.h /usr/local/cuda/lib64/libcudnn*
```

# Git Clone Repo
```git
git clone https://github.com/mozilla/DeepSpeech.git
```


# Creating Virtual ENV
```
pip3 install --upgrade virtualenv
```
```
sudo apt install virtualenv
```
```
virtualenv -p python3 venv
```
```
source venv/bin/activate
```
# Install all the packages
```
pip install deepspeech-gpu
```
1.  Delete the `requirements.txt`
2. Create a New `requirements.txt`
3. Paste the following in it!
```
# Main training requirements
tensorflow == 1.15.0
numpy == 1.16.0
progressbar2
pandas
six
pyxdg
attrdict
absl-py

# Requirements for building native_client files
setuptools

# Requirements for importers
sox
bs4
requests
librosa
soundfile

# Miscellaneous scripts
paramiko >= 2.1
scipy
matplotlib
webrtcvad
```
4. Install the requirements.txt
```
pip install -r requirements.txt
```
# Running The Code [CLI]
```
deepspeech --model deepspeech-0.5.1-models/output_graph.pbmm --alphabet deepspeech-0.5.1-models/alphabet.txt --lm deepspeech-0.5.1-models/lm.binary --trie deepspeech-0.5.1-models/trie --audio audio/2830-3980-0043.wav
```
# Running the Python Code 
```
python test_client.py --aggressive 1 --model deepspeech-0.5.1-models/ --audio audio/2830-3980-0043.wav
```
