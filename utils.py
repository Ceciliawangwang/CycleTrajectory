import pandas as pd
import geopandas as gpd
import gpxpy
from shapely.geometry import Point
import os



"""This file includes the gpx preparation functions

"""


def get_speed_values(p):
    """This is a function extract speed values from .gpx files

    Args:
        p (_type_): _description_

    Returns:
        v1 (_type_): value of speed_2d
        v2 (_type_): value of speed_3d
    """
    v1 = None
    v2 = None
    for e in p.extensions:
        if e.tag == 'speed_2d':
            for echild in list(e):
                if echild.tag == 'value':
                    # print(echild.text)
                    v1 = echild.text

        elif e.tag == 'speed_3d':
            for echild in list(e):
                if echild.tag == 'value':
                    v2 = echild.text

    return v1, v2




## ================================ remove to GPXHandler ====================================
# def gpx_to_df(gpx):
#     """_summary_

#     Args:
#         gpx (_type_): _description_

#     Returns:
#         _type_: _description_
#     """
#     points = []
    
#     for segment in gpx.tracks[0].segments:
#         for p in segment.points:
#             speed_2d, speed_3d = get_speed_values(p)  # function: get_speed_values()
#             points.append({
#                 'time': p.time,
#                 'latitude': p.latitude,
#                 'longitude': p.longitude,
#                 'elevation': p.elevation,
#                 'speed_2d': speed_2d,
#                 'speed_3d': speed_3d
#             })
    
#     df = pd.DataFrame.from_records(points)
#     return df
## ================================= remove to GPXHandler ====================================


def df_to_gdf(df):
    """ This is a function ... (could be extended then)

    Args:
        df (DataFrame): _description_

    Returns:
        _type_: _description_
    """
    geometry = [Point(lon, lat) for lon, lat in zip(df['longitude'], df['latitude'])]
    gdf = gpd.GeoDataFrame(df, geometry = geometry, crs= 'EPSG:4326')
    return gdf



def df_to_gpx(data):
    """Convert a DataFrame to a GPX object.

    Args:
        data (DataFrame): The DataFrame to be converted.

    Returns:
        gpx (GPX): The GPX object created from the DataFrame.
    """

    gpx = gpxpy.gpx.GPX()

    # Create a new GPX track
    gpx_track = gpxpy.gpx.GPXTrack()
    gpx.tracks.append(gpx_track)

    # Create a new GPX track segment
    gpx_segment = gpxpy.gpx.GPXTrackSegment()
    gpx_track.segments.append(gpx_segment)

    # Add track points
    for index, row in data.iterrows():
        gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(row['latitude'], 
                                                          row['longitude'], 
                                                          elevation=row['elevation'], 
                                                          time=row['time'],
                                                          speed=row['speed_2d'])) 
    return gpx




def save_gpx(gpx, root_path, filename):
    """This is a function to save a GPX object to a file.

    Args:
        gpx (GPX): The GPX object to be saved.
        root_path (str): The root directory where the GPX file will be saved.
        filename (str): The name of the file to save the GPX data.
    """
    path = os.path.join(root_path, filename)
    with open(path, "w") as f:
        f.write(gpx.to_xml())




def reprojection(gdf, c):
    """This is a function for reprojection

    Args:
        gdf (_type_): geodataframe to be projected
        c (str): objective projection (as a number string, e.g., "27700")

    Returns:
        gdf_projected (_type_): projected geodataframe
    """

    # Construct the full CRS string

    ns = f'EPSG:{c}'
    gdf_projected =  gdf.to_crs(ns)
    
    return gdf_projected



# def test():
#     df = fdsfw