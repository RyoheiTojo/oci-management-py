from usecase.oci import OCIInteractor

from configparser import ConfigParser
from os import path

if __name__ == '__main__':
  config = ConfigParser()
  config.read('./config.ini', encoding='utf-8')

  compartment_id = config['Environment']['compartment_id']
  availability_domain = config['Environment']['availability_domain']
  region = config['Environment']['region']

  stack_id = config['Scaleout']['stack_id']

  interactor = OCIInteractor()
  res = interactor.apply_rm_stack(stack_id = stack_id)
  print(vars(res))
