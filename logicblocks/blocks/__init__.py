from abc import ABC, abstractmethod
from typing import List, Optional

from logicblocks.connections import Header, Input, Output, Wire
from logicblocks.types import Updateable


class Block(ABC, Updateable):
	name: Optional[str]
	inputs: List[Header]
	outputs: List[Header]

	def __init__(self, name: str = None, input_count: int = 1, output_count: int = 1, gen_headers: bool = False):
		self.name = name
		self.inputs = list()
		self.outputs = list()
		if gen_headers:
			for _ in range(input_count):
				self.inputs.append(Input(self))
			for _ in range(output_count):
				self.outputs.append(Output(self))

	@property
	def input(self) -> Header:
		if len(self.inputs) != 1:
			raise ValueError("The input pseudo-property can only be used when len(inputs)==1")
		return self.inputs[0]

	@input.setter
	def input(self, i: Header) -> None:
		if len(self.inputs) != 1:
			raise ValueError("The input pseudo-property can only be used when len(inputs)==1")
		self.inputs[0] = i

	@input.deleter
	def input(self) -> None:
		if len(self.inputs) != 1:
			raise ValueError("The input pseudo-property can only be used when len(inputs)==1")
		del self.inputs[0]

	@property
	def output(self) -> Header:
		if len(self.outputs) != 1:
			raise ValueError("The output pseudo-property can only be used when len(outputs)==1")
		return self.outputs[0]

	@output.setter
	def output(self, o: Header) -> None:
		if len(self.outputs) != 1:
			raise ValueError("The output pseudo-property can only be used when len(outputs)==1")
		self.outputs[0] = o

	@output.deleter
	def output(self) -> None:
		if len(self.outputs) != 1:
			raise ValueError("The output pseudo-property can only be used when len(outputs)==1")
		del self.outputs[0]

	@abstractmethod
	def update(self) -> None:
		pass


class SimpleBlock(Block, ABC):
	def __init__(self, name: str = None, input_count: int = 1, output_count: int = 1):
		super().__init__(name, input_count, output_count, True)


class CompoundBlock(Block, ABC):
	internal_wires: List[Wire]

	def __init__(self, name: str = None, input_count: int = 1, output_count: int = 1):
		super().__init__(name, input_count, output_count)
		self.internal_wires = list()

	def update(self) -> None:
		pass
