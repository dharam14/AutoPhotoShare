import sys
from imageCapture import detect_bounding_box, video_capture_script
from cmpImg import similar_images, image_resizer
import logFile

def complete_mobile_number(mobile_number,log_file_name):
    if mobile_number.startswith('+'):
        print("Mobile number already has a country code.")
        return mobile_number
    country_code = input("Enter your country code (e.g., US, UK, IN): ").upper()    
    country_codes = {'US': '+1','UK': '+44',
                     'IN': '+91','CA': '+1',}
    if country_code not in country_codes:
        print("!!!Invalid country code!!!")
        logFile.write_to_log(f"Invalid mobile no.: {mobile_number}",log_file_name)
        os.remove(log_file_name)
        sys.exit()
    complete_number = country_codes[country_code] + mobile_number
    return complete_number

log_file_name = 'log.txt'
logFile.first_log(log_file_name)

x = int(input("Select option: \n"+ "1. Capture photo\n"+"2. Enter image path manually\n"))
if x == 1: 
    logFile.write_to_log("selected to capture a photo",log_file_name)
    captured_image = video_capture_script(log_file_name)
    logFile.write_to_log(f"captured image path: {captured_image}",log_file_name)
elif x == 2: 
    logFile.write_to_log("selected to enter image path manually",log_file_name)
    captured_image = input("Enter image path\n")
    logFile.write_to_log(f"provided image path: {captured_image}",log_file_name)
else:
    logFile.write_to_log(f"invalid selection Program terminated.",log_file_name)
    os.remove(log_file_name)
    sys.exit()

directory_path = r'C:\Users\gargg\OneDrive\Desktop\APS\Database'
logFile.write_to_log(f"path: {directory_path}",log_file_name)
similar_image_path = similar_images(captured_image,directory_path,log_file_name)

phone_number = input("Enter your mobile number: ")
complete_phone_number = complete_mobile_number(phone_number,log_file_name)
caption = "Extract this file to get images"
logFile.write_to_log(f"Mobile no: {complete_phone_number}",log_file_name)
logFile.write_to_log(f"Caption: {caption}",log_file_name)

import os
import zipfile
zip_file_name = 'SimilarImages.zip'
with zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
    # add each image to the ZIP file
    for image_path in similar_image_path:
        zipf.write(image_path) # include only the image file name in the ZIP file
    zipf.write('log.txt') # write the log file into the ZIP file
print("zip create success")

os.remove(log_file_name)
os.remove(captured_image)

import sendFile
sendFile.whats_send_file(complete_phone_number, zip_file_name, caption)