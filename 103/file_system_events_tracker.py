import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir='C:/Users/junin/Downloads'

class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"olá,{event.src_path}foi criado")
        
    def on_deleted(self, event):
        print(f"opa! alguem excluiu{event.src_path}")
        
    def on_modified(self, event):
        print(f"olá,{event.src_path}foi modificado")
        
    def on_moved(self, event):
        print(f"alguem moveu{event.src_path}para{event.dest_path}")
        
event_handle=FileEventHandler()

observer=Observer()

observer.schedule(event_handle,from_dir,recursive=True)

observer.start()

try:
    while True:
        time.sleep(2)
        print("executando")
except KeyboardInterrupt:
    print("interrompido")
    observer.stop()