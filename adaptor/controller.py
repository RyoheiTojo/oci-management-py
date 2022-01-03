import usecase.interactor
import utility.logger

class CliController:
    usecase: usecase.interactor.DefaultInteractor
    logger:  utility.logger.LoggingLogger

    def __init__(self, usecase:usecase.interactor.DefaultInteractor, logger:utility.logger.LoggingLogger):
        self.usecase = usecase
        self.logger  = logger

    def scaleout(self):
        res = self.usecase.scaleout()
        print(vars(res))

    def scalein(self):
        res = self.usecase.scalein()
        print(vars(res))

    def boot(self):
        res = self.usecase.boot()
        print(vars(res))

    def test(self):
        self.logger.debug('hogehoge')
