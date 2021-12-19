import oci
import domain.entity

from typing import List

class OCIInteractor:
  compartment_id: str
  signer: oci.signer.Signer

  def __init__(self, compartment_id:str):
    self.compartment_id = compartment_id
    self.signer = oci.auth.signers.InstancePrincipalsSecurityTokenSigner()

  def get_instances(self) -> List[domain.entity.instance]:
    compute_client = oci.core.ComputeClient(config={}, signer=self.signer)
    response = compute_client.list_instances(self.compartment_id)

    instances = [domain.entity.instance(
        id                  = instance.id,
        availability_domain = instance.availability_domain,
        compartment_id      = instance.compartment_id,
        display_name        = instance.display_name,
        fault_domain        = instance.fault_domain,
        shape               = instance.shape,
      ) for instance in response.data]

    return instances
