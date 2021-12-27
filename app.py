from usecase.oci import OCIInteractor

from configparser import ConfigParser
from os import path

if __name__ == '__main__':
  config = ConfigParser()
  config.read('./config.ini', encoding='utf-8')

  compartment_id = config['Environment']['compartment_id']
  availability_domain = config['Environment']['availability_domain']
  region = config['Environment']['region']

  instance_id = config['Scaleout']['instance_id']

  interactor = OCIInteractor()
  res = interactor.duplicate_instance(compartment_id=compartment_id, availability_domain=availability_domain, instance_id=instance_id, region=region)
  print(res)
