import boto3
ACCESS_ID = "Replace with your ID"
ACCESS_KEY = "Replace with your secret key"
REGION = "eu-west-1"
def face_reg(REGION,ACCESS_ID,ACCESS_KEY,source='images/1.jpg',target='target.jpg'):
    # Replace sourceFile and targetFile with the image files you want to compare.
    sourceFile=source
    targetFile=target
    client=boto3.client('rekognition',region_name=REGION,aws_access_key_id=ACCESS_ID,
         aws_secret_access_key= ACCESS_KEY)

    imageSource=open(sourceFile,'rb')
    imageTarget=open(targetFile,'rb')
    try:
     response=client.compare_faces(SimilarityThreshold=70,
                                  SourceImage={'Bytes': imageSource.read()},
                                  TargetImage={'Bytes': imageTarget.read()})
    except:
     print("Face not detected, Invalid Image")
     return(0)
    faceMatchFlag=0
    for faceMatch in response['FaceMatches']:
        faceMatchFlag=1
        position = faceMatch['Face']['BoundingBox']
        confidence = str(faceMatch['Face']['Confidence'])
        print('Face Matched')
        return(1)
    if faceMatchFlag==0:
        print ('Not Matched')
        return(0)
    imageSource.close()
    imageTarget.close()

'''t=face_reg(REGION,ACCESS_ID,ACCESS_KEY,source='images/surya.jpg',target='target.jpg')
print(t)'''
