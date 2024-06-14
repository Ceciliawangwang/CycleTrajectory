import os
import pandas as pd

from gpx_handler import GPXHandler
from utils import df_to_gpx

######### completed #########

def read_gpx_files(folder_path):
    trajectories = {}
    for filename in os.listdir(folder_path):
        if filename.endswith('.gpx'):
            # Look for the location of 'GS' or 'GH'
            gs_gh_index = filename.find('GS') if 'GS' in filename else filename.find('GH')
            if gs_gh_index != -1:
                # Get trajectory ID
                identifier = filename[gs_gh_index:gs_gh_index+2]  # 'GS' or 'GH'
                trajectory_id = filename[-7:-4]  # the last 3 digits
                full_id = identifier + trajectory_id
                if full_id not in trajectories:
                    trajectories[full_id] = []
                trajectories[full_id].append(filename)
    return trajectories


def merge_gpx_data(files, folder_path):
    merged_data = None
    for file in files:
        file_path = os.path.join(folder_path, file)
        gpx_hdl = GPXHandler(file_path)
        data = gpx_hdl.gpx_to_df()
        merged_data = pd.concat([merged_data, data]) if merged_data is not None else data
    return merged_data


def save_gpx_file(merged_gpx, output_path, participant_id, full_id):
    with open(os.path.join(output_path, f'{participant_id}_{full_id}.gpx'), 'w') as f:
        f.write(merged_gpx.to_xml())


def process_folder(top_folder, output_path):
    for root, dirs, files in os.walk(top_folder):
        participant_id = os.path.basename(root)  # Get the participant ID
        trajectories = read_gpx_files(root)
        for full_id, files in trajectories.items():
            files.sort(key=lambda x: int(x[x.find('GS') + 2:x.find('GS') + 4]) if 'GS' in x else int(x[x.find('GH') + 2:x.find('GH') + 4]))
            merged_data = merge_gpx_data(files, root)
            merged_gpx = df_to_gpx(merged_data)
            save_gpx_file(merged_gpx, output_path, participant_id, full_id)



folder_path = '/Users/ceciliawang/Documents/PhD/pyprojects/metadata/data/gpx_filtered/'
output_path = '/Users/ceciliawang/Documents/PhD/pyprojects/metadata/data/gpx_merged'
process_folder(folder_path, output_path)