def write_cred_to_json(name,username,email_id):
        # importing the module
        import json
        with open(r'C:\Users\tejas\Desktop\22-01-22\.qt_for_python\uic\settings.json') as settings_json_file:
            data = json.load(settings_json_file)
            data["log"]["name"]=name
            data["log"]["email_id"]=email_id
            data["log"]["username"]=username
            
        with open(r"C:\Users\tejas\Desktop\22-01-22\.qt_for_python\uic\settings.json", "w") as settings_json_file:
            json.dump(data, settings_json_file,indent=4)
            
write_cred_to_json("","","")  