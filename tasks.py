#!/usr/bin/env python3

#import libraries
import json
import matplotlib as mpl
import matplotlib.pyplot as plt
import os
from fastuaparser import parse_ua
import pygraphviz as pgv
import networkx as nx

#helpful dict
continents = {
  'AF' : 'Africa',
  'AS' : 'Asia',
  'EU' : 'Europe',
  'NA' : 'North America',
  'SA' : 'South America',
  'OC' : 'Oceania',
  'AN' : 'Antarctica'
}

#maps countries to continents
cntry_to_cont = { 'AF' : 'AS', 'AX' : 'EU', 'AL' : 'EU', 'DZ' : 'AF', 'AS' : 'OC', 'AD' : 'EU', 'AO' : 'AF', 'AI' : 'NA', 'AQ' : 'AN', 'AG' : 'NA', 'AR' : 'SA', 'AM' : 'AS', 'AW' : 'NA', 'AU' : 'OC', 'AT' : 'EU', 'AZ' : 'AS', 'BS' : 'NA', 'BH' : 'AS', 'BD' : 'AS', 'BB' : 'NA', 'BY' : 'EU', 'BE' : 'EU', 'BZ' : 'NA', 'BJ' : 'AF', 'BM' : 'NA', 'BT' : 'AS', 'BO' : 'SA', 'BQ' : 'NA', 'BA' : 'EU', 'BW' : 'AF', 'BV' : 'AN', 'BR' : 'SA', 'IO' : 'AS', 'VG' : 'NA', 'BN' : 'AS', 'BG' : 'EU', 'BF' : 'AF', 'BI' : 'AF', 'KH' : 'AS', 'CM' : 'AF', 'CA' : 'NA', 'CV' : 'AF', 'KY' : 'NA', 'CF' : 'AF', 'TD' : 'AF', 'CL' : 'SA', 'CN' : 'AS', 'CX' : 'AS', 'CC' : 'AS', 'CO' : 'SA', 'KM' : 'AF', 'CD' : 'AF', 'CG' : 'AF', 'CK' : 'OC', 'CR' : 'NA', 'CI' : 'AF', 'HR' : 'EU', 'CU' : 'NA', 'CW' : 'NA', 'CY' : 'AS', 'CZ' : 'EU', 'DK' : 'EU', 'DJ' : 'AF', 'DM' : 'NA', 'DO' : 'NA', 'EC' : 'SA', 'EG' : 'AF', 'SV' : 'NA', 'GQ' : 'AF', 'ER' : 'AF', 'EE' : 'EU', 'ET' : 'AF', 'FO' : 'EU', 'FK' : 'SA', 'FJ' : 'OC', 'FI' : 'EU', 'FR' : 'EU', 'GF' : 'SA', 'PF' : 'OC', 'TF' : 'AN', 'GA' : 'AF', 'GM' : 'AF', 'GE' : 'AS', 'DE' : 'EU', 'GH' : 'AF', 'GI' : 'EU', 'GR' : 'EU', 'GL' : 'NA', 'GD' : 'NA', 'GP' : 'NA', 'GU' : 'OC', 'GT' : 'NA', 'GG' : 'EU', 'GN' : 'AF', 'GW' : 'AF', 'GY' : 'SA', 'HT' : 'NA', 'HM' : 'AN', 'VA' : 'EU', 'HN' : 'NA', 'HK' : 'AS', 'HU' : 'EU', 'IS' : 'EU', 'IN' : 'AS', 'ID' : 'AS', 'IR' : 'AS', 'IQ' : 'AS', 'IE' : 'EU', 'IM' : 'EU', 'IL' : 'AS', 'IT' : 'EU', 'JM' : 'NA', 'JP' : 'AS', 'JE' : 'EU', 'JO' : 'AS', 'KZ' : 'AS', 'KE' : 'AF', 'KI' : 'OC', 'KP' : 'AS', 'KR' : 'AS', 'KW' : 'AS', 'KG' : 'AS', 'LA' : 'AS', 'LV' : 'EU', 'LB' : 'AS', 'LS' : 'AF', 'LR' : 'AF', 'LY' : 'AF', 'LI' : 'EU', 'LT' : 'EU', 'LU' : 'EU', 'MO' : 'AS', 'MK' : 'EU', 'MG' : 'AF', 'MW' : 'AF', 'MY' : 'AS', 'MV' : 'AS', 'ML' : 'AF', 'MT' : 'EU', 'MH' : 'OC', 'MQ' : 'NA', 'MR' : 'AF', 'MU' : 'AF', 'YT' : 'AF', 'MX' : 'NA', 'FM' : 'OC', 'MD' : 'EU', 'MC' : 'EU', 'MN' : 'AS', 'ME' : 'EU', 'MS' : 'NA', 'MA' : 'AF', 'MZ' : 'AF', 'MM' : 'AS', 'NA' : 'AF', 'NR' : 'OC', 'NP' : 'AS', 'NL' : 'EU', 'NC' : 'OC', 'NZ' : 'OC', 'NI' : 'NA', 'NE' : 'AF', 'NG' : 'AF', 'NU' : 'OC', 'NF' : 'OC', 'MP' : 'OC', 'NO' : 'EU', 'OM' : 'AS', 'PK' : 'AS', 'PW' : 'OC', 'PS' : 'AS', 'PA' : 'NA', 'PG' : 'OC', 'PY' : 'SA', 'PE' : 'SA', 'PH' : 'AS', 'PN' : 'OC', 'PL' : 'EU', 'PT' : 'EU', 'PR' : 'NA', 'QA' : 'AS', 'RE' : 'AF', 'RO' : 'EU', 'RU' : 'EU', 'RW' : 'AF', 'BL' : 'NA', 'SH' : 'AF', 'KN' : 'NA', 'LC' : 'NA', 'MF' : 'NA', 'PM' : 'NA', 'VC' : 'NA', 'WS' : 'OC', 'SM' : 'EU', 'ST' : 'AF', 'SA' : 'AS', 'SN' : 'AF', 'RS' : 'EU', 'SC' : 'AF', 'SL' : 'AF', 'SG' : 'AS', 'SX' : 'NA', 'SK' : 'EU', 'SI' : 'EU', 'SB' : 'OC', 'SO' : 'AF', 'ZA' : 'AF', 'GS' : 'AN', 'SS' : 'AF', 'ES' : 'EU', 'LK' : 'AS', 'SD' : 'AF', 'SR' : 'SA', 'SJ' : 'EU', 'SZ' : 'AF', 'SE' : 'EU', 'CH' : 'EU', 'SY' : 'AS', 'TW' : 'AS', 'TJ' : 'AS', 'TZ' : 'AF', 'TH' : 'AS', 'TL' : 'AS', 'TG' : 'AF', 'TK' : 'OC', 'TO' : 'OC', 'TT' : 'NA', 'TN' : 'AF', 'TR' : 'AS', 'TM' : 'AS', 'TC' : 'NA', 'TV' : 'OC', 'UG' : 'AF', 'UA' : 'EU', 'AE' : 'AS', 'GB' : 'EU', 'US' : 'NA', 'UM' : 'OC', 'VI' : 'NA', 'UY' : 'SA', 'UZ' : 'AS', 'VU' : 'OC', 'VE' : 'SA', 'VN' : 'AS', 'WF' : 'OC', 'EH' : 'AF', 'YE' : 'AS', 'ZM' : 'AF', 'ZW' : 'AF' } 

