import os,sys

class menuCmds():
    def __init__(self,App) -> None:
        self.root = App

    def menuSettings(self):
        pass

    def menuOpenFile(self):
        """
        ouvrir un fichier
        """

    def menuOpenDirectory(self):
        """
        ouvrir un fichier
        """

    def menuNewFile(self):
        pass

    def menuSave(self):
        pass

    def menuSaveAs(self):
        pass

    def menuExit(self):
        self.root.destroy()
