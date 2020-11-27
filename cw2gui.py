#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk

#import python files
import tasks

#list of valid task ids
validTasks = ["2a","2b","3","4","5","6"]



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
                    plotter.displayVert(task2.continentsCount)
                else:
                    #finish off a
                    print(task2.countriesCount)
                    plotter.displayVert(task2.countriesCount)

        if taskId.get() == "3":
            task3 = tasks.Task3()
            for i in range(10):
                dataLoader.loadPartOfData(i)
                task3.countBrowsers()
            print(task3.browsersCount)
            plotter.displayHorz(task3.browsersCount)

        if taskId.get() == "4":
            task4 = tasks.Task4()
            for i in range(10):
                dataLoader.loadPartOfData(i)
                task4.getTopReaders()
            print(task4.topReaders)
            plotter.displayHorz(task4.topReaders)
        
        if taskId.get() == "5" or taskId.get() == "6":
            if docId.get() == "":
                output.set("Please specify a document")
            else:
                task5 = tasks.Task5(docId.get(), userId.get())
                #pretty gross, gotta load in the data twice
                
                for i in range(10):
                    dataLoader.loadPartOfData(i)
                    task5.getVisitors()
                print("Got all visitors, now to find the documents")
                for i in range(10):
                    dataLoader.loadPartOfData(i)
                    task5.alsoLikes()
                

                print("User: %s" % task5.userId)
                if taskId.get() == "5":
                    print(task5.docNumbers)
                    plotter.displayHorz(task5.docNumbers)
                else:
                    print(task5.likes)
                    task5.makeGraph()


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
            output.set("Running")
            run()
        
root = Tk()
root.title("CW2")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

fileId = StringVar()
taskId = StringVar()
userId = StringVar()
docId = StringVar()
output = StringVar()



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


ttk.Button(mainframe, text="Run", command=checkInputs).grid(column=1, row=5)
ttk.Label(mainframe, textvariable = output).grid(column=2, row=6, sticky=S)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.bind('<Return>', checkInputs)

root.mainloop()