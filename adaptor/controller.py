import usecase.interactor

class CliController:
    usecase: usecase.interactor.DefaultInteractor

    def __init__(self, usecase:usecase.interactor.DefaultInteractor):
        self.usecase = usecase

    def scaleout(self):
        res = self.usecase.scaleout()
        print(vars(res))
