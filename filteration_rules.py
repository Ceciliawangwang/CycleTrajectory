

import pandas as pd
# import geopandas as gpd
import os
import shutil
# import osmnx as ox



# R1: Data size < 100

def move_small_files(folder_path, removed_path, file_size):

    for filename in os.listdir(folder_path):
        # 检查文件名是否符合条件
        if ('GS01' in filename or 'GH01' in filename):
            full_file_path = os.path.join(folder_path, filename)

            # 获取文件大小并转换为kb
            file_size = os.path.getsize(full_file_path) / 1024

            if file_size < file_size:
                # 如果文件小于100kb，移动文件
                shutil.move(full_file_path, os.path.join(removed_path, filename))
                print(f"Moved: {filename}")
            else:
                # 文件大于等于100kb，保留文件
                print(f"Kept: {filename}")


# R2: Jumping points out of London

# city = ox.geocode_to_gdf('Greater London, UK') # if only mention London, City of London will not included


def points_within_city(data, city):
    """_summary_

    Args:
        data (GeoDataFrame): A GeoDataFrame containing geospatial data points. It should have a defined CRS and geometries.
        city (GeoDataFrame): A GeoDataFrame representing the city boundary. This should contain a single geometry of the city, and have a defined CRS.

    Returns:
        masked_data (GeoDataFrame)_type_: A GeoDataFrame inside the city boundary.
    """
    if data.crs != city.crs:
        data = data.to_crs(city.crs)
    
    mask = data.within(city.iloc[0].geometry)
    masked_data = data[mask]
    return masked_data


# R3: Total distance

# def total_distance(gdf):
#     """_summary_

#     Args:
#         gdf (GeoDataFrame): A GeoDataFrame in projected coordinate

#     Returns:
#         _type_: _description_
#     """
#     gdf['distance'] = gdf['geometry'].shift().distance(gdf['geometry'])
#     dis_km = gdf['distance'].sum()/1000

#     return dis_km


# R4: 判断连续性


def calculate_speed(row, prev_row):
    if prev_row is None:
        return 0
    time_diff = (row['time'] - prev_row['time']).total_seconds() / 3600  # Hours

    if time_diff == 0:
        return 0  # 如果时间差为零，返回速度为0

    distance = (row['geometry'].distance(prev_row['geometry']))/1000 # Euclidean distance
    speed = abs(distance/time_diff)
    return speed 


def filter_by_speed_threshold(gdf, k):  # to be tested, if not work, delete it
    """
    Filters a GeoDataFrame by removing rows where the speed between consecutive points exceeds a threshold.

    Parameters:
    gdf (GeoDataFrame): The input GeoDataFrame with 'timestamp' and 'geometry' columns.
    k (float): The speed threshold (in kilometers per hour).

    Returns:
    GeoDataFrame: The filtered GeoDataFrame.
    """


# List to hold the indices of rows to keep
    indices_to_keep = []

    kept_row = None
    for index, row in gdf.iterrows():
        # Always keep the first row
        if kept_row is None:
            indices_to_keep.append(index)
            kept_row = row
        else:
            speed = calculate_speed(row, kept_row)
            if speed <= k:
                indices_to_keep.append(index)
                kept_row = row  # Update the kept row for next iteration

    # Filter the GeoDataFrame using the indices
    filtered_gdf = gdf.loc[indices_to_keep]
    return filtered_gdf



# R5: stationary points at the beginning
def remove_initial_zero_rows(gdf, column_name):
    """
    删除GeoDataFrame开头连续的、指定列值等于0的行。

    Args:
        gdf (GeoDataFrame): 输入的GeoDataFrame。
        column_name (str): 要检查的列名。

    Returns:
        GeoDataFrame: 过滤后的GeoDataFrame。
    """
    # 确保列值为数值类型
    gdf[column_name] = pd.to_numeric(gdf[column_name], errors='coerce')
    
    # 找到第一个非零值的索引
    first_non_zero_index = (gdf[column_name] != 0).idxmax()

    # 删除连续的、列值等于0的行
    if first_non_zero_index != 0:
        return gdf.iloc[first_non_zero_index:]
    else:
        return gdf


# reversed_gdf = gdf.iloc[::-1].reset_index(drop=True)  # for the Series 01


