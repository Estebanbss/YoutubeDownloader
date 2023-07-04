from customtkinter import CTk, CTkFrame,CTkEntry,CTkButton
class GUI:
    def __init__(self, root):

        self.root = root
        self.videos = CTkEntry(root,width=140)
        self.videos.grid(row=0,column=0)
        self.videos2 = CTkEntry(root,width=140)
        self.videos2.grid(row=1,column=0)
       
  
        # Resto de la configuración y asignación de funcione