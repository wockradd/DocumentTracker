#!/usr/bin/env python3

#imports libraries
import sys
import time

#import python files
import tasks


#useful arguemtns 
#issuu_cw2.json for file
#140224101516-e5c074c3404177518bab9d7a65fb578e for task 2
#140227145459-ea9a6d79dfd0d64c12f65d38cf2038ab for task 5



#list of valid task ids
validTasks = ["2a","2b","3","4","5","6"]

#global vars
user_uuid = ""
doc_uuid = ""
task_id = ""
file_name = ""





    
def doTask(task_id):
    dataLoader = tasks.DataLoader(file_name)
    plotter = tasks.Plotter()
    
    #make sure data loaded properly before doing any tasks
    if not dataLoader.failed:
       
        if task_id[0] == "2":
            #need a doc id for task 2
            if doc_uuid == "":
                print("Please specify a document like this: cw2 -d doc_uuid")
            else: 
                #do this for a and b
                task2 = tasks.Task2(doc_uuid)
                for i in range(10):
                    dataLoader.loadPartOfData(i)
                    task2.countCountries()
                
                if task_id[1] == "b":
                    #finish off b
                    task2.countContinents()
                    print(task2.continentsCount)
                    plotter.display(task2.continentsCount,"Continents","Continents where the document was viewed", True)
                else:
                    #finish off a
                    print(task2.countriesCount)
                    plotter.display(task2.countriesCount,"Countries","Countries where the document was viewed", True)

        if task_id == "3":
            task3 = tasks.Task3()
            #work it out
            for i in range(10):
                dataLoader.loadPartOfData(i)
                task3.countBrowsers()

            #display it
            print(task3.browsersCount)
            plotter.display(task3.browsersCount, "Browsers", "Browsers by popularity")

        if task_id == "4":
            task4 = tasks.Task4()
            #work it out
            for i in range(10):
                dataLoader.loadPartOfData(i)
                task4.getTopReaders()

            #display it
            print(task4.topReaders)
            plotter.display(task4.topReaders, "Users", "Top 10 readers")
        
        if task_id == "5" or task_id == "6":
            if doc_uuid == "":
                print("Please specify a document like this: cw2 -d doc_uuid")
            else:
                task5and6 = tasks.Task5and6(doc_uuid, user_uuid)

                #pretty gross, gotta load in the data twice
                for i in range(10):
                    dataLoader.loadPartOfData(i)
                    task5and6.getVisitors()
                print("Got all visitors, now to find the documents")
                for i in range(10):
                    dataLoader.loadPartOfData(i)
                    task5and6.alsoLikes()
                
                #print the user if they've supplied one
                print("User: %s" % task5and6.userId)

                #finish off task 5
                if task_id == "5":
                    print(task5and6.docNumbers)
                    plotter.display(task5and6.docNumbers,"Documents","Documents also liked ranked")
                #finish off task 6 
                else:
                    print(task5and6.likes)
                    task5and6.makeGraph()
                
                
                



#entry point
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



