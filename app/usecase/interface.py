from abc import ABCMeta, abstractmethod
from typing import List

import app.domain.entity

class OCIGateway(metaclass=ABCMeta):
    @abstractmethod
    def get_instances(self, compartment_id:str) -> List[app.domain.entity.instance]:
        raise NotImplementedError

    @abstractmethod
    def power_on_instance(self, compute_id:str) -> app.domain.entity.instance:
        raise NotImplementedError

    @abstractmethod
    def apply_rm_stack(self, stack_id:str) -> app.domain.entity.job_response:
        raise NotImplementedError

    @abstractmethod
    def destroy_rm_stack(self, stack_id:str) -> app.domain.entity.job_response:
        raise NotImplementedError

class ScaleoutInput:
    pass

class ScaleoutOutput:
    ok: bool

    def __init__(self, ok:bool):
        self.ok = ok

class ScaleinInput:
    pass

class ScaleinOutput:
    ok: bool

    def __init__(self, ok:bool):
        self.ok = ok
