#!/usr/bin/env python3

#imports
import json
import matplotlib as mpl
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk
from fastuaparser import parse_ua
import time
import os
import pygraphviz as pgv
import networkx as nx

#useful arguemtns 
#issuu_cw2.json for file
#140224101516-e5c074c3404177518bab9d7a65fb578e for task 2
#140227145459-ea9a6d79dfd0d64c12f65d38cf2038ab for task 5


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

#list of valid task ids
validTasks = ["2a","2b","3","4","5","6"]

#global vars
user_uuid = ""
doc_uuid = ""
task_id = ""
file_name = ""
data = []


class DataLoader:
    failed = False
    path = ""
    fileSize = 0
    
    #set the path, see if the file exists, work out how big it is
    def __init__(self,file_name):
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
        data = []
        start = (self.fileSize*x)//10
        end = (self.fileSize*(x+1))//10
        print("Dealing with lines %d to %d" % (start,end))
        with open(self.path, "r") as JSONfile:
            for pos,line in enumerate(JSONfile):
                if pos >= start and pos < end:
                     data.append(json.loads(line))
            



class Plotter:
    def displayHorz(self,dictionary):
        n = len(dictionary)
        plt.barh(range(n), list(dictionary.values()))
        plt.yticks(range(n), list(dictionary.keys()))
        plt.ylabel("Things")
        plt.xlabel("Count")
        plt.title("Title")
        plt.show()
    
    def displayVert(self,dictionary):
        n = len(dictionary)
        plt.bar(range(n), list(dictionary.values()))
        plt.xticks(range(n), list(dictionary.keys()))
        plt.xlabel("Things")
        plt.ylabel("Count")
        plt.title("Title")
        plt.show()



class Task2:
    countriesCount = {}
    continentsCount = {}

    def countCountries(self):
        for x in data:
            try:
                if x["env_doc_id"] == doc_uuid:
                    if x["visitor_country"] in self.countriesCount:
                        self.countriesCount[x["visitor_country"]] += 1
                    else:
                        self.countriesCount[x["visitor_country"]] = 1
            except KeyError:
                pass

    
    def countContinents(self):
        for x in self.countriesCount:
            if continents[cntry_to_cont[x]] in self.continentsCount:
                self.continentsCount[continents[cntry_to_cont[x]]] += self.countriesCount[x]
            else:
                self.continentsCount[continents[cntry_to_cont[x]]] = self.countriesCount[x]



class Task3:
    browsersCount = {}

    def countBrowsers(self):
        for x in data:
            try:
                browser = parse_ua(x["visitor_useragent"]).partition("-")[0]
                #print(browser)
                if browser in self.browsersCount:
                    self.browsersCount[browser] += 1
                else:
                    self.browsersCount[browser] = 1
            except KeyError:
                pass



class Task4:
    topReaders = {}

    def getTopReaders(self):
        for x in data:
            try:
                if x["visitor_uuid"][-4:] in self.topReaders:
                    self.topReaders[x["visitor_uuid"][-4:]] += x["event_readtime"]/60000
                else:
                    self.topReaders[x["visitor_uuid"][-4:]] = x["event_readtime"]/60000
            except KeyError:
                pass
        self.topReaders = dict(sorted(self.topReaders.items(), key=lambda x:x[1], reverse=True)[:10])
        


class Task5:
    uniqueVisitors = []
    uniqueDocuments = []
    likes = []
    docNumbers = {}
    userPrime = "" #if they provide a user they care about

    def getVisitors(self,document):
        for x in data:
            try:
                if x["env_doc_id"] == document:
                    if x["visitor_uuid"][-4:] not in self.uniqueVisitors:
                        self.uniqueVisitors.append(x["visitor_uuid"][-4:])
            except KeyError:
                pass

    
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
        G = nx.DiGraph()
        G.add_node(doc_uuid[-4:],style = "filled",color = "green")

        if self.userPrime[-4:] in self.uniqueVisitors: 
            G.add_node(self.userPrime[-4:],style = "filled",color = "green")

        for x in self.likes:
            G.add_edge(x[0],x[1])

        A = nx.nx_agraph.to_agraph(G)
        A.add_subgraph(self.uniqueVisitors,rank='same')
        A.add_subgraph(self.uniqueDocuments,rank='same')
        A.draw('example.ps', prog='dot')
        os.system("evince example.ps")
        


    




def doTask(task_id):
    dataLoader = DataLoader(file_name)
    plotter = Plotter()
    
    #make sure data loaded properly before doing any tasks
    if not dataLoader.failed:
       
        if task_id[0] == "2":
            #need a doc id for task 2
            if doc_uuid == "":
                print("Please specify a document like this: cw2 -d doc_uuid")
            else: 
                #do this for a and b
                task2 = Task2()
                for i in range(10):
                    dataLoader.loadPartOfData(i)
                    task2.countCountries()
                
                if task_id[1] == "b":
                    #finish off b
                    task2.countContinents()
                    print(task2.continentsCount)
                    plotter.displayVert(task2.continentsCount)
                else:
                    #finish off a
                    print(task2.countriesCount)
                    plotter.displayVert(task2.countriesCount)

        if task_id == "3":
            task3 = Task3()
            for i in range(10):
                dataLoader.loadPartOfData(i)
                task3.countBrowsers()
            print(task3.browsersCount)
            plotter.displayHorz(task3.browsersCount)

        if task_id == "4":
            task4 = Task4()
            for i in range(10):
                dataLoader.loadPartOfData(i)
                task4.getTopReaders()
            print(task4.topReaders)
            plotter.displayHorz(task4.topReaders)
        
        if task_id == "5" or task_id == "6":
            if doc_uuid == "":
                print("Please specify a document like this: cw2 -d doc_uuid")
            else:
                task5 = Task5()
                if user_uuid != "":
                    task5.userPrime = user_uuid
                #pretty gross, gotta load in the data twice
                
                for i in range(10):
                    dataLoader.loadPartOfData(i)
                    task5.getVisitors(doc_uuid)
                print("Got all visitors, now to find the documents")
                for i in range(10):
                    dataLoader.loadPartOfData(i)
                    task5.alsoLikes()
                

                print("User: %s" % task5.userPrime)
                if task_id == "5":
                    print(task5.docNumbers)
                    plotter.displayHorz(task5.docNumbers)
                else:
                    print(task5.likes)
                    task5.makeGraph()
                
                
                




def main():
    startTime = time.time()

    global user_uuid
    global doc_uuid
    global task_id
    global file_name

    #get command line args
    if "-u" in sys.argv:
        user_uuid = sys.argv[sys.argv.index("-u")+1]
    if "-d" in sys.argv:
        doc_uuid = sys.argv[sys.argv.index("-d")+1]
    if "-t" in sys.argv:
        task_id = sys.argv[sys.argv.index("-t")+1]
    if "-f" in sys.argv:
        file_name = sys.argv[sys.argv.index("-f")+1]

    #cant do anything without a file
    if file_name == "":
        print("Please specify a file like this: cw2 -f file_name")
    else:
        #need a valid task id too
        if task_id == "":
            print("Please specify a task like this: cw2 -t task_id")
        elif task_id not in validTasks:
            print("Invalid task, valid tasks are:")
            print(validTasks)
        else:
            doTask(task_id)
    
    endTime = time.time() - startTime
    print("Time taken: %fs" % endTime)


if __name__ == "__main__":
    main()