#main list that will hold the json
data = []


class DataLoader:
    failed = False
    path = ""
    fileSize = 0
    
    #set the path, see if the file exists, work out how big it is
    def __init__(self,file_name):
        #initialise stuff
        self.failed = False
        self.fileSize = 0
        self.path = "./data/" + file_name
        
        try:
            with open(self.path, "r") as JSONfile:
                print("Working out file size")
                for line in JSONfile:
                    self.fileSize+=1
        except FileNotFoundError:
            self.failed = True
            print("Couldnt find the file at %s" % self.path)


    # x=0 means get the data from 0 - 10%
    # x=1 means get the data from 10 - 20%
    # x=2 means get the data from 20 - 30% etc
    def loadPartOfData(self,x):
        global data
        data = [] #empty the list

        #work out start and ending lines
        start = (self.fileSize*x)//10
        end = (self.fileSize*(x+1))//10

        print("Dealing with lines %d to %d" % (start,end))

        with open(self.path, "r") as JSONfile:
            for pos,line in enumerate(JSONfile):
                #load the data from line start to end into the list
                if pos >= start and pos < end:
                     data.append(json.loads(line))
            



class Plotter:
    #displays the data its given using matplotlib
    def display(self,dictionary, things, title, vert=False):
        n = len(dictionary)
        if vert:
            plt.bar(range(n), list(dictionary.values()))
            plt.xticks(range(n), list(dictionary.keys()))
            plt.xlabel(things)
            plt.ylabel("Count")
        else:
            plt.barh(range(n), list(dictionary.values()))
            plt.yticks(range(n), list(dictionary.keys()))
            plt.ylabel(things)
            plt.xlabel("Count")
        
        plt.title(title)
        plt.show()




