from abc import ABC, abstractmethod
from pydantic import BaseModel
from typing import Union, Type

class BaseEvent(ABC):
    @abstractmethod
    async def handle(self, param: Union[Type[BaseModel], None] = None) -> None:
        ...