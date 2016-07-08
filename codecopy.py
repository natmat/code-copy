import os
import platform

from tkinter import filedialog, messagebox, Frame

import tkinter
import linecache

filePrefix = "JHNM:"

def chooseDirectory():
    system = platform.system()
    print("Sys=" + system)
    if (system == "darwin"):
        baseDir = "~/GitHub/."
    else:
        baseDir = "C:/MyWorkspaces/git/." 
    dirname = filedialog.askdirectory(parent=tkinter.Tk(), 
                                      initialdir=baseDir, 
                                      title='Please select a directory')
    return(dirname)
    
def createFileList(inDir):
    print(">", inDir)
    
    javafiles = []  
    for root, dirs, files in os.walk(inDir):
        for name in files:
            if name.endswith(".java"):
                print("F ", os.path.join(root, name))
                javafiles.append(os.path.join(root, name))
                
        for name in dirs:
            print("D ", os.path.join(root, name))
    
    with open("./javafiles.txt", 'w') as outfile:
        for fname in javafiles:
            global filePrefix
            filetag = filePrefix + fname + "\n"
            filetag = filetag.replace('\\', '/')
            outfile.write(filetag)
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)
            infile.close()
    outfile.close()
    
def chooseFile():
    global filePrefix
    file = filedialog.askopenfile(mode="r") 
    with open(file.name, 'r') as codeFile:  
        # skip to first file prefix line
        line = codeFile.readline()
        while (False == line.startswith(filePrefix)) :
            line = codeFile.readline()

        while(True):
            if (len(line) == 0):
                return
            
            file = line[len(filePrefix):].rstrip() + "_"
            outfile = open(file, 'w')
            print ("Importing: " + file.rstrip())
            line = codeFile.readline()
            while ((len(line) > 0) & (False == line.startswith(filePrefix))):
                outfile.write(line.rstrip())
                line = codeFile.readline()
            outfile.close()
            
    
def importFiles():
    chooseFile()

def exportFiles():
    dirName = chooseDirectory()
    createFileList(dirName)
    
def importExport():
    root = tkinter.Tk()
    frame = Frame(root)
    b1 = tkinter.Button(frame, text='Import', command=importFiles)
    b1.pack()
    
    b2 = tkinter.Button(frame, text='Export', command=exportFiles)
    b2.pack()
    frame.pack()
    root.mainloop()
    
    frame.quit()
        
def main():   
    importExport()
#     dirName = chooseDirectory()
#     createFileList(dirName)
    print("Out")
    
    
if __name__ == "__main__":
    main()
    
