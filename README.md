# Microsoft Azure Computer Vision API
This is inteded as a sample demonstration of using Azure Computer Vision API :
- Computer Vision API (Distill actionable information from images)
- Face API (Detect, identify, analyze, organize, and tag faces in photos)

You may obtain 2 separate trial keys from [here](https://azure.microsoft.com/en-us/try/cognitive-services/), one for each API.

## Insert your API keys into the **key.txt** file
vision = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
face = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

## Required libraries
```linux
pip install -r requirements.txt
```

## Running the script
```linux
python azure-computer-vision-api.py
```
The script assumes the existence of a **key.txt** and a **pictureList.txt** files in the current directory.

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
