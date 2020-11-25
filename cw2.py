#!/usr/bin/env python3

#imports
import json
import matplotlib as mpl
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk

#useful arguemtns 
#issuu_cw2.json for file
#140224101516-e5c074c3404177518bab9d7a65fb578e for document


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
validTasks = ["2a","2b","3a","3b","4d","5","6"]

#global vars
user_uuid = ""
doc_uuid = ""
task_id = ""
file_name = ""
data = []


class DataLoader:
    global data
    failed = False
    def __init__(self,file_name):
        path = "./data/" + file_name
        try:
            with open(path, "r") as JSONfile:
                for line in JSONfile:
                    data.append(json.loads(line))
        except FileNotFoundError:
            self.failed = True
            print("Couldnt find the file")


class Plotter:
    def display(self,dictionary):
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
            if "subject_doc_id" in x.keys():
                if x["subject_doc_id"] == doc_uuid:
                    if x["visitor_country"] in self.countriesCount:
                        self.countriesCount[x["visitor_country"]] += 1
                    else:
                        self.countriesCount[x["visitor_country"]] = 1
    
    def countContinents(self):
        for x in self.countriesCount:
            if continents[cntry_to_cont[x]] in self.continentsCount:
                self.continentsCount[continents[cntry_to_cont[x]]] += self.countriesCount[x]
            else:
                self.continentsCount[continents[cntry_to_cont[x]]] = self.countriesCount[x]





def doTask(task_id):
    dataLoader = DataLoader(file_name)
    plotter = Plotter()

    if not dataLoader.failed:
        if task_id[0] == "2":
            if doc_uuid == "":
                print("Please specify a document like this: cw2 -d doc_uuid")
            else: 
                task2 = Task2()
                task2.countCountries()
                
                if task_id[1] == "b":
                    task2.countContinents()
                    print(task2.continentsCount)
                    plotter.display(task2.continentsCount)
                else:
                    plotter.display(task2.countriesCount)


def main():
    global user_uuid
    global doc_uuid
    global task_id
    global file_name

    if "-u" in sys.argv:
        user_uuid = sys.argv[sys.argv.index("-u")+1]
    if "-d" in sys.argv:
        doc_uuid = sys.argv[sys.argv.index("-d")+1]
    if "-t" in sys.argv:
        task_id = sys.argv[sys.argv.index("-t")+1]
    if "-f" in sys.argv:
        file_name = sys.argv[sys.argv.index("-f")+1]

    if file_name == "":
        print("Please specify a file like this: cw2 -f file_name")
    else:
        if task_id == "":
            print("Please specify a task like this: cw2 -t task_id")
        elif task_id not in validTasks:
            print("Invalid task, valid tasks are:")
            print(validTasks)
        else:
            doTask(task_id)


if __name__ == "__main__":
    main()



