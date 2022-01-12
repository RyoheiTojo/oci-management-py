import datetime

class instance:
  id:                  str
  availability_domain: str
  compartment_id:      str 
  display_name:        str
  fault_domain:        str
  shape:               str

  def __init__(self, id:str, availability_domain:str, compartment_id:str, display_name:str, fault_domain:str, shape:str):
    self.id                  = id
    self.availability_domain = availability_domain
    self.compartment_id      = compartment_id
    self.display_name        = display_name
    self.fault_domain        = fault_domain
    self.shape               = shape

class job_response:
  id:              str
  stack_id:        str
  lifecycle_state: str
  operation:       str
  error_message:   str
  time_created:    datetime.datetime
  time_finished:   datetime.datetime

  def __init__(self, id:str, stack_id:str, lifecycle_state:str, operation:str, error_message:str, time_created:datetime.datetime, time_finished:datetime.datetime):
    self.id              = id
    self.stack_id        = stack_id
    self.lifecycle_state = lifecycle_state
    self.operation       = operation
    self.error_message   = error_message
    self.time_created    = time_created
    self.time_finished   = time_finished

