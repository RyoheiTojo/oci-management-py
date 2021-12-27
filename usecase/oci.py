import oci
import domain.entity

from typing import List

class OCIInteractor:
  signer: oci.signer.Signer

  def __init__(self):
    self.signer = oci.auth.signers.InstancePrincipalsSecurityTokenSigner()

  def get_instances(self, compartment_id:str) -> List[domain.entity.instance]:
    compute_client = oci.core.ComputeClient(config={}, signer=self.signer)
    response = compute_client.list_instances(compartment_id)

    instances = [domain.entity.instance(
        id                  = instance.id,
        availability_domain = instance.availability_domain,
        compartment_id      = instance.compartment_id,
        display_name        = instance.display_name,
        fault_domain        = instance.fault_domain,
        shape               = instance.shape,
      ) for instance in response.data]

    return instances

  def power_on_instance(self, compute_id:str) -> domain.entity.instance:
    compute_client = oci.core.ComputeClient(config={}, signer=self.signer)
    response = compute_client.instance_action(instance_id=compute_id, action="START")

    return domain.entity.instance(
        id                  = response.data.id,
        availability_domain = response.data.availability_domain,
        compartment_id      = response.data.compartment_id,
        display_name        = response.data.display_name,
        fault_domain        = response.data.fault_domain,
        shape               = response.data.shape,
      )

  def duplicate_instance(self, compartment_id:str, availability_domain:str, instance_id:str, region:str) -> List[domain.entity.instance]:
    compute_client = oci.core.ComputeClient(config={}, signer=self.signer)
    bootvolume_attachments_response = compute_client.list_boot_volume_attachments(availability_domain=availability_domain, compartment_id=compartment_id, instance_id=instance_id)

    bootvolume_id = bootvolume_attachments_response.data[0].boot_volume_id

    blockstorage_client = oci.core.BlockstorageClient(config={}, signer=self.signer)
    blockstorage_client.create_boot_volume_backup(create_boot_volume_backup_details=oci.core.models.CreateBootVolumeBackupDetails(boot_volume_id=bootvolume_id, type="FULL"))
    return bootvolume_id
    
