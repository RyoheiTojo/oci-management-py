import usecase.interface

class DefaultInteractor:
    oci_gateway:       usecase.interface.OCIGateway
    scaleout_stack_id: str

    def __init__(self, oci_gateway:usecase.interface.OCIGateway, scaleout_stack_id:str):
        self.oci_gateway       = oci_gateway
        self.scaleout_stack_id = scaleout_stack_id

    def scaleout(self) -> usecase.interface.ScaleoutOutput:
        response = self.oci_gateway.apply_rm_stack(stack_id = self.scaleout_stack_id)
        return usecase.interface.ScaleoutOutput(ok = (response.lifecycle_state == "SUCCEEDED"))
