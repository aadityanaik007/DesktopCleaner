# DesktopCleaner
Desktop Cleaner Utility for MacOS to move files from the Desktop to Another Folder in an Organized and Segregated manner.


## Setup
This project requires Python3, PIP.

## How it works
- Track a specific directory(e.g: desktop), if new file is added then move
- move files
- run in the background
- System for file organization
  - Folders for each file type category (e.g Images, Video, Audio, Text etc.)
  - Within folders we need to organise by date, create subfolders with date as name something like
    - 2019 September 9th
- need to find all file types to check what file has been added

## Installation
- Clone the repository.
- Make the appropriate changes in the desktopCleaner.py file like seting the tracking and destination folder and user profile name.
- Install the requirement.txt file (pip install -r requirement.txt).
- Run the desktopCleaner.py file (python3 desktopCleaner.py)

# Usage
- To test the working, add a file inside the tracking folder.