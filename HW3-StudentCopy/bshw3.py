# Use https://www.si.umich.edu/programs/bachelor-science-
# information/bsi-admissions as a template.
# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.
import requests
import re
from bs4 import BeautifulSoup

url = 'https://www.si.umich.edu/programs/bachelor-science-information/bsi-admissions'
request = requests.get(url)
soup = BeautifulSoup(request.text, "html.parser")

# find all the image tags and replace with new image
for img in soup.find_all('img'):
    img['src'] = "media/logo.png"

# replace the main image, which is in an iframe
iframe = soup.find('iframe')
iframe['src'] = "media/pic_to_use.jpg"
# change height/width so it looks better
iframe['width'] = "154"
iframe['height'] = "154"

# find all tags with text Student or student
student_tags = soup.find_all(text=re.compile('[Ss]tudent'))

# replace occurences of Student and student
for tag in student_tags:
    temp_string = tag.string
    temp_string = temp_string.replace("student", "AMAZING student")
    temp_string = temp_string.replace("Student", "AMAZING Student")
    tag.replaceWith(temp_string)

# write to ouput file
with open("output.html", "w+") as file:
    file.write(soup.prettify())
