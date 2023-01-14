from configparser import ConfigParser
from typing import Dict


def getConfigParameters(section, filename="config.ini", debug=False) -> Dict:
    # Create config data dictionary
    configParameter = {}

    # Parse desired configuration data from config.ini config file
    # Declare a new parser
    parser = ConfigParser()

    # Check if we are currently in debug mode, if so, read from the localized config file
    if debug:
        filename = filename.split(".")[0] + "-dev." + filename.split(".")[-1]  # This build a filename-dev.ini name from the filename

    # Read config file
    parser.read(filename)

    # Get section and extract parameters
    if parser.has_section(section):
        parametersList = parser.items(section)
        for param in parametersList:
            configParameter[param[0]] = param[1]
    else:
        raise Exception("Section {0} not found in the {1} file".format(section, filename))

    return configParameter