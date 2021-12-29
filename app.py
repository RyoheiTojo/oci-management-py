from adaptor.gateway import PythonOCIGateway
from usecase.interactor import DefaultInteractor

from configparser import ConfigParser
from os import path

if __name__ == '__main__':
    config = ConfigParser()
    config.read('./config.ini', encoding='utf-8')

    
    interactor = DefaultInteractor(
        oci_gateway       = PythonOCIGateway(),
        scaleout_stack_id = config['Scaleout']['stack_id']
        )

    res = interactor.scaleout()
    print(vars(res))
