from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
# pip install watchdog for these packages to work

import os
import json
import time
import shutil
from datetime import datetime
from time import gmtime, strftime
import pdb
class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            i = 1
            if filename != 'newDesktop':
                # try:
                    new_name = filename
                    extension = 'noname'
                    # pdb.set_trace()
                    try:
                        extension = str(os.path.splitext(folder_to_track + '/' + filename)[1])
                        path = extensions_folders[extension]
                    except Exception:
                        extension = 'noname'

                    now = datetime.now()
                    year = now.strftime("%Y")
                    month = now.strftime("%m")

                    folder_destination_path = extensions_folders[extension]
                    year_exists = False
                    month_exists = False
                    if not os.path.exists(folder_destination_path):
                        os.makedirs(folder_destination_path)
                    for folder_name in os.listdir(extensions_folders[extension]):
                        if folder_name == year:
                            folder_destination_path = extensions_folders[extension] + "/" + year
                            year_exists = True
                            for folder_month in os.listdir(folder_destination_path):
                                if month == folder_month:
                                    folder_destination_path = extensions_folders[extension] + "/" + year + "/" + month
                                    month_exists = True
                    if not year_exists:
                        os.mkdir(extensions_folders[extension] + "/" + year)
                        folder_destination_path = extensions_folders[extension] + "/" + year
                    if not month_exists:
                        os.mkdir(folder_destination_path + "/" + month)
                        folder_destination_path = folder_destination_path + "/" + month


                    file_exists = os.path.isfile(folder_destination_path + "/" + new_name)
                    while file_exists:
                        i += 1
                        new_name = os.path.splitext(folder_to_track + '/' + filename)[0] + str(i) + os.path.splitext(folder_to_track + '/' + filename)[1]
                        new_name = new_name.split("/")[4]
                        file_exists = os.path.isfile(folder_destination_path + "/" + new_name)
                    src = folder_to_track + "/" + filename

                    new_name = folder_destination_path + "/" + new_name
                    os.rename(src, new_name)
                # except Exception:
                #     print(filename)

