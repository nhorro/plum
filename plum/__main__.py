import re
import os
import shutil
import json
import sys
from glob import glob

VERSION_MAJOR=1
VERSION_MINOR=0
VERSION_REVISION=0

TEMPLATE_PATH = os.path.dirname(os.path.realpath(__file__)) + "/data/templates"
TEMPLATE_SPEC_FILENAME = "template.json"

def list_project_templates():
    result = []
    template_directories = glob("%s/*/" % TEMPLATE_PATH )
    for t in template_directories:
        result.append(os.path.basename(os.path.normpath(t)))
    return result

def process_file(filename, value_list):
    with open(filename) as f:
        text = f.read()        
    with open(filename, 'w') as f:
        f.write(re.sub(r'\[(\w+)\]', lambda x: value_list.get(x.group(1), x.group(1)), text))

def plum_app():
    print("██████╗ ██╗     ██╗   ██╗███╗   ███╗██╗   ")
    print("██╔══██╗██║     ██║   ██║████╗ ████║██║   ")
    print("██████╔╝██║     ██║   ██║██╔████╔██║██║   ")
    print("██╔═══╝ ██║     ██║   ██║██║╚██╔╝██║╚═╝   ")
    print("██║     ███████╗╚██████╔╝██║ ╚═╝ ██║██╗   ")
    print("╚═╝     ╚══════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝   ")
    print("Plum is a minimalistic tool for project scaffolding.")
    print("Version %d.%d.%d                       " % (VERSION_MAJOR, VERSION_MINOR, VERSION_REVISION) )

    #with open('data/config.json') as json_data_file:
    #        config = json.load(json_data_file)

    available_templates = list_project_templates()
    project_template = ''

    try:
        if project_template == '':
            print("Available project templates in %s:" % TEMPLATE_PATH )
            i = 0
            for t in available_templates:
                print(" %d: %s" % (i, t) )
                i = i + 1
            template_index = int(input("Enter template:"))
            if template_index>=0 and template_index<len(available_templates):
                project_template = available_templates[template_index]
            else:
                print("Invalid template.")
                sys.exit(0)    
        elif project_template not in available_templates:
            print("Invalid template.")
            sys.exit(0)

        # Input data (TODO: do from CLI)
        with open("%s/%s/%s" % (TEMPLATE_PATH, project_template,TEMPLATE_SPEC_FILENAME)) as f:
            parameter_list = json.loads(f.read())

        value_list = {}
        for k,v in parameter_list.items():
            value = input("%s [%s]:" % (k,v))
            if value=='':
                value = v
            value_list[k]=value

        project_name = value_list['project_name']
        project_output_path="%s/%s/" % ("output",project_name)

        yes = input("Generate project '%s' in '%s' ? [Y]" % ( project_name, project_output_path))
        if 'Y' == yes or 'y' == yes or '' == yes:
            # Remove directory if it exists        
            if os.path.exists(project_output_path) and os.path.isdir(project_output_path):
                shutil.rmtree(project_output_path)

            # Copy template
            template_project_path = "%s/%s" % (TEMPLATE_PATH, project_template)
            print("Copying template %s " % template_project_path)
            shutil.copytree(template_project_path, project_output_path, ignore=shutil.ignore_patterns(TEMPLATE_SPEC_FILENAME) )                   

            # Get all files in directory                    
            files = glob(project_output_path + "**/*", recursive=True)
            files.extend(glob(project_output_path + ".*", recursive=True)) #glob is not seeing .cproject and .project

            for f in files:
                if os.path.isfile(f):
                    print("Processing file: ", f)
                    process_file(f, value_list)
                else:
                    print("Skipping ", f)

            print("Project generation completed.")
        else:
            print("Project generation cancelled by user.")
            sys.exit(0)
    except KeyboardInterrupt:
        print("Project generation cancelled by user.")  

plum_app()