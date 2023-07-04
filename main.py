import tkinter
from tkinter import messagebox as MessageBox
from YoutubeDownloader.guiviews.gui_views import GUI
from YoutubeDownloader.utils.downloader import seleccionar_carpeta, seleccionar_calidad, accion
from customtkinter import CTk, CTkFrame
root = CTk()
gui = GUI(root)
root.mainloop()

