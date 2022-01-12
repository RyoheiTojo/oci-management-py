import app.usecase.interactor
import app.utility.logger

class CliController:
    usecase: app.usecase.interactor.DefaultInteractor
    logger:  app.utility.logger.LoggingLogger

    def __init__(self, usecase:app.usecase.interactor.DefaultInteractor, logger:app.utility.logger.LoggingLogger):
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
        self.usecase.test()
        self.logger.debug('hogehoge')
