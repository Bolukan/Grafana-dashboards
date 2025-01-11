import os
import json

# Define the mapping of types to new UIDs
type_to_uid = {
    "influxdb": "de9ejk2fk91j4b", # Residence
    "marcusolsson-json-datasource": "be8pllgxdcq2ob"
}

# Function to update the 'uid' based on the 'type'
def update_datasource_uid(panel):
    if isinstance(panel, dict):
        datasource = panel.get("datasource")
        if datasource:
            current_type = datasource.get("type")
            if current_type in type_to_uid:
                datasource["uid"] = type_to_uid[current_type]
        
        targets = panel.get("targets")
        if targets:
            for target in targets:
                target_datasource = target.get("datasource")
                if target_datasource:
                    current_type = target_datasource.get("type")
                    if current_type in type_to_uid:
                        target_datasource["uid"] = type_to_uid[current_type]

def process_json(json_data):
    json_data["version"] = 1
    panels = json_data.get("panels", [])
    for panel in panels:
        update_datasource_uid(panel)

# Example JSON input (you can replace this with reading from a file)
def load_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def find_files_in_subdirectory(subdirectory_name):
    # Get the path of the current Python file
    current_directory = os.path.dirname(os.path.realpath(__file__))
    subdirectory_path = os.path.join(current_directory, subdirectory_name)

    # Check if the subdirectory exists and return files
    if os.path.isdir(subdirectory_path):
        return [os.path.join(subdirectory_path, f) for f in os.listdir(subdirectory_path) if os.path.isfile(os.path.join(subdirectory_path, f))]
    else:
        return []
  
def find_files_in_directory(directory):
    return [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

dashboard_filenames = find_files_in_subdirectory("dashboard")
for dashboard_filename in dashboard_filenames:
    data = load_file(dashboard_filename)
    process_json(data)
    updated_json = json.dumps(data, indent=4)
    with open(dashboard_filename, 'w', encoding='utf-8') as file:
        file.write(updated_json)
