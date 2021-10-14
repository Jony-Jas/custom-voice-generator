# custom-voice-generator

 Turn your own voice into computer generated voice. This app lets you to convert the text input into your own voice 
 This is a forked repository from <a href="https://github.com/CorentinJ/Real-Time-Voice-Cloning"/>Real-Time-Voice-Cloning<a>.
 For more deatils head over to the original repo :)


### Setup

#### 1. Install Requirements

**Python 3.6 or 3.7** is needed to run the toolbox.

* Install [PyTorch](https://pytorch.org/get-started/locally/) (>=1.0.1).
* Install [ffmpeg](https://ffmpeg.org/download.html#get-packages).
* Run `pip install -r requirements.txt` to install the remaining necessary packages.

#### 2. Download Pretrained Models
Download the latest [here](https://github.com/CorentinJ/Real-Time-Voice-Cloning/wiki/Pretrained-models).

#### 3. (Optional) Download Datasets
For playing with the toolbox alone, I only recommend downloading [`LibriSpeech/train-clean-100`](https://www.openslr.org/resources/12/train-clean-100.tar.gz). Extract the contents as `<datasets_root>/LibriSpeech/train-clean-100` where `<datasets_root>` is a directory of your choosing. Other datasets are supported in the toolbox, see [here](https://github.com/CorentinJ/Real-Time-Voice-Cloning/wiki/Training#datasets). You're free not to download any dataset, but then you will need your own data as audio files or you will have to record it with the toolbox.

#### 4. Launch the Web-app
To launch the web-app: you must setup the directory as per given below

> main-directory
>> \- voice-synthesizer-backend <br/> - original_audios <br/> - cloned_audios <br/> - voice-synthesizer-frontend <br/> - custom-voice-generator

- Code and steps to setup for ``` voice-synthesizer-backend ``` can be found <a href="https://github.com/Jony-Jas/voice-synthesizer-backend">here</a>🔗
- Code and steps to setup for ``` voice-synthesizer-frontend ``` can be found <a href="https://github.com/Jony-Jas/voice-synthesizer-frontend">here</a>🔗
- place the original audios in the ``` original_audios ``` folder
- Create an empty directory named ``` cloned_audios ```
 
 
## Screenshot
 
 ![Screenshot 2021-10-14 154114](https://user-images.githubusercontent.com/74784363/137297945-06d2ffe0-a39b-4062-b62f-5a95ae7164fb.png)


  


