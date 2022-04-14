from bs4 import BeautifulSoup
import requests

print("\n**********TIMES JOB WEB SCRAPER**********\n")
str=input("Enter your skills (enter multiple with spaces).\n")
un_sk=input("Enter unfamiliar skills (enter multiple with spaces).\n").upper().split()
loc=input("Enter the location (Leave empty for universal search).\n")


try:
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords='+str+'&txtLocation='+loc)
except: 
    print("Connect to internet first dumbass.")
    exit(0)

soup = BeautifulSoup(html_text.text, 'lxml')
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

c=1
for job in jobs:
    f=0
    skills = job.find('span', class_ = 'srp-skills').text.strip()
    sk=skills.upper()
    for uskill in un_sk:
        if(uskill in sk):
            f=1
    company_Name= job.find('h3', class_ = 'joblist-comp-name').text.strip()
    time = job.find('span', class_ = 'sim-posted').text.strip()
    location=job.find('span').text
    if(location==''): location='Not available'
    link=job.header.h2.a['href']
    if f==1: continue
    
    print(f'''
{c})
Company Name: {company_Name}
Required Skills: {skills}
Location: {location}
Date: {time}
Link: {link}
        ''')
    c=c+1
if(c==1):
    print("No job post matched your skills.")
