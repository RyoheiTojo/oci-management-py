import oci
import domain.entity

from typing import List

class PythonOCIGateway:
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

    def apply_rm_stack(self, stack_id:str) -> domain.entity.job_response:
        rm_client = oci.resource_manager.ResourceManagerClient(config={}, signer=self.signer)
        composite_operations = oci.resource_manager.ResourceManagerClientCompositeOperations(client = rm_client)

        plan_response = composite_operations.create_job_and_wait_for_state(
            wait_for_states    = ["SUCCEEDED", "FAILED", "UNKNOWN_ENUM_VALUE"],
            create_job_details = oci.resource_manager.models.CreateJobDetails(
                stack_id              = stack_id,
                job_operation_details = oci.resource_manager.models.CreatePlanJobOperationDetails(),
            )
        )
        if plan_response.data.lifecycle_state != "SUCCEEDED":
            return domain.entity.job_response(
                id              = plan_response.data.id,
                stack_id        = plan_response.data.stack_id,
                lifecycle_state = plan_response.data.lifecycle_state,
                error_message   = "" if plan_response.data.failure_details == None else plan_response.data.failure_details.message,
                operation       = plan_response.data.operation,
                time_created    = plan_response.data.time_created,
                time_finished   = plan_response.data.time_finished,
            )

        apply_response = composite_operations.create_job_and_wait_for_state(
            wait_for_states    = ["SUCCEEDED", "FAILED", "UNKNOWN_ENUM_VALUE"],
            create_job_details = oci.resource_manager.models.CreateJobDetails(
                stack_id              = stack_id,
                job_operation_details = oci.resource_manager.models.CreateApplyJobOperationDetails(execution_plan_job_id = plan_response.data.id),
            )
        )
        return domain.entity.job_response(
            id              = apply_response.data.id,
            stack_id        = apply_response.data.stack_id,
            lifecycle_state = apply_response.data.lifecycle_state,
            error_message   = "" if apply_response.data.failure_details == None else apply_response.data.failure_details.message,
            operation       = apply_response.data.operation,
            time_created    = apply_response.data.time_created,
            time_finished   = apply_response.data.time_finished,
        )
