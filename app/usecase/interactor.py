import app.usecase.interface
import app.utility.logger

class DefaultInteractor:
    oci_gateway:       app.usecase.interface.OCIGateway
    scaleout_stack_id: str
    logger:  app.utility.logger.LoggingLogger

    def __init__(self, oci_gateway:app.usecase.interface.OCIGateway, scaleout_stack_id:str, logger:app.utility.logger.LoggingLogger):
        self.oci_gateway       = oci_gateway
        self.scaleout_stack_id = scaleout_stack_id
        self.logger            = logger

    def scaleout(self) -> app.usecase.interface.ScaleoutOutput:
        response = self.oci_gateway.apply_rm_stack(stack_id = self.scaleout_stack_id)
        return app.usecase.interface.ScaleoutOutput(ok = (response.lifecycle_state == "SUCCEEDED"))

    def scalein(self) -> app.usecase.interface.ScaleoutOutput:
        response = self.oci_gateway.destroy_rm_stack(stack_id = self.scaleout_stack_id)
        return app.usecase.interface.ScaleinOutput(ok = (response.lifecycle_state == "SUCCEEDED"))

    def test(self):
        self.logger.error('hoge')
