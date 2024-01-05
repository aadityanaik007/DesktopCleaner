from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
# pip install watchdog for these packages to work

import os
import json
import time
import shutil
from datetime import datetime
from time import gmtime, strftime
class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            i = 1
            if filename != 'newDesktop':
                # try:
                    new_name = filename
                    extension = 'noname'
                    try:
                        extension = str(os.path.splitext(folder_to_track + '/' + filename)[1])
                        if extension == '' or extension is None:
                            continue
                        # path = extensions_folders[extension]
                    except Exception:
                        extension = 'noname'

                    now = datetime.now()
                    year = now.strftime("%Y")
                    month = now.strftime("%m")
                    folder_destination_path = folder_destination+extensions_folders[extension]
                    year_exists = False
                    month_exists = False
                    if not os.path.exists(folder_destination_path):
                        os.makedirs(folder_destination_path)
                    for folder_name in os.listdir(folder_destination_path):
                        if folder_name == year:
                            folder_destination_path = folder_destination_path + "/" + year
                            year_exists = True
                            for folder_month in os.listdir(folder_destination_path):
                                if month == folder_month:
                                    folder_destination_path = folder_destination_path+"/" + month
                                    month_exists = True
                    if not os.path.exists(folder_destination_path):
                         os.makedirs(folder_destination_path)
                    # if not year_exists:
                    #     os.mkdir(extensions_folders[extension] + "/" + year)
                    #     folder_destination_path = extensions_folders[extension] + "/" + year
                    # if not month_exists:
                    #     os.mkdir(folder_destination_path + "/" + month)
                    #     folder_destination_path = folder_destination_path + "/" + month


                    file_exists = os.path.isfile(folder_destination_path + "/" + new_name)
                    while file_exists:
                        i += 1
                        new_name = os.path.splitext(folder_to_track + '/' + filename)[0] + str(i) + os.path.splitext(folder_to_track + '/' + filename)[1]
                        new_name = new_name.split("/")[-1]
                        file_exists = os.path.isfile(folder_destination_path + "/" + new_name)
                    src = folder_to_track + "/" + filename

                    new_name = folder_destination_path + "/" + new_name
                    os.rename(src, new_name)
                # except Exception:
                #     print(filename)


