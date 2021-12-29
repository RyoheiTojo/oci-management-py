from abc import ABCMeta, abstractmethod
from typing import List

import domain.entity

class OCIGateway(metaclass=ABCMeta):
    @abstractmethod
    def get_instances(self, compartment_id:str) -> List[domain.entity.instance]:
        raise NotImplementedError

    @abstractmethod
    def power_on_instance(self, compute_id:str) -> domain.entity.instance:
        raise NotImplementedError

    @abstractmethod
    def apply_rm_stack(self, stack_id:str) -> domain.entity.job_response:
        raise NotImplementedError

class ScaleoutInput:
    pass

class ScaleoutOutput:
    ok: bool

