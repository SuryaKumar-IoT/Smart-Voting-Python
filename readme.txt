install Packages

pip install openpyxl
pip install xlrd
pip install xlsxwriter
pip install opencv-python
pip install boto3

How to run Program

Here Instead of real database I have collected some data and stored in xlcel file with name dataset

you need to run readdata.py in idle or command prompt

first it will ask you enter Aadhar Number

kindly check one Aadhar Number from dataset.xlsx

First Verification : Aadhar Verification

if Aadhar is found it will check whether the vote is casted before or not if not it will return the details of the person

Second Verfication : Voter ID Verification

It will ask you enter your Voter ID 

if voter id is matched from the fetched details it will show your mobile number for verification

Third Verification : Mobile Verification

Mobile Number Verfication

Here you can update your current mobile or you can use your registered mobile number

It will send OTP to your mobile number for verification you need to verify your otp

Fourth Verification : Face Recognition

Once your are verified it will ask you to keep your face infornt of camera

It will take snap and verify your face 

if matched it will ask you to cast your vote if your face is not matched it will not give access to cast your vote

How to check results

you can run showresult.py inorder to check results


