import requests
import pprint
import re
import csv
import os
from bs4 import BeautifulSoup

def getRidersScores():
    ridersScores = []
    offset = 0
    results = True
    while(results):
        URL = f'https://www.procyclingstats.com/rankings.php?date=2021-03-09&nation=&age=&zage=&page=smallerorequal&team=&offset={offset}&filter=Filter&p=me&s=season-individual'
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')

        riderString = soup.find_all('a', {'href': re.compile(r'rider/')})
        pointsString = soup.find_all('a', {'href': re.compile(r'pcs-season-ranking')})

        if len(riderString) > 0:
            offset += 100
            for i in range(len(riderString)):
                riderName = riderString[i]['href'][6:].replace('-', ' ')
                riderScore = pointsString[i].string
                ridersScores.append([riderName, riderScore])
        else:
            results = False
        
    return ridersScores 

def writeRiderScores(rows):
    scriptDir = os.path.dirname(__file__) #<-- absolute dir the script is in
    absPath = os.path.join(scriptDir,"scores.csv")
    with open(absPath, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)  

        for row in rows:
            print(row)
            writer.writerow(row)

def main():
    writeRiderScores(getRidersScores())
    
if __name__ == '__main__':
    main()






# pp.pprint(soup)
