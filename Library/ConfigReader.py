import configparser


def readConfigData(section, key):
    config = configparser.ConfigParser()
    config.read('./ConfigrationFile/Config.cfg')
    return config.get(section, key)

def readElements(section, key):
    config = configparser.ConfigParser()
    config.read('./ConfigrationFile/Elements.cfg')
    return config.get(section,key)

