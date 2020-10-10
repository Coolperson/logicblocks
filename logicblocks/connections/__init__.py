from abc import ABC, abstractmethod
from typing import Any, List, Optional

from logicblocks.types import Updateable


class Header(ABC):
	_value: bool
	_parent: Updateable
	wires: Optional[List["Wire"]]

	def __init__(self, parent: Updateable):
		self._parent = parent
		self._value = False
		self.wires = list()

	@property
	def value(self) -> bool:
		return self._value

	@value.setter
	@abstractmethod
	def value(self, v) -> None:
		pass


class Input(Header):
	@Header.value.setter
	def value(self, v: Any) -> None:
		prev = self._value
		self._value = bool(v)
		if prev != self._value:
			self._parent.update()


class Output(Header):
	@Header.value.setter
	def value(self, v: Any) -> None:
		prev = self._value
		self._value = bool(v)
		if prev != self._value:
			for w in self.wires:
				w.push()


class Wire:
	source: Header
	dest: Header

	def __init__(self, source: Header, dest: Header):
		self.source = source
		source.wires.append(self)
		self.dest = dest

	def push(self) -> None:
		self.dest.value = self.source.value
