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
