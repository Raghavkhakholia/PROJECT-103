import os
import time
import random
import sys
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


from_dir = "C:/Users/ragha/Downloads"
to_dir = "C:/Users/ragha/OneDrive/Desktop/Downloaded_files"

class FileMovementHandler(FileSystemEventHandler):
    def on_created(self,event):
        print(f"Hey, {event.src_path} has been created !!")
    def on_modified(self,event):
        print(f"Hey, {event.src_path} has been modified !!")
    def on_deleted(self,event):
        print(f"Oops! Someone deleted {event.src_path}!")
    def on_moved(self,event):
        print(f"Hey, Someone moved {event.src_path}!")

event_handler = FileMovementHandler()
observer = Observer()
observer.schedule(event_handler,from_dir,recursive=True)
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()
