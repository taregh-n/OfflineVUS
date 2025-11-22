from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from os import path, makedirs
from time import sleep
import requests
import re

# Define Functions

def goToCoursesList(courses_list_url):
    driver.get(courses_list_url)
    
def getSelectedSemester():
    semester = driver\
    .find_element(
        'xpath',
        '//*[@id="edSemester"]/option[@selected="selected"]'
    ).get_attribute("value")
    return semester

def getCourseName(course_code):
    course_name = driver.find_elements(
        'xpath',
        f'//tr/td[starts-with(@ident, "SRL={course_code}")]'
    )[2].text
    return course_name.strip()

def clickOnVirtualClassList():
    driver.find_element('xpath', '//tr[@id="trVirtualClassList"]').click()
    
def getClassLinks():
    class_elements = driver.find_elements('xpath', '//td[@onclick]')
    class_links = [i.get_attribute("onclick")[10:-2] for i in class_elements]
    for i in class_links:
        if '?html-view=true' in i:
            class_links.remove(i)
    return class_links

def makeCourseDir(semester, course_name):
    course_dir = path.join(f'./{semester}', f'{course_name}/')
    if not path.exists(course_dir):
        makedirs(course_dir)
    return course_dir

# -------------------------------------------------------

def getFileNameId(class_url):
    try:
        return re.findall(r'shirazu\.ac\.ir/(\w*)', class_url)[0]
    except:
        return None

def makeDownloadUrl(file_name, semester):
    return f'https://offline.shirazu.ac.ir/{semester}/{file_name}.zip'

def downloader(file_url, course_dir, file_name):
    file_path = f"{course_dir}{file_name}.zip"
    if not path.exists(file_path):
        resp = requests.get(file_url, stream = True)
        total = int(resp.headers.get('content-length', 0))
        status = resp.status_code
        if status == 200:
            print(f"------------------------\n[ Download Info ]\nFile Size: {total/(1024**2):.2f} MB \nFile Name: {file_name}.zip" )
            print(f"Download Link: {file_url}")
            with open(file_path, "wb") as file:
                downloaded = 0 
                for data in resp.iter_content(chunk_size=1024):
                    file.write(data)
                    downloaded += len(data)
                    print(f"> Downloading {downloaded / total * 100:.2f} %", end='\r')
                else:
                    print("> Downloaded Successfully.")
        elif status == 404:
            print("[404] File Not Found.")
        else:
            print("[Erorr] An Error Occurred.")
    else:
        print("File Exists.")


# load login page
print("Loading ... ")
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.accept_insecure_certs = True
chrome_install = ChromeDriverManager().install()
folder = path.dirname(chrome_install)
chromedriver_path = path.join(folder, "chromedriver.exe")
service = ChromeService(chromedriver_path)
driver = webdriver.Chrome(service=service, options=options)
driver.get('https://sess.shirazu.ac.ir/')

sleep(2)

# Load username & password from user-pass.txt
with open('user-pass.txt', 'r') as file:
    content = file.readlines()
    username = content[0].split(':')[1].strip()
    password = content[1].split(':')[1].strip()

# Enter user & pass
user_field = driver.find_element("xpath", '//*[@id="edId"]')
pass_field = driver.find_element("xpath", '//*[@id="edPass"]')
user_field.send_keys(username)
pass_field.send_keys(password)

sleep(1)

# Click On login Button
login_button = driver.find_element('xpath', '//*[@id="edEnter"]')
login_button.click()

sleep(3)

# Go To Curses List
student_units = driver.find_element('xpath', '//*[@actlist="OtherActs"]')
student_units.click()
courses_list_url = driver.current_url

sleep(1)

# Get Course Codes
course_code_elements = driver.find_elements('xpath', '//*[@id="edMiddle"]//td[@title]')
course_codes = [i.get_attribute("title") for i in course_code_elements]

# App

semester = getSelectedSemester()

for i in course_codes:
    course_name = getCourseName(i)
    driver.find_element('xpath', f'//td[@title="{i}"]').click()
    sleep(.5)
    clickOnVirtualClassList()
    sleep(.5) 
    class_links = getClassLinks()
    course_dir = makeCourseDir(semester, course_name)
    print(f'Course: {course_name} [{len(class_links)} Files]')
    for j in class_links:
        file_name = getFileNameId(j)
        file_url = makeDownloadUrl(file_name, semester)
        downloader(file_url, course_dir, file_name)
    print()
    goToCoursesList(courses_list_url)
    sleep(1)

print('All Done!\n-------------------------------\n>>> By Taregh Naderi - 1402 <<<\n-------------------------------\n')
input('Press Enter To Exit.')