if __name__ == "__main__":
    extensions_folders = {
    #No name
        'noname' : "Other/Uncategorized",
    #Audio
        '.aif' : "Media/Audio",
        '.cda' : "Media/Audio",
        '.mid' : "Media/Audio",
        '.midi' : "Media/Audio",
        '.mp3' : "Media/Audio",
        '.mpa' : "Media/Audio",
        '.ogg' : "Media/Audio",
        '.wav' : "Media/Audio",
        '.wma' : "Media/Audio",
        '.wpl' : "Media/Audio",
        '.m3u' : "Media/Audio",
    #Text
        '.txt' : "Text/TextFiles",
        '.doc' : "Text/Microsoft/Word",
        '.docx' : "Text/Microsoft/Word",
        '.odt ' : "Text/TextFiles",
        '.pdf': "Text/PDF",
        '.rtf': "Text/TextFiles",
        '.tex': "Text/TextFiles",
        '.wks ': "Text/TextFiles",
        '.wps': "Text/TextFiles",
        '.wpd': "Text/TextFiles",
    #Video
        '.3g2': "Media/Video",
        '.3gp': "Media/Video",
        '.avi': "Media/Video",
        '.flv': "Media/Video",
        '.h264': "Media/Video",
        '.m4v': "Media/Video",
        '.mkv': "Media/Video",
        '.mov': "Media/Video",
        '.mp4': "Media/Video",
        '.mpg': "Media/Video",
        '.mpeg': "Media/Video",
        '.rm': "Media/Video",
        '.swf': "Media/Video",
        '.vob': "Media/Video",
        '.wmv': "Media/Video",
    #Images
        '.ai': "Media/Images",
        '.bmp': "Media/Images",
        '.gif': "Media/Images",
        '.ico': "Media/Images",
        '.jpg': "Media/Images",
        '.jpeg': "Media/Images",
        '.png': "Media/Images",
        '.ps': "Media/Images",
        '.psd': "Media/Images",
        '.svg': "Media/Images",
        '.tif': "Media/Images",
        '.tiff': "Media/Images",
        '.CR2': "Media/Images",
    #Internet
        '.asp': "Other/Internet",
        '.aspx': "Other/Internet",
        '.cer': "Other/Internet",
        '.cfm': "Other/Internet",
        '.cgi': "Other/Internet",
        '.pl': "Other/Internet",
        '.css': "Other/Internet",
        '.htm': "Other/Internet",
        '.js': "Other/Internet",
        '.jsp': "Other/Internet",
        '.part': "Other/Internet",
        '.php': "Other/Internet",
        '.rss': "Other/Internet",
        '.xhtml': "Other/Internet",
    #Compressed
        '.7z': "Other/Compressed",
        '.arj': "Other/Compressed",
        '.deb': "Other/Compressed",
        '.pkg': "Other/Compressed",
        '.rar': "Other/Compressed",
        '.rpm': "Other/Compressed",
        '.tar.gz': "Other/Compressed",
        '.z': "Other/Compressed",
        '.zip': "Other/Compressed",
    #Disc
        '.bin': "Other/Disc",
        '.dmg': "Other/Disc",
        '.iso': "Other/Disc",
        '.toast': "Other/Disc",
        '.vcd': "Other/Disc",
    #Data
        '.csv': "Programming/Database",
        '.dat': "Programming/Database",
        '.db': "Programming/Database",
        '.dbf': "Programming/Database",
        '.log': "Programming/Database",
        '.mdb': "Programming/Database",
        '.sav': "Programming/Database",
        '.sql': "Programming/Database",
        '.tar': "Programming/Database",
        '.xml': "Programming/Database",
        '.json': "Programming/Database",
    #Executables
        '.apk': "Other/Executables",
        '.bat': "Other/Executables",
        '.com': "Other/Executables",
        '.exe': "Other/Executables",
        '.gadget': "Other/Executables",
        '.jar': "Other/Executables",
        '.wsf': "Other/Executables",
    #Fonts
        '.fnt': "Other/Fonts",
        '.fon': "Other/Fonts",
        '.otf': "Other/Fonts",
        '.ttf': "Other/Fonts",
    #Presentations
        '.key': "Text/Presentations",
        '.odp': "Text/Presentations",
        '.pps': "Text/Presentations",
        '.ppt': "Text/Presentations",
        '.pptx': "Text/Presentations",
    #Programming
        '.c': "Programming/C&C++",
        '.class': "Programming/Java",
        '.dart': "Programming/Dart",
        '.py': "Programming/Python",
        '.sh': "Programming/Shell",
        '.swift': "Programming/Swift",
        '.html': "Programming/html",
        '.h': "Programming/html",
    #Spreadsheets
        '.ods' : "Text/Microsoft/Excel",
        '.xlr' : "Text/Microsoft/Excel",
        '.xls' : "Text/Microsoft/Excel",
        '.xlsx' : "Text/Microsoft/Excel",
    #System
        '.bak' : "Text/Other/System",
        '.cab' : "Text/Other/System",
        '.cfg' : "Text/Other/System",
        '.cpl' : "Text/Other/System",
        '.cur' : "Text/Other/System",
        '.dll' : "Text/Other/System",
        '.dmp' : "Text/Other/System",
        '.drv' : "Text/Other/System",
        '.icns' : "Text/Other/System",
        '.ico' : "Text/Other/System",
        '.ini' : "Text/Other/System",
        '.lnk' : "Text/Other/System",
        '.msi' : "Text/Other/System",
        '.sys' : "Text/Other/System",
        '.tmp' : "Text/Other/System",
    }

    # Enter the name of the user profile
    profile_name = "csuftitan"

    # Please write the exact name of the folder you want to track
    tracking_folder_name = "oldDesktop"
    folder_to_track = f'/Users/{profile_name}/Desktop/{tracking_folder_name}'

    # Name of your destination folder
    destination_folder_name = 'newDesktop'
    folder_destination = f'/Users/{profile_name}/Desktop/{destination_folder_name}/'

    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, folder_to_track, recursive=True)
    observer.start()

    try:
        while True:
            # Adjust the timer as per your requirement
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()