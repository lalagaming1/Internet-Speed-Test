#Importing the speedtest module
import speedtest as st

Speed_Test = st.Speedtest(secure=True)
print("Getting download speed")
Download_Speed = Speed_Test.download()
Upload_Speed = Speed_Test.upload()
print("Getting upload speed")
results = f"Download speed: {Download_Speed}, Upload Speed: {Upload_Speed}" 
print(results)
