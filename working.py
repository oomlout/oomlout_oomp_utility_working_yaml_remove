import os
import time
# An oomp utility to:
# delete all the working,yaml files to cleanse before rebuilding from base.yaml 
# 
# This is part of OOMP the Oopen Organization Method For Parts. For more details: https://github.com/oomlout/oomp_base  


def main(**kwargs):
    recursive_through_parts(**kwargs)    
    
def recursive_through_parts(**kwargs):
    folder = kwargs.get("folder", os.path.dirname(__file__))
    kwargs["folder"] = folder
    folders = os.listdir(folder)
    for item in folders:
        item_absolute = os.path.join(folder, item)
        if os.path.isdir(item_absolute):
            #if base.yaml exists in the folder or working,yaml exists in the folder
            file_yaml_base = os.path.join(item_absolute, "base.yaml")
            file_yaml_working = os.path.join(item_absolute, "working.yaml")
            if os.path.exists(file_yaml_base) or os.path.exists(file_yaml_working):
                kwargs["directory"] = item_absolute
                process_part(**kwargs)

def process_part(**kwargs):
    directory = kwargs.get("directory", os.getcwd())    
    kwargs["directory"] = directory        
    print("Processing: {}".format(directory))
    #if working.yaml exists in directory delete it
    if os.path.exists(os.path.join(directory, "working.yaml")):
        print(f"Deleting working.yaml from {directory}")
        os.remove(os.path.join(directory, "working.yaml"))
        #delay 1 second
        #time.sleep(1)
    else:
        print(f"working.yaml does not exist in {directory}")
        #delay 1 second
        #time.sleep(1)

if __name__ == '__main__':
    #folder is the path it was launched from
    
    kwargs = {}
    folder = os.path.dirname(__file__)
    #folder = "C:/gh/oomlout_oomp_builder/parts"
    #folder = "C:/gh/oomlout_oomp_part_generation_version_1/parts"
    #folder = "C:/gh/oomlout-organization/oomlout_oomp_current_version/parts"
    kwargs["folder"] = folder
    main(**kwargs)