import sys

from app.utility.logger import setLogger, getLogger
from app.utility.logger import LogLevel

from app.adaptor.controller import CliController
from app.adaptor.gateway import PythonOCIGateway
from app.usecase.interactor import DefaultInteractor

from configparser import ConfigParser
from os import path

if __name__ == '__main__':
    config = ConfigParser()
    config.read('./config.ini', encoding='utf-8')

    if len(sys.argv) < 2:
        print("Usage: python3 app.py <subcommand> [option]")
        sys.exit(1)

    setLogger(name = 'app', level = LogLevel.of_string(level = config['Environment']['log_level']), path = config['Environment']['log_path'])
    
    controller = CliController(
        usecase = DefaultInteractor(
            oci_gateway       = PythonOCIGateway(),
            scaleout_stack_id = config['Scaleout']['stack_id'],
            logger            = getLogger('app.usecase.interactor')
            ),
        logger  = getLogger('app.adaptor.controller')
        )

    subcommand = sys.argv[1]

    if subcommand == "scaleout":
        controller.scaleout()
    elif subcommand == "scalein":
        controller.scalein()
    elif subcommand == "boot":
        controller.boot()
    elif subcommand == "test":
        controller.test()
    else:
        print("Unknown subcommand.")
        sys.exit(1)
