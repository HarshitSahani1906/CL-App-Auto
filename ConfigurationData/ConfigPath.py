import os

class configPath:
    absolute_path = ''

    def config_path(self):
        self.absolute_path = str(os.path.dirname(__file__))
        #print(absolute_path)
        return self.absolute_path

# apk_object =APK()
# path=apk_object.CX_apk("1.31.10")
# print("path for apk is : " +path)

