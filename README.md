# An End-to-End Pipeline for Enriching and Analyzing GPS Trajectories to Understand Cycling Behavior and Environment

## Abstract
Global positioning system (GPS) trajectories recorded by mobile phones or action cameras offer valuable insights into sustainable mobility, as they provide fine-scale spatial and temporal characteristics of individual travel. However, the high volume, noise, and lack of semantic information in this data poses challenges for storage, analysis, and applications. To address these issues, we propose an end-to-end pipeline for processing high-sampling rate GPS trajectory data from action cameras, leveraging OpenStreetMap (OSM) for semantic enrichment. The methodology includes (1) Data Preparation, which includes filtration, noise removal, and resampling; (2) Map Matching, which accurately aligns GPS points with road segments using the OSRM API; (3) OSM Data integration to enrich trajectories with road infrastructure details; and (4) Variable Calculation to derive metrics like distance, speed, and infrastructure usage. This approach enhances efficient GPS data preparation and facilitates a deeper understanding of cycling behavior and the cycling environment.

## Software and tools
Python 3.10
Libraries: gpmf-parser, gpxpy, ....
Web Service: OSRM, Overpass

## Main Functions
### 0 GPS extraction from GoPro Videos


### 1 Data Processing

### 2 Map Matching

### 3 Senmantic Enrichment

### 4 Variables Calculation
