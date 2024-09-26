# CycleTrajectory: An End-to-End Pipeline for Enriching and Analyzing GPS Trajectories to Understand Cycling Behavior and Environment


## Abstract
Global positioning system (GPS) trajectories recorded by mobile phones or action cameras offer valuable insights into sustainable mobility, as they provide fine-scale spatial and temporal characteristics of individual travel. However, the high volume, noise, and lack of semantic information in this data poses challenges for storage, analysis, and applications. To address these issues, we propose an end-to-end pipeline for processing high-sampling rate GPS trajectory data from action cameras, leveraging OpenStreetMap (OSM) for semantic enrichment. The methodology includes (1) Data Preparation, which includes filtration, noise removal, and resampling; (2) Map Matching, which accurately aligns GPS points with road segments using the OSRM API; (3) OSM Data integration to enrich trajectories with road infrastructure details; and (4) Variable Calculation to derive metrics like distance, speed, and infrastructure usage. This approach enhances efficient GPS data preparation and facilitates a deeper understanding of cycling behavior and the cycling environment.

<img width="947" alt="preprocessing" src="https://github.com/user-attachments/assets/67d3834b-1298-4973-8d79-a50d4f7a37f1">

## Software and tools
- **Python** for data preprocessing and analysis.
- **PostgreSQL with PostGIS** for data management and storage.
- **QGIS** for data visualization.
- **OSRM and Overpass API** for map matching and data integration.


## Data
CycleTrajectory is designed for processing GPS trajectory data, specifically focusing on data from GoPro devices.

## Functions
- ```1_merge_gpx.py``` and ```1_timestamp.ipynb```: Used for the initial preprocessing of GPS trajectories. These scripts and notebooks correct timestamps and merge multiple GPX files into a complete trip.

- ```.ipynb```: Snaps raw GPS data to road segments using the OSRM API, improving positional accuracy and preparing data for semantic enrichment.

- ```.ipynb```: Enhances GPS data by integrating infrastructure data from OpenStreetMap.

- ```4_variables_calculation.ipynb```: Computes cycling-related variables such as average speed, average moving speed, time spent under various speed limits, and time spent on different types of cycling infrastructure.


## Cite
If you find CycleTrajectory useful for your research, please cite us!

**Authors**: [Meihui Wang](https://github.com/Ceciliawangwang), James Haworth, [Ilya Ilyankou](https://github.com/ilyankou), Nicola Christie
```
@misc{wang2024cycletrajectoryendtoendpipelineenriching,
      title={CycleTrajectory: An End-to-End Pipeline for Enriching and Analyzing GPS Trajectories to Understand Cycling Behavior and Environment}, 
      author={Meihui Wang and James Haworth and Ilya Ilyankou and Nicola Christie},
      year={2024},
      eprint={2406.10069},
      archivePrefix={arXiv},
      primaryClass={cs.DB},
      url={https://arxiv.org/abs/2406.10069}, 
}
```
