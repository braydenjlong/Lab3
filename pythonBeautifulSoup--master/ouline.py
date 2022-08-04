import requests
from bs4 import BeautifulSoup
import json

def getJobList(role,location):
   # Complete the missing part of this function here
   url = f'https://www.talent.com/jobs?k={role}&l={location}'
   response = requests.get(url)

   # print the status code here!
   if response :
    print('Pass')
   else :
    print('Fail')

   soup = BeautifulSoup(response.text , 'html.parser')
   JobDetails = soup.find_all('div', class_='card card__job')
   # Create an array Here
   arr =[]
   for job in JobDetails:
       jobTitle = job.find('h2', class_='card__job-title').text.strip()
       company = job.find('div', class_='card__job-empname-label').text.strip()
       description = job.find('p', class_='card__job-snippet').text.replace('\n', '').replace("'", "").strip()
       jobDetailsjson = {
           "Title": jobTitle,
           "Company": company,
           "Description": description
       }
       arr[jobDetailsjson]
       
       return arr


#save data in JSON file
def saveDataInJSON(jobDetails):
    #Complete the missing part of this function here
    saveDataInJSON(jobDetails)
    print("Saving data to JSON")

#main function
def main():

    # Write a code here to get job location and role from user e.g. role = input()
    print("What location would you like to search?")
    location = input()

    print("Enter role you want to search")
    role = input()
    # Complete the missing part of this function here
    print(getJobList(role,location))
    
if __name__ == '__main__':
    main()
