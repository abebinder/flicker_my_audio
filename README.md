# flicker_my_audio

My friend Aidan told me LED lights have a refresh rate (they turn on and off rapidly, producing what looks like a steady 
stream of light). He wondered what that refresh rate would sound like if applied to audio. This script will take in 
mp3 audio and add silence at regular intervals. This will create repeated cycles of audio then silence mimicking the 
refresh rate of an LED. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and 
testing purposes.

### Prerequisites

python3


### Installing

If on a debian system, you can run

```
install_dependencies_script.sh
```
to get all the dependencies you need to run this project. Note the script asks for sudo privileges, run at your own 
risk. 

Else, use [this readme section](https://github.com/jiaaro/pydub#getting-ffmpeg-set-up) to install audio dependencies 
that 
pydub needs.

Then run

```
pip3 install -r requirements.txt
```


## Running the tests

``` python3 test.py ```


## Libraries Used

* [pydub by jiaaro](https://github.com/jiaaro/pydub) - Easy audio manipulating in python
* [progress](https://pypi.org/project/progress/) - Progress bars


## License

This project is licensed under the MIT License - see the LICENSE file for details

## Acknowledgments

* jiaaro for awesome pydub library
* Aidan Marvick for asking the question  "What would an LED light sound like?"
