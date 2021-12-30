import sys

from adaptor.controller import CliController
from adaptor.gateway import PythonOCIGateway
from usecase.interactor import DefaultInteractor

from configparser import ConfigParser
from os import path

if __name__ == '__main__':
    config = ConfigParser()
    config.read('./config.ini', encoding='utf-8')

    if len(sys.argv) < 2:
        print("Usage: python3 app.py <subcommand> [option]")
        sys.exit(1)
    
    controller = CliController(
        usecase = DefaultInteractor(
            oci_gateway       = PythonOCIGateway(),
            scaleout_stack_id = config['Scaleout']['stack_id']
            )
        )

    subcommand = sys.argv[1]

    if subcommand == "scaleout":
        controller.scaleout()
    elif subcommand == "scalein":
        controller.scalein()
    else:
        print("Unknown subcommand.")
        sys.exit(1)
