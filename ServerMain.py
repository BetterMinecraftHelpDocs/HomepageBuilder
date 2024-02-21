from flask import Flask, request
from Core.Project import Project, PageNotFoundError
from Core.FileIO import readYaml
from Core.Debug import LogFatal,LogError,LogInfo
from Server.project_updater import request_update
import traceback
import os
import subprocess
app = Flask(__name__)

@app.route("/pull",methods=['POST'])
def git_update():
    status,data = request_update(request,server.project_dir,
        server.config['github_secret'])
    if status == 200:
        server.clear_cache()
        server.cache.clear()
        LogInfo('[Server] Cache cleared.')
    else:
        LogError(data)
    return data,status

@app.route("/")
def index_page():
    if server.defult_page != None:
        return getpage(server.defult_page)
    else:
        return 'No Page Found',404
    
@app.route("/<path:alias>")
def getpage(alias:str):
    if alias.endswith('/version') or alias == 'version':
        return server.getVersion()
    while alias.endswith('/'):
        alias = alias[:-1]
    try:
        if alias.endswith('.json'):
            return server.getPageJson(alias[:-5])
        if alias.endswith('.xaml'):
            alias = alias[:-5]
        return server.getPageXaml(alias)
    except PageNotFoundError:
        return 'No Page Found',404
    except Exception:
        LogError(traceback.format_exc())
        return 'Inner Error Occured',500
    
class Server: 
    def __init__(self):
        envpath = os.path.dirname(os.path.dirname(__file__))
        self.config_path = f"{envpath}{os.path.sep}server_config.yml"
        self.cache = {}
        try:
            self.config = readYaml(self.config_path)
            self.project_path = self.config['project_path']
            self.project = Project(self.project_path)
            self.defult_page = self.project.defult_page
            self.project_dir = os.path.dirname(self.project_path)
        except Exception as e:
            LogFatal(e.args)
            exit() 
    
    def clear_cache(self):
        self.project = Project(self.project_path)
        self.cache.clear()
    
    def getVersion(self):
        if 'version' not in self.cache:
            githash = subprocess.check_output('git rev-parse HEAD',cwd = self.project_dir, shell=True)
            githash = githash.decode("utf-8")
            self.cache['version'] = githash
        return self.cache['version']
    
    def getPageJson(self,alias):
        key = alias + '.json'
        if key not in self.cache:
            name = self.project.get_page_name(alias)
            if name is None:
                name = 'Untitled Page'
            self.cache[key] = name
        return f'{{"Title":"{self.cache[key]}"}}'
    
    def getPageXaml(self,alias):
        if alias not in self.cache:
            self.cache[alias] = self.project.get_page_xaml(alias)
        return self.cache[alias]

server = Server()
if __name__ == "__main__":
    app.run(port=6608)