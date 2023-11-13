from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        data = toml.loads(content)['tool']['poetry']
        print('DATA: ',data)

        name = data['name']
        des = data['description']
        dep = data['dependencies']
        toimi = data['group']['dev']['dependencies']

        lic = data['license']
        aut = data['authors']
       
        # Tulostus
      
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, des, dep, toimi, lic, aut)

