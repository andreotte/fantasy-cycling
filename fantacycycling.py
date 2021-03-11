import requests
import pprint
import re
import csv
import os
from bs4 import BeautifulSoup

def getRidersScores():
    # ridersScores = []
    ridersScores = {}
    offset = 0
    results = True
    while(results):
        URL = f'https://www.procyclingstats.com/rankings.php?date=2021-03-11&nation=&age=&zage=&page=smallerorequal&team=&offset={offset}&filter=Filter&p=me&s=season-individual'
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')

        riderString = soup.find_all('a', {'href': re.compile(r'rider/')})
        pointsString = soup.find_all('a', {'href': re.compile(r'pcs-season-ranking')})

        if len(riderString) > 0:
            offset += 100
            for i in range(len(riderString)):
                riderName = riderString[i]['href'][6:].replace('-', ' ')
                riderScore = pointsString[i].string
                # ridersScores.append([riderName, riderScore])
                ridersScores[riderName] = riderScore
        else:
            results = False
        
    return ridersScores 
 
def buildLeagueScores(leagueRiders, riderScores):
    leagueScores = []
    for lr in leagueRiders:
        try:
            leagueScores.append([lr, riderScores[lr.lower()]])
        except KeyError:
            leagueScores.append([lr,0])

    return leagueScores

def writeRiderScores(rows):
    scriptDir = os.path.dirname(__file__) #<-- absolute dir the script is in
    absPath = os.path.join(scriptDir,"scores.csv")
    with open(absPath, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)  

        for row in rows:
            writer.writerow(row)

def getRidersFromLeague(): #todo read this from a file?
    riders = ["giacomo nizzolo"
    ,"mathieu van der poel"
    ,"mads pedersen"
    ,"wout van aert"
    ,"sam bennett"
    ,"arnaud demare"
    ,"marc hirschi"
    ,"dan martin"
    ,"richard carapaz"
    ,"julian alaphilippe"
    ,"primoz roglic"
    ,"mikel landa"
    ,"filippo ganna"
    ,"tadej pogacar"
    ,"alexander kristoff"
    ,"bryan coquard"
    ,"peter sagan"
    ,"stefan kung"
    ,"jakob fuglsang"
    ,"wilco kelderman"
    ,"tao geoghegan hart"
    ,"egan bernal"
    ,"giulio ciccone"
    ,"guillaume martin"
    ,"alejandro valverde"
    ,"remco evenepoel"
    ,"daryl impey"
    ,"tim wellens"
    ,"enric mas"
    ,"aleksey lutsenko"
    ,"hugh carthy"
    ,"michael woods"
    ,"thomas pidcock"
    ,"chris froome"
    ,"peerapol chawchiangkwang"
    ,"remi cavagna"
    ,"davide ballerini"
    ,"geraint thomas"
    ,"oliver naesen"
    ,"elia viviani"
    ,"jai hindley"
    ,"kasper asgreen"
    ,"neilson powless"
    ,"thomas de gendt"
    ,"sepp kuss"
    ,"niccolo bonifazio"
    ,"josef cerny"
    ,"richie porte"
    ,"biniam ghirmay"
    ,"michael matthews"
    ,"sonny colbrelli"
    ,"simon yates"
    ,"rohan dennis"
    ,"caleb ewan"
    ,"davide formolo"
    ,"diego ulissi"
    ,"nairo quintana"
    ,"jasper stuyven"
    ,"tiesj benoot"
    ,"ben o connor"
    ,"sergio higuita"
    ,"benoit cosnefroy"
    ,"romain bardet"
    ,"maximilian schachmann"
    ,"jack haig"
    ,"greg van avermaet"
    ,"matteo trentin"
    ,"tejay van garderen"
    ,"quinn simmons"
    ,"aleksandr vlasov"
    ,"david gaudu"
    ,"warren barguil"
    ,"philippe gilbert"
    ,"george bennett"
    ,"magnus cort"
    ,"miguel angel lopez"
    ,"michal kwiatkowski"
    ,"thibaut pinot"
    ,"alberto bettiol"
    ,"pascal ackermann"
    ,"fernando gaviria"
    ,"adam yates"
    ,"tim merlier"
    ,"vincenzo nibali"
    ,"rafal majka"
    ,"matej mohoric"
    ,"hugo hofstetter"
    ,"florian senechal"
    ,"joao almeida"
    ,"soren kragh andersen"
    ,"steven kruijswijk"
    ,"lennard kamna"
    ,"yves lampaert"
    ,"patrick konrad"
    ,"pavel sivakov"
    ,"luka mezgec"]

    return riders

def main(): 
    leagueScores = buildLeagueScores(getRidersFromLeague(),getRidersScores())
    writeRiderScores(leagueScores)
    
if __name__ == '__main__':
    main()

