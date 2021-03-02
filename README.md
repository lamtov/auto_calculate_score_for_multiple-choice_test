## Build window 
```sh
conda create -n multiple_choise python=3.7 pyinstaller
conda activate multiple_choise
pip install opencv-python
conda install -y -c anaconda tk
conda install -y -c anaconda pillow
conda  install  -y -c anaconda numpy
conda install -y -c conda-forge imutils
conda install   -y -c anaconda flask
```

## RUN
```sh
git clone https://github.com/lamtov/auto_calculate_score_for_multiple-choice_test.git
cd auto_calculate_score_for_multiple-choice_test
conda activate multiple_choise
python main.py
```