extensions_folders = {
#No name
    'noname' : "/Users/csuftitan/Desktop/newDesktop/Other/Uncategorized",
#Audio
    '.aif' : "/Users/csuftitan/Desktop/newDesktop/Media/Audio",
    '.cda' : "/Users/csuftitan/Desktop/newDesktop/Media/Audio",
    '.mid' : "/Users/csuftitan/Desktop/newDesktop/Media/Audio",
    '.midi' : "/Users/csuftitan/Desktop/newDesktop/Media/Audio",
    '.mp3' : "/Users/csuftitan/Desktop/newDesktop/Media/Audio",
    '.mpa' : "/Users/csuftitan/Desktop/newDesktop/Media/Audio",
    '.ogg' : "/Users/csuftitan/Desktop/newDesktop/Media/Audio",
    '.wav' : "/Users/csuftitan/Desktop/newDesktop/Media/Audio",
    '.wma' : "/Users/csuftitan/Desktop/newDesktop/Media/Audio",
    '.wpl' : "/Users/csuftitan/Desktop/newDesktop/Media/Audio",
    '.m3u' : "/Users/csuftitan/Desktop/newDesktop/Media/Audio",
#Text
    '.txt' : "/Users/csuftitan/Desktop/newDesktop/Text/TextFiles",
    '.doc' : "/Users/csuftitan/Desktop/newDesktop/Text/Microsoft/Word",
    '.docx' : "/Users/csuftitan/Desktop/newDesktop/Text/Microsoft/Word",
    '.odt ' : "/Users/csuftitan/Desktop/newDesktop/Text/TextFiles",
    '.pdf': "/Users/csuftitan/Desktop/newDesktop/Text/PDF",
    '.rtf': "/Users/csuftitan/Desktop/newDesktop/Text/TextFiles",
    '.tex': "/Users/csuftitan/Desktop/newDesktop/Text/TextFiles",
    '.wks ': "/Users/csuftitan/Desktop/newDesktop/Text/TextFiles",
    '.wps': "/Users/csuftitan/Desktop/newDesktop/Text/TextFiles",
    '.wpd': "/Users/csuftitan/Desktop/newDesktop/Text/TextFiles",
#Video
    '.3g2': "/Users/csuftitan/Desktop/newDesktop/Media/Video",
    '.3gp': "/Users/csuftitan/Desktop/newDesktop/Media/Video",
    '.avi': "/Users/csuftitan/Desktop/newDesktop/Media/Video",
    '.flv': "/Users/csuftitan/Desktop/newDesktop/Media/Video",
    '.h264': "/Users/csuftitan/Desktop/newDesktop/Media/Video",
    '.m4v': "/Users/csuftitan/Desktop/newDesktop/Media/Video",
    '.mkv': "/Users/csuftitan/Desktop/newDesktop/Media/Video",
    '.mov': "/Users/csuftitan/Desktop/newDesktop/Media/Video",
    '.mp4': "/Users/csuftitan/Desktop/newDesktop/Media/Video",
    '.mpg': "/Users/csuftitan/Desktop/newDesktop/Media/Video",
    '.mpeg': "/Users/csuftitan/Desktop/newDesktop/Media/Video",
    '.rm': "/Users/csuftitan/Desktop/newDesktop/Media/Video",
    '.swf': "/Users/csuftitan/Desktop/newDesktop/Media/Video",
    '.vob': "/Users/csuftitan/Desktop/newDesktop/Media/Video",
    '.wmv': "/Users/csuftitan/Desktop/newDesktop/Media/Video",
#Images
    '.ai': "/Users/csuftitan/Desktop/newDesktop/Media/Images",
    '.bmp': "/Users/csuftitan/Desktop/newDesktop/Media/Images",
    '.gif': "/Users/csuftitan/Desktop/newDesktop/Media/Images",
    '.ico': "/Users/csuftitan/Desktop/newDesktop/Media/Images",
    '.jpg': "/Users/csuftitan/Desktop/newDesktop/Media/Images",
    '.jpeg': "/Users/csuftitan/Desktop/newDesktop/Media/Images",
    '.png': "/Users/csuftitan/Desktop/newDesktop/Media/Images",
    '.ps': "/Users/csuftitan/Desktop/newDesktop/Media/Images",
    '.psd': "/Users/csuftitan/Desktop/newDesktop/Media/Images",
    '.svg': "/Users/csuftitan/Desktop/newDesktop/Media/Images",
    '.tif': "/Users/csuftitan/Desktop/newDesktop/Media/Images",
    '.tiff': "/Users/csuftitan/Desktop/newDesktop/Media/Images",
    '.CR2': "/Users/csuftitan/Desktop/newDesktop/Media/Images",
#Internet
    '.asp': "/Users/csuftitan/Desktop/newDesktop/Other/Internet",
    '.aspx': "/Users/csuftitan/Desktop/newDesktop/Other/Internet",
    '.cer': "/Users/csuftitan/Desktop/newDesktop/Other/Internet",
    '.cfm': "/Users/csuftitan/Desktop/newDesktop/Other/Internet",
    '.cgi': "/Users/csuftitan/Desktop/newDesktop/Other/Internet",
    '.pl': "/Users/csuftitan/Desktop/newDesktop/Other/Internet",
    '.css': "/Users/csuftitan/Desktop/newDesktop/Other/Internet",
    '.htm': "/Users/csuftitan/Desktop/newDesktop/Other/Internet",
    '.js': "/Users/csuftitan/Desktop/newDesktop/Other/Internet",
    '.jsp': "/Users/csuftitan/Desktop/newDesktop/Other/Internet",
    '.part': "/Users/csuftitan/Desktop/newDesktop/Other/Internet",
    '.php': "/Users/csuftitan/Desktop/newDesktop/Other/Internet",
    '.rss': "/Users/csuftitan/Desktop/newDesktop/Other/Internet",
    '.xhtml': "/Users/csuftitan/Desktop/newDesktop/Other/Internet",
#Compressed
    '.7z': "/Users/csuftitan/Desktop/newDesktop/Other/Compressed",
    '.arj': "/Users/csuftitan/Desktop/newDesktop/Other/Compressed",
    '.deb': "/Users/csuftitan/Desktop/newDesktop/Other/Compressed",
    '.pkg': "/Users/csuftitan/Desktop/newDesktop/Other/Compressed",
    '.rar': "/Users/csuftitan/Desktop/newDesktop/Other/Compressed",
    '.rpm': "/Users/csuftitan/Desktop/newDesktop/Other/Compressed",
    '.tar.gz': "/Users/csuftitan/Desktop/newDesktop/Other/Compressed",
    '.z': "/Users/csuftitan/Desktop/newDesktop/Other/Compressed",
    '.zip': "/Users/csuftitan/Desktop/newDesktop/Other/Compressed",
#Disc
    '.bin': "/Users/csuftitan/Desktop/newDesktop/Other/Disc",
    '.dmg': "/Users/csuftitan/Desktop/newDesktop/Other/Disc",
    '.iso': "/Users/csuftitan/Desktop/newDesktop/Other/Disc",
    '.toast': "/Users/csuftitan/Desktop/newDesktop/Other/Disc",
    '.vcd': "/Users/csuftitan/Desktop/newDesktop/Other/Disc",
#Data
    '.csv': "/Users/csuftitan/Desktop/newDesktop/Programming/Database",
    '.dat': "/Users/csuftitan/Desktop/newDesktop/Programming/Database",
    '.db': "/Users/csuftitan/Desktop/newDesktop/Programming/Database",
    '.dbf': "/Users/csuftitan/Desktop/newDesktop/Programming/Database",
    '.log': "/Users/csuftitan/Desktop/newDesktop/Programming/Database",
    '.mdb': "/Users/csuftitan/Desktop/newDesktop/Programming/Database",
    '.sav': "/Users/csuftitan/Desktop/newDesktop/Programming/Database",
    '.sql': "/Users/csuftitan/Desktop/newDesktop/Programming/Database",
    '.tar': "/Users/csuftitan/Desktop/newDesktop/Programming/Database",
    '.xml': "/Users/csuftitan/Desktop/newDesktop/Programming/Database",
    '.json': "/Users/csuftitan/Desktop/newDesktop/Programming/Database",
#Executables
    '.apk': "/Users/csuftitan/Desktop/newDesktop/Other/Executables",
    '.bat': "/Users/csuftitan/Desktop/newDesktop/Other/Executables",
    '.com': "/Users/csuftitan/Desktop/newDesktop/Other/Executables",
    '.exe': "/Users/csuftitan/Desktop/newDesktop/Other/Executables",
    '.gadget': "/Users/csuftitan/Desktop/newDesktop/Other/Executables",
    '.jar': "/Users/csuftitan/Desktop/newDesktop/Other/Executables",
    '.wsf': "/Users/csuftitan/Desktop/newDesktop/Other/Executables",
#Fonts
    '.fnt': "/Users/csuftitan/Desktop/newDesktop/Other/Fonts",
    '.fon': "/Users/csuftitan/Desktop/newDesktop/Other/Fonts",
    '.otf': "/Users/csuftitan/Desktop/newDesktop/Other/Fonts",
    '.ttf': "/Users/csuftitan/Desktop/newDesktop/Other/Fonts",
#Presentations
    '.key': "/Users/csuftitan/Desktop/newDesktop/Text/Presentations",
    '.odp': "/Users/csuftitan/Desktop/newDesktop/Text/Presentations",
    '.pps': "/Users/csuftitan/Desktop/newDesktop/Text/Presentations",
    '.ppt': "/Users/csuftitan/Desktop/newDesktop/Text/Presentations",
    '.pptx': "/Users/csuftitan/Desktop/newDesktop/Text/Presentations",
#Programming
    '.c': "/Users/csuftitan/Desktop/newDesktop/Programming/C&C++",
    '.class': "/Users/csuftitan/Desktop/newDesktop/Programming/Java",
    '.dart': "/Users/csuftitan/Desktop/newDesktop/Programming/Dart",
    '.py': "/Users/csuftitan/Desktop/newDesktop/Programming/Python",
    '.sh': "/Users/csuftitan/Desktop/newDesktop/Programming/Shell",
    '.swift': "/Users/csuftitan/Desktop/newDesktop/Programming/Swift",
    '.html': "/Users/csuftitan/Desktop/newDesktop/Programming/html",
    '.h': "/Users/csuftitan/Desktop/newDesktop/Programming/html",
#Spreadsheets
    '.ods' : "/Users/csuftitan/Desktop/newDesktop/Text/Microsoft/Excel",
    '.xlr' : "/Users/csuftitan/Desktop/newDesktop/Text/Microsoft/Excel",
    '.xls' : "/Users/csuftitan/Desktop/newDesktop/Text/Microsoft/Excel",
    '.xlsx' : "/Users/csuftitan/Desktop/newDesktop/Text/Microsoft/Excel",
#System
    '.bak' : "/Users/csuftitan/Desktop/newDesktop/Text/Other/System",
    '.cab' : "/Users/csuftitan/Desktop/newDesktop/Text/Other/System",
    '.cfg' : "/Users/csuftitan/Desktop/newDesktop/Text/Other/System",
    '.cpl' : "/Users/csuftitan/Desktop/newDesktop/Text/Other/System",
    '.cur' : "/Users/csuftitan/Desktop/newDesktop/Text/Other/System",
    '.dll' : "/Users/csuftitan/Desktop/newDesktop/Text/Other/System",
    '.dmp' : "/Users/csuftitan/Desktop/newDesktop/Text/Other/System",
    '.drv' : "/Users/csuftitan/Desktop/newDesktop/Text/Other/System",
    '.icns' : "/Users/csuftitan/Desktop/newDesktop/Text/Other/System",
    '.ico' : "/Users/csuftitan/Desktop/newDesktop/Text/Other/System",
    '.ini' : "/Users/csuftitan/Desktop/newDesktop/Text/Other/System",
    '.lnk' : "/Users/csuftitan/Desktop/newDesktop/Text/Other/System",
    '.msi' : "/Users/csuftitan/Desktop/newDesktop/Text/Other/System",
    '.sys' : "/Users/csuftitan/Desktop/newDesktop/Text/Other/System",
    '.tmp' : "/Users/csuftitan/Desktop/newDesktop/Text/Other/System",
}
profile_name = "csuftitan"
folder_to_track = '/Users/profile_name/Desktop/oldDesktop'
folder_destination = '/Users/csuftitan/Desktop/newDesktop'
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
	while True:
		time.sleep(10)
except KeyboardInterrupt:
	observer.stop()
observer.join()