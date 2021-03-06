# Microsoft Azure Computer Vision API
[![Build Status](https://travis-ci.org/josepipher/azure-computer-vision-api.svg?branch=master)](https://travis-ci.org/josepipher/azure-computer-vision-api)
[![codecov](https://codecov.io/gh/josepipher/azure-computer-vision-api/branch/master/graph/badge.svg)](https://codecov.io/gh/josepipher/azure-computer-vision-api)
[![HitCount](http://hits.dwyl.io/sanjose/azure-computer-vision.svg)](http://hits.dwyl.io/sanjose/azure-computer-vision)

This is inteded as a sample demonstration of using Azure Computer Vision API :
- Computer Vision API (Distill actionable information from images)
- Face API (Detect, identify, analyze, organize, and tag faces in photos)

You may obtain 2 separate trial keys from [here](https://azure.microsoft.com/en-us/try/cognitive-services/), one for each API.

## Required libraries
```linux
pip install -r requirements.txt
```

## Running the script
```linux
python azure-computer-vision-api.py <computer vision API key> <face API key>
```
For example,
```linux
python azure-computer-vision-api.py abcxxxxxxxxxxxxxxxxxx efgxxxxxxxxxxxxxxxxxxx
```
The script assumes the existence of a **pictureList.txt** file in the current directory.

## Sample Input (generally available from the web)
![Input photo](http://www.herworldplus.com/sites/default/files/Amber%20Kuo%20and%20Hong%20Kong%20actor%20Nick%20Cheung.jpg)

## Sample Results
```linux
This is the 1st API
Azure is 96.85% confident of a couple of people posing for the camera

This is the 2nd API
Azure has identified no celebrity.

This is the 3rd API
He is emotionally showing happiness
He is around 38.1 years old
He is wearing Sunglasses
He is bald

She is emotionally showing happiness
She is around 25.5 years old
She is wearing NoGlasses
She has black hair color

```
