import pytube
from tkinter import filedialog, messagebox as MessageBox

from YoutubeDownloader.guiviews.gui_views import GUI

def seleccionar_carpeta():
    carpeta_destino = filedialog.askdirectory()
    return carpeta_destino

def seleccionar_calidad(audio, video):
     calidad_video=video  
     calidad_audio=audio     
     return calidad_video, calidad_audio
    
def accion():
    enlace = GUI.videos.get() # type: ignore
    video = pytube.YouTube(enlace)
    formato = GUI.videos2.get().lower() # type: ignore
    if formato == "mp4":
        video.streams.filter(file_extension="mp4").first().download(outpath_path=carpeta_destino)# type: ignore
        MessageBox.showinfo("Success", "¡Descarga completa en MP4! :D")
    elif formato == "mp3":
        audio = video.streams.filter(only_audio=True).first
        audio.download(outpath_path=carpeta_destino)# type: ignore
        MessageBox.showinfo("Success", "¡Descarga completa en MP3! :D")
    else:
        MessageBox.showinfo("Error", "Formato inválido :/, intenta nuevamente")
