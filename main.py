import tkinter as tk
import sys,os
import menuCommands
from jsonRead import settings_data

# Besoin d'une stack pour les control-Z

class App(tk.Tk):
    def __init__(self,settings):
        tk.Tk.__init__(self)
        self.settings = settings
        self.commands = menuCommands.menuCmds(self)
        #liste de dictionnaire de tous les éléments de la fenêtre avec leurs informations. 
        self.element = []   

        
         
    def menuBar(self):
        self.menubar = tk.Menu(self)
        self.config(menu=self.menubar)

        def menuInterpreter(self,menuDict:dict)->None:
            base = menuDict["settings"]["menu"]
            for k in base:
                #print(k)
                #print(base[k])
                exec('self.menu'+k+'=tk.Menu(self.menubar,tearoff=0)')
                exec("self.menubar.add_cascade(label='"+base[k]['label'].encode("iso-8859-1").decode("utf-8")+"',menu=self.menu"+k+")")
                for i in base[k]['order']:
                    if i == "sep":
                        exec("self.menu"+k+".add_separator()")
                    elif "settings" in  base[k]['settings'][i]:
                        # sous menus dans les sous menus pour faire un selecteur de fichier récents
                        print(k)
                    else:
                        exec("self.menu"+k+".add_command(label='"+base[k]['settings'][i]['label'].encode("iso-8859-1").decode("utf-8")+"',command=self.commands."+base[k]['settings'][i]['value']+")")

        """

        accelerator="CTRL+N"

        self.menufichier = tk.Menu(self.menubar,tearoff=0)
        self.menubar.add_cascade(label='Fichier',menu=self.menufichier)

        self.menuedition = tk.Menu(self.menubar,tearoff=0)
        self.menubar.add_cascade(label='Edition',menu=self.menuedition)
        """

        menuInterpreter(self,self.settings)

    def schema(self):
        ...

    def menuOpen(self):
        ...

    def menuNewFile(self):
        ...

    def run(self):
        self.menuBar()
        self.mainloop()

if __name__=="__main__":
    a=App(settings_data)
    a.run()