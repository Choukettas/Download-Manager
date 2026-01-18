import os
import colorama
import shutil
from colorama import Fore, Back, Style


print(Fore.MAGENTA +'Download Manager')
print(Style.RESET_ALL)

file_download = "Your Download Folder" #fill in here
folders = ("Image","Video","Model-3D","Fichier-Compressé","Executable","Autre")

conpreser = (".zip",".rar",".7z")
video = (".mp4",".avi", ".mkv",".mov",".wmv")
image = (".jpg",".png",".jpeg",".gif",".svg","webp")
model_3D =(".stl",".3mf",".obj",".amf",".step")
executable = (".exe",".msi")

with os.scandir(file_download) as it:
    for folder in folders:
        path = os.path.join(file_download,folder)

        if os.path.exists(path):
            print (Fore.GREEN + f"{folder}"" OK")

        else:
            print (Fore.RED + f"{folder}"" Not fonds")
            os.mkdir(path)
            print (Fore.YELLOW+ f"{folder}""Make")


print(Style.RESET_ALL)
with os.scandir(file_download) as it:
        
    for entry in it:
        if entry.is_file():
            nom, extension = os.path.splitext(entry.name)
            if extension in conpreser:
                print (Fore.YELLOW+nom,extension,"→ Fichier-Compressé")
                folder_locate = os.path.join(file_download, "Fichier-Compressé")
                destination = os.path.join(folder_locate, entry.name)
                shutil.move(entry.path, destination)
                print(Fore.GREEN+entry.name, "→ déplacé dans Fichier-Compressé")
            
            elif extension in video: 
                print (Fore.YELLOW+nom,extension,"→ Video")
                folder_locate = os.path.join(file_download, "Video")
                destination = os.path.join(folder_locate, entry.name)
                shutil.move(entry.path, destination)
                print(Fore.GREEN+entry.name, "→ déplacé dans Video")

            elif extension in image: 
                print (Fore.YELLOW+nom,extension,"→ Image")
                folder_locate = os.path.join(file_download, "Image")
                destination = os.path.join(folder_locate, entry.name)
                shutil.move(entry.path, destination)
                print(Fore.GREEN+entry.name, "→ déplacé dans Image")
            
            elif extension in model_3D: 
                print (Fore.YELLOW+nom,extension,"→ Model-3D")
                folder_locate = os.path.join(file_download, "Model-3D")
                destination = os.path.join(folder_locate, entry.name)
                shutil.move(entry.path, destination)
                print(Fore.GREEN+entry.name, "→ déplacé dans Model-3D")
          
            elif extension in executable:
                print (Fore.YELLOW+nom,extension,"→ Executable")
                folder_locate = os.path.join(file_download, "Executable")
                destination = os.path.join(folder_locate, entry.name)
                shutil.move(entry.path, destination)
                print(Fore.GREEN+entry.name, "→ déplacé dans Executable")
         
            else:
                print (Fore.YELLOW+nom,extension,"→ Autre")
                folder_locate = os.path.join(file_download, "Autre")
                destination = os.path.join(folder_locate, entry.name)
                shutil.move(entry.path, destination)
                print(Fore.GREEN+entry.name, "→ déplacé dans Autre")


print(Style.RESET_ALL)

