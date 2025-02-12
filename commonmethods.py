import json
import pickle
import os
import Objects.tenno
from pythonmonkey import require
from commonattributes import Commonattributes

class Commonmethods:

    common_attributes_object: Commonattributes

    def __init__(self, common_attributes_object: Commonattributes):
        self.common_attributes_object = common_attributes_object
        pass

    def readyPages(self, parent):
        from Pages.startpage import Startpage
        from Pages.pageone import Pageone
        from Pages.pagetwo import Pagetwo
        from Pages.homepage import Homepage
        for P in (Startpage, Pageone, Pagetwo, Homepage):
            page = P(parent, self.common_attributes_object)
            self.common_attributes_object.pages.update({P : page})

    def changePage(self, page):
        page.mainframe.tkraise()

    def parseJSON(self, json_string) -> dict:
        try:
            data = json.loads(json_string)
            return data
        except json.JSONDecodeError as error:
            print(f"Error in JSON parsing: {error}")

    async def parseTest(self):
        try:
            print('Starting parseTest...')
            jsgrabber = require('./jsgrabber')
            print('Successfully got jsgrabber.')
            print('Data type of jsgrabber: ' + str(type(jsgrabber)))
            data = await jsgrabber.findAnItem('/Lotus/Powersuits/Excalibur/ExcaliburPrime')
            print('Successfully got data from findAnItem.')
            print("This is the unparsed data:" + str(data))
            parsed_data = json.loads(data)
            print("This is the parsed data: " + str(parsed_data))
        except Exception as error:
            print('Something went wrong :< - ' + str(error))

    def writeFile(self, user_profile: Objects.tenno.Tenno):
        try:
            up_file = open('user_profile_file', 'wb')
            pickle.dump(user_profile, up_file)
            up_file.close()
        except Exception as error:
            print(f"Error in writing file: {error}")

    def loadFile(self) -> Objects.tenno.Tenno:
        try:
            up_file = open('user_profile_file', 'rb')
            user_profile = pickle.load(up_file)
            up_file.close()
            return user_profile
        except Exception as error:
            print(f"Error in loading file: {error}")

    def deleteFile(self):
        if os.path.isfile('user_profile_file'):
            os.remove('user_profile_file')
        else:
            print("User file does not exist.")