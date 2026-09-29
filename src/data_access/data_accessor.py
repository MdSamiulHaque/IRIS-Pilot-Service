import geopandas as gpd
import pandas as pd
from typing import List, Dict, Any
import random

class DataAccessor:
    def __init__(self, endpoint: str):
        self.endpoint = endpoint

    def extract(self) -> gpd.GeoDataFrame:
        import json
        with open(self.endpoint, 'r') as f:
            data = json.load(f)
        gdf = gpd.GeoDataFrame.from_features(data["features"])
        # Set the CRS to 4326 as it is standard for GeoJSON
        gdf.set_crs(epsg=4326, inplace=True)
        return gdf

    def transform(self, gdf: gpd.GeoDataFrame) -> List[Dict[str, Any]]:
        gdf = gdf.copy()
        
        if 'eco_points_per_m2' not in gdf.columns:
            gdf['eco_points_per_m2'] = None
        gdf['eco_points_per_m2'] = pd.to_numeric(gdf['eco_points_per_m2'], errors='coerce')
        
        if 'source_date' in gdf.columns:
            gdf['source_date'] = pd.to_datetime(gdf['source_date'], errors='coerce')
        else:
            gdf['source_date'] = pd.NaT
            
        if 'uncertainty' not in gdf.columns:
            gdf['uncertainty'] = None
            
        gdf['site_suitability'] = gdf.apply(self._evaluate_site, axis=1)
        
        # Drop any row that contains missing values in our strict data contracts
        required_cols = ['site_name', 'eco_points_per_m2', 'country_code', 'geometry', 'source_date']
        gdf = gdf.dropna(subset=required_cols)
        
        records = []
        for _, row in gdf.iterrows():
            geom_val = f"SRID=4326;{row['geometry'].wkt}"
            
            record = {
                'site_name': row['site_name'],
                'eco_points_per_m2': row['eco_points_per_m2'],
                'country_code': row['country_code'],
                'geom': geom_val,
                'site_suitability': row['site_suitability'],
                'source_date': row['source_date'].to_pydatetime()
            }
            if pd.notnull(row['uncertainty']):
                record['uncertainty'] = row['uncertainty']
            records.append(record)
        return records

    def _evaluate_site(self, row: pd.Series) -> bool:
        if pd.notnull(row.get('eco_points_per_m2')) and row.get('eco_points_per_m2') > 200:
            return True
        return False