class Task2:
    countriesCount = {}
    continentsCount = {}
    docId = ""

    #initialise stuff, resets the dictionaries for the GUI version
    def __init__(self,docId):
        self.docId = docId
        self.countriesCount = {}
        self.continentsCount = {}

    #populates the contriesCount dictionary
    def countCountries(self):
        for x in data:
            try:
                #we've found an instance of the doc we're interested in
                if x["env_doc_id"] == self.docId:
                    if x["visitor_country"] in self.countriesCount:#seen it before
                        self.countriesCount[x["visitor_country"]] += 1
                    else:
                        self.countriesCount[x["visitor_country"]] = 1
            except KeyError:
                pass

    
    #populates the continentsCount dictionary
    def countContinents(self):
        for x in self.countriesCount:
            if continents[cntry_to_cont[x]] in self.continentsCount:#seen it before
                self.continentsCount[continents[cntry_to_cont[x]]] += self.countriesCount[x]
            else:
                self.continentsCount[continents[cntry_to_cont[x]]] = self.countriesCount[x]



class Task3:
    browsersCount = {}

    #initialise stuff, resets the dictionary for the GUI version
    def __init__(self):
        self.browsersCount = {}

    #populates the browserCount dictionary
    def countBrowsers(self):
        for x in data:
            try:
                browser = parse_ua(x["visitor_useragent"]).partition("-")[0]
                if browser in self.browsersCount:#seen it before
                    self.browsersCount[browser] += 1
                else:
                    self.browsersCount[browser] = 1
            except KeyError:
                pass



class Task4:
    topReaders = {}

    #initialise stuff, resets the dictionary for the GUI version
    def __init__(self):
        self.topReaders = {}

    #populates the topReaders dictionary
    def getTopReaders(self):
        for x in data:
            try:
                if x["visitor_uuid"][-4:] in self.topReaders:#seen it before
                    self.topReaders[x["visitor_uuid"][-4:]] += x["event_readtime"]/60000
                else:
                    self.topReaders[x["visitor_uuid"][-4:]] = x["event_readtime"]/60000
            except KeyError:
                pass

        #only care about the top 10
        self.topReaders = dict(sorted(self.topReaders.items(), key=lambda x:x[1], reverse=True)[:10])
        


class Task5and6:
    uniqueVisitors = []
    uniqueDocuments = []
    likes = []
    docNumbers = {}
    docId = ""
    userId = "" #if they provide a user they care about

    #initialise stuff, resets the dictionaries and lists for the GUI version
    def __init__(self,docId,userId):
        self.docId = docId
        self.userId = userId
        self.uniqueVisitors = []
        self.uniqueDocuments = []
        self.likes = []
        self.docNumbers = {}

    #works out which users have seen the document
    def getVisitors(self):
        for x in data:
            try:
                if x["env_doc_id"] == self.docId:
                    if x["visitor_uuid"][-4:] not in self.uniqueVisitors:
                        self.uniqueVisitors.append(x["visitor_uuid"][-4:])
            except KeyError:
                pass

    #main function for task 5 and 6
    def alsoLikes(self):
        for vis in self.uniqueVisitors:
            for x in data:
                try:
                    if x["visitor_uuid"][-4:] == vis:
                        #save all the unique doc ids
                        if x["env_doc_id"][-4:] not in self.uniqueDocuments:
                            self.uniqueDocuments.append(x["env_doc_id"][-4:])

                        #populate the thing for task 5
                        if x["env_doc_id"][-4:] in self.docNumbers:
                            self.docNumbers[x["env_doc_id"][-4:]] += 1
                        else:
                            self.docNumbers[x["env_doc_id"][-4:]] = 1

                        #populate the thing for task 6
                        if (x["visitor_uuid"][-4:],x["env_doc_id"][-4:]) not in self.likes:
                            self.likes.append((x["visitor_uuid"][-4:],x["env_doc_id"][-4:]))
                except KeyError:
                    pass

            #sort the list
            self.docNumbers = dict(sorted(self.docNumbers.items(), key=lambda x:x[1], reverse=True))
            

    def makeGraph(self):
        #init graph
        G = nx.DiGraph()
        G.add_node(self.docId[-4:],style = "filled",color = "green")

        #color user if specified
        if self.userId[-4:] in self.uniqueVisitors: 
            G.add_node(self.userId[-4:],style = "filled",color = "green")

        #add edges
        for x in self.likes:
            G.add_edge(x[0],x[1])

        #sort out layout and display
        A = nx.nx_agraph.to_agraph(G)
        A.add_subgraph(self.uniqueVisitors,rank='same')
        A.add_subgraph(self.uniqueDocuments,rank='same')
        A.draw('example.ps', prog='dot')
        os.system("evince example.ps")
        
