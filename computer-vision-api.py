#!/usr/bin/python
import requests, urllib, base64
import json, os.path

def read_file(filename):
  content = {}
  # Check the file is in current directory
  if os.path.isfile(filename):
    execfile(filename,content)
  else:
    print "Please check %s exists in the current directory" % (filename)
  return content

def analyzeImage(visionheaders,body):
  params = urllib.urlencode({
      'visualFeatures': 'Tags,Description,Adult',
      'language': 'en'
  })
  r = requests.post("https://westcentralus.api.cognitive.microsoft.com/vision/v1.0/analyze", json=body, headers=visionheaders, params=params)
  return json.loads(r.text)

def recognizeDomainSpecificContent(visionheaders,body):
  # There are only 2 models : "Celebrities" and "Landmarks" at the time of composition
  r = requests.post("https://westcentralus.api.cognitive.microsoft.com/vision/v1.0/models/celebrities/analyze", json=body, headers=visionheaders)
  return json.loads(r.text)

def analyzeFace(faceheaders,body):
  params = urllib.urlencode({
      'returnFaceLandmarks': 'True',
      'returnFaceAttributes': 'age,gender,smile,facialHair,glasses,emotion,hair,makeup,accessories'
  })
  r = requests.post("https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect", json=body, headers=faceheaders, params=params)
  return json.loads(r.text)

if __name__ == "__main__":
  API_key = read_file("key.txt")
  picture_list = read_file("pictureList.txt")
  
  confidence = 0.95

  visionheaders = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': API_key['vision'],
  }
  
  faceheaders = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': API_key['face'],
  }
  
  photoSource = picture_list['celebwglasses']
  print "This is the 1st API"
  result1 = analyzeImage(visionheaders,photoSource)
  print "Azure is %.2f%% confident of %s" % (result1['description']['captions'][0]['confidence']*100, result1['description']['captions'][0]['text'])
  
  print "\nThis is the 2nd API"
  result2 = recognizeDomainSpecificContent(visionheaders,photoSource)
  if not result2['result']['celebrities']:
    print "Azure has identified no celebrity."
  else:
    for j in range(len(result2['result']['celebrities'])):
      print "Azure is %.2f%% confident that there is a %s" % (result2['result']['celebrities'][j]['confidence']*100, result2['result']['celebrities'][j]['name'])
  
  print "\nThis is the 3rd API"
  result3 = analyzeFace(faceheaders,photoSource)
  for j in range(len(result3)):
    gender = "The person"
    if result3[j]['faceAttributes']['gender'] == "male": gender = "He"
    
    if result3[j]['faceAttributes']['gender'] == "female": gender = "She"
    
    for i in result3[j]['faceAttributes']['emotion'].keys():
      if result3[j]['faceAttributes']['emotion'][i] >= confidence: print "%s is emotionally showing %s" % (gender,i)
    
    print "%s is around %.1f years old" % (gender, result3[j]['faceAttributes']['age'])
    if result3[j]['faceAttributes']['makeup']['lipMakeup'] == "True": print "%s has applied lip makeup" % (gender)
    
    if result3[j]['faceAttributes']['makeup']['eyeMakeup'] == "True": print "%s has applied eye makeup" % (gender)
    
    print "%s is wearing %s" % (gender, result3[j]['faceAttributes']['glasses'])
    if result3[j]['faceAttributes']['hair']['invisible'] == False:
      if result3[j]['faceAttributes']['hair']['bald'] >= confidence: print "%s is bald" % (gender)
      
      for k in range(len(result3[j]['faceAttributes']['hair']['hairColor'])):
        if result3[j]['faceAttributes']['hair']['hairColor'][k]['confidence'] >= confidence: print "%s has %s hair color" % (gender, result3[j]['faceAttributes']['hair']['hairColor'][k]['color'])
    
    print "\n"
