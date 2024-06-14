import os
import pandas as pd
import gpxpy

from utils import get_speed_values


class GPXHandler:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_size_kb = self.get_file_size()
        self.gpx_data = self.load_gpx()


    def get_file_size(self):
        size = os.path.getsize(self.file_path)/ 1024   # size in kb
        return size    # unit: kb
    

    def load_gpx(self):
        with open(self.file_path, 'r') as file:
            return gpxpy.parse(file)
        

    def gpx_to_df(self):
        """_summary_

        Args:
            gpx (_type_): _description_

        Returns:
            _type_: _description_
        """
        points = []
        
        for segment in self.gpx_data.tracks[0].segments:
            for p in segment.points:
                speed_2d, speed_3d = get_speed_values(p)  # function: get_speed_values()
                points.append({
                    'time': p.time,
                    'latitude': p.latitude,
                    'longitude': p.longitude,
                    'elevation': p.elevation,
                    'speed_2d': speed_2d,
                    'speed_3d': speed_3d
                })
        
        df = pd.DataFrame.from_records(points)
        return df
