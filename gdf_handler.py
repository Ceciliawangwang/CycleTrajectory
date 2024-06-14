import geopandas as gpd


# class GDFHandler:
#     def __init__(self,gdf):
#         self.gdf = gdf
#         self.total_distance_km = self.calculate_total_distance()

#     # static method
    

#     def calculate_total_distance(self):
#         """_summary_

#         Args:
#             gdf (GeoDataFrame): A GeoDataFrame in projected coordinate

#         Returns:
#             _type_: _description_
#         """
#         if self.gdf.crs is None or self.gdf.crs.is_geographic:
#             return "Using geographic coordinate now, please reproject it to a projected coordinate system !"
        
#         self.gdf['distance'] = self.gdf['geometry'].shift().distance(self.gdf['geometry'])
#         d = self.gdf['distance'].sum()/1000

#         return d  # unit: km
    

class GDFHandler(gpd.GeoDataFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.total_distance_km = self.calculate_total_distance()

    def calculate_total_distance(self):
        """Calculate the total distance"""
        if self.crs is None or self.crs.is_geographic:
            return "Using geographic coordinate system, please reproject it to a projected coordinate system!"

        self['distance'] = self['geometry'].shift().distance(self['geometry'])
        total_distance = self['distance'].sum() / 1000  # meter to kilometer
        return total_distance