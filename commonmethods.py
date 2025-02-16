import json, pickle, os, subprocess
from Objects import tenno
from pythonmonkey import require
from tkinter import *
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

    async def parseTest2(self):
        try:
            print('Starting parseTest2...')
            find_module = require('./node_modules/warframe-items/utilities/find.mjs')
            if find_module is None:
                print('Did not successfully pull the find module.')
                return
            else:
                print('Successfully pulled find module.')
                print('Data type of find_module: ' + str(type(find_module)))
                data = await find_module.findItem('/Lotus/Powersuits/Excalibur/ExcaliburPrime')
                if data is None:
                    print('Data retrival was unsuccessful.')
                    return
                else:
                    print('Data retrival successfull!')
                    print('This is the unparsed data: ' + str(data))
                    parsed_data = json.loads(data)
                    if parsed_data is None:
                        print('Did not successfully parse data.')
                        return
                    else:
                        print('Successfully parsed data.')
                        print('This is the parsed data: ' + str(parsed_data))
                        print('Yay!')
        except Exception as error:
            print('Something went very wrong... ' + str(error))

    async def parseTest3(self):
        print('Starting parseTest3...')
        try:
            returned_item = await self.execute_js_with_node('./jsgrabber.js', '/Lotus/Powersuits/Excalibur/ExcaliburPrime')
            if returned_item is None:
                print('Did not get a returned item.')
            else:
                print('Successfully got a returned item!')
                print('Here is the unparsed data ----')
                print(returned_item)
                print('----')
                parsed_item = json.loads(returned_item)
                if parsed_item is None:
                    print('Did not parse the returned item.')
                else:
                    print('Item successfully parsed!')
                    print('Here is the parsed data ----')
                    print(parsed_item)
                    print('----')
                    print('Yay!')
        except Exception as error:
            print('Something went wrong :(')
            print(str(error))
        pass

    def execute_js_with_node(self, js_file, *args) -> json:
        process = subprocess.Popen(['node', '-e', js_file, *args], stdout = subprocess.PIPE,
            stderr = subprocess.PIPE)
        stdout, stderr = process.communicate()

        if stderr:
            raise Exception(f'Error in executing JavaScript: {stderr.decode()}')

        print(stdout.decode().strip())
        return stdout.decode().strip()

    def writeFile(self, user_profile: tenno.Tenno):
        try:
            up_file = open('user_profile_file', 'wb')
            pickle.dump(user_profile, up_file)
            up_file.close()
        except Exception as error:
            print(f"Error in writing file: {error}")

    def loadFile(self) -> tenno.Tenno:
        try:
            up_file = open('user_profile_file', 'rb')
            user_profile = pickle.load(up_file)
            up_file.close()
            return user_profile
        except AttributeError:
            return None
        except Exception as error:
            print(f"Error in loading file: {error}")

    def deleteFile(self):
        if os.path.isfile('user_profile_file'):
            os.remove('user_profile_file')
        else:
            print("User file does not exist.")

    def cleanPage(self, mainframe: Frame):
        for child in mainframe.winfo_children():
            child.destroy()