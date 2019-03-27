"""Данный скрипт сортирует все фотографии, указанные по пути в your_path
    сортировка идёт по году и месяцу создания фотографии"""

import os
import time
import shutil

your_path = os.path.join('icons')


class PhotoArrangement:

    def __init__(self, path):
        self.path = path
        self.time = {}
        self.year_month = {}
        self.full_file_path = {}

    def execute_files(self):
        for dirpath, dirnames, filenames in os.walk(self.path):
            for file in filenames:
                self.full_file_path[file] = os.path.join(dirpath, file)

    def set_time(self):
        for file, time_path in self.full_file_path.items():
            unix_time = os.path.getmtime(time_path)
            self.time[file] = time.gmtime(unix_time)

    def pick_year_month(self):
        for file, filetime in self.time.items():
            self.year_month[file] = [str(filetime[0]), str(filetime[1])]

    def arrange(self):
        for file, filetime in self.year_month.items():
            path_year_month = os.path.join(os.path.dirname(self.path), 'icons_by_year', filetime[0], filetime[1])
            if not os.path.exists(path_year_month):
                os.makedirs(path_year_month)
            shutil.copy2(self.full_file_path[file], path_year_month)

    def run(self):
        self.execute_files()
        self.set_time()
        self.pick_year_month()
        self.arrange()


sort_photo = PhotoArrangement(path=your_path)
sort_photo.run()
