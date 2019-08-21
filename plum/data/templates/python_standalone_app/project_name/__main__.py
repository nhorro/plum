VERSION_MAJOR=1
VERSION_MINOR=0
VERSION_REVISION=0

def app():    
	print("[project_name]")
    print("Version %d.%d.%d                       " % (VERSION_MAJOR, VERSION_MINOR, VERSION_REVISION) )

    #TODO: Application code here

    try:
        print("Command line application")
    except KeyboardInterrupt:
        print("Project generation cancelled by user.")  

app()