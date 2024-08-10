#First, make a virtual environment called 'pipertts'
virtualenv pipertts

# Specify the Python 3 interpreter (use v3.9 or higher)
virtualenv -p /usr/bin/python3  pipertts

#Activate the venv
source pipertts/bin/activate

#promt now looks like:
(pipertts) pi@raspberrytts:~/tts $

#Deactivate:
deactivate
	
#Once the virtual environment has been activated, Python usage proceeds in the normal fashion.
#Running python or pip will be done in the context of the virtual environment.
#Modules installed with pip will be placed in the local venv folders - sudo should not be used.

#Installing Dependencies in Virtual Environment Python (the name of this Pi is 'raspberrytts')
(pipertts) pi@raspberrytts:~ $

#piper install
#check python version (need 3.9)
python -V

#get pip3
sudo apt-get install python3-pip

#modules needed:
#search for module: apt search numpy
pip install numpy
pip install psutil #cpu info
pip install httplib2 #for retrieving web data to speak
pip install time
pip install sounddevice
pip install scipy
sudo apt-get install libportaudio2
sudo apt-get install libasound2-dev
pip install piper-tts

#download voices:
cd ~/pipertts/lib/python3.11/site-packages/piper/
cd /home/pi/pipertts/lib/python3.11/site-packages/piper/

wget https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_US/joe/medium/en_US-joe-medium.onnx
wget https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_US/joe/medium/en_US-joe-medium.onnx.json

#call test program
python piper_example.py

#for playing wav files:
#put audio files in same dir as python program that plays them
pip install soundfile
sudo apt-get install libsndfile1
pip install RPi.GPIO

#example
python playsound_example.py


#To autostart venv at startup
#To auto start on login only:
sudo nano /home/pi/.bashrc

#add to bottom of bashrc file:
source ~/pipertts/bin/activate #activate virtual environment
cd pipertts #go to dir
python piper_example.py #start python program
