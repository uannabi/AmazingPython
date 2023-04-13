
import speedtest

test = speedtest.Speedtest()

download_speed=test.download()
upload_speed=test.upload()

print("Download Speed: ",download_speed)
print("Upload Speed: ",upload_speed)

