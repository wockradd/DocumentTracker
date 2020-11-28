#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk

#import python files
import tasks

#list of valid task ids
validTasks = ["2a","2b","3","4","5","6"]


#main function that does the tasks
def run():
    dataLoader = tasks.DataLoader(fileId.get())
    plotter = tasks.Plotter()
    
    #make sure data loaded properly before doing any tasks
    if not dataLoader.failed:
       
        if taskId.get()[0] == "2":
            #need a doc id for task 2
            if docId.get() == "":
                output.set("Please specify a document")
            else: 
                #do this for a and b
                task2 = tasks.Task2(docId.get())
                for i in range(10):
                    dataLoader.loadPartOfData(i)
                    task2.countCountries()
                
                if taskId.get()[1] == "b":
                    #finish off b
                    task2.countContinents()
                    print(task2.continentsCount)
                    plotter.display(task2.continentsCount,"Continents","Continents where the document was viewed", True)
                else:
                    #finish off a
                    print(task2.countriesCount)
                    plotter.display(task2.countriesCount,"Countries","Countries where the document was viewed", True)

        if taskId.get() == "3":
            task3 = tasks.Task3()
            #work it out
            for i in range(10):
                dataLoader.loadPartOfData(i)
                task3.countBrowsers()
            
            #display it
            print(task3.browsersCount)
            plotter.display(task3.browsersCount, "Browsers", "Browsers by popularity")

        if taskId.get() == "4":
            task4 = tasks.Task4()
            #work it out
            for i in range(10):
                dataLoader.loadPartOfData(i)
                task4.getTopReaders()
            
            #display it
            print(task4.topReaders)
            plotter.display(task4.topReaders, "Users", "Top 10 readers")
        
        if taskId.get() == "5" or taskId.get() == "6":
            if docId.get() == "":
                output.set("Please specify a document")
            else:
                task5and6 = tasks.Task5and6(docId.get(), userId.get())

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
                if taskId.get() == "5":
                    print(task5and6.docNumbers)
                    plotter.display(task5and6.docNumbers,"Documents","Documents also liked ranked")
                #finish off task 6
                else:
                    print(task5and6.likes)
                    task5and6.makeGraph()


#callback function for the run button, checks inputs are valid before calling run()
def checkInputs(*args):
    #cant do anything without a file
    if fileId.get() == "":
        output.set("Please specify a file")
    else:
        #need a valid task id too
        if taskId.get() == "":
            output.set("Please specify a task")
        elif taskId.get() not in validTasks:
            output.set("Invalid task, valid tasks are:" + str(validTasks))
        else:
            output.set("Done, see the console for more info")
            run()
            

#init gui   
root = Tk()
root.title("CW2")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

#vars holding the strings we care about
fileId = StringVar()
taskId = StringVar()
userId = StringVar()
docId = StringVar()
output = StringVar()


#set up textboxes for user, file, doc and task
file_entry = ttk.Entry(mainframe, width=70, textvariable=fileId)
file_entry.grid(column=2, row=1, sticky=(W, E))
ttk.Label(mainframe, text="file:").grid(column=1, row=1, sticky=W)

task_entry = ttk.Entry(mainframe, textvariable=taskId)
task_entry.grid(column=2, row=2, sticky=(W, E))
ttk.Label(mainframe, text="task:").grid(column=1, row=2, sticky=W)

user_entry = ttk.Entry(mainframe, textvariable=userId)
user_entry.grid(column=2, row=3, sticky=(W, E))
ttk.Label(mainframe, text="user:").grid(column=1, row=3, sticky=W)

doc_entry = ttk.Entry(mainframe, textvariable=docId)
doc_entry.grid(column=2, row=4, sticky=(W, E))
ttk.Label(mainframe, text="doc:").grid(column=1, row=4, sticky=W)

#add run button and some info for the user
ttk.Button(mainframe, text="Run", command=checkInputs).grid(column=1, row=5)
ttk.Label(mainframe, textvariable = output).grid(column=2, row=6, sticky=S)

#add padding
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

#not sure
root.bind('<Return>', checkInputs)

#run
root.mainloop()