from configparser import ConfigParser
from ConfigurationData.ConfigPath import configPath

# config = ConfigParser()
# configFile=configPath()
# filePath=configFile.config_path()+"/config.ini"
# print(filePath)
# config.read(filePath)
# print(config.get("LogoPage-Locator", "Xpath_continueButton"))


def readConfig(section, key):
    config = ConfigParser()
    configFile=configPath()
    filePath=configFile.config_path()+"/config.ini"
    # print(filePath)
    config.read(filePath, encoding='utf8')
    # print(config.get("LogoPage-Locator", "Xpath_continueButton"))
    return config.get(section, key)


