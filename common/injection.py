from typing import Callable, Type, TypeVar
from injector import Injector, singleton

injector = Injector()
T = TypeVar('T')

def on(dependency_class: Type[T]) -> Callable[[], T]:
  """Bridge between FastAPI injection and 'injector' DI framework."""
  return lambda: injector.get(dependency_class)
