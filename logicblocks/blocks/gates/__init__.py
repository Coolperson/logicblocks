from logicblocks.blocks import SimpleBlock, CompoundBlock
from logicblocks.connections import Wire


class NotGate(SimpleBlock):
	def __init__(self, name: str = None):
		super().__init__(name)
		self.update()

	def update(self) -> None:
		self.output.value = not self.input.value


InverterGate = NotGate


class AndGate(SimpleBlock):
	def __init__(self, name: str = None, input_count: int = 2):
		super().__init__(name, input_count)

	def update(self) -> None:
		tmp = True
		for i in self.inputs:
			tmp &= i.value
		self.output.value = tmp


class OrGate(SimpleBlock):
	def __init__(self, name: str = None, input_count: int = 2):
		super().__init__(name, input_count)

	def update(self) -> None:
		tmp = False
		for i in self.inputs:
			tmp |= i.value
		self.output.value = tmp


class NandGate(CompoundBlock):
	def __init__(self, name: str = None, input_count: int = 2):
		super().__init__(name, input_count)
		g_and = AndGate(input_count=input_count)
		g_not = NotGate()
		self.inputs.extend(g_and.inputs)
		self.internal_wires.append(Wire(g_and.output, g_not.input))
		self.output = g_not.output


class NorGate(CompoundBlock):
	def __init__(self, name: str = None, input_count: int = 2):
		super().__init__(name, input_count)
		g_or = OrGate(input_count=input_count)
		g_not = NotGate()
		self.inputs.extend(g_or.inputs)
		self.internal_wires.append(Wire(g_or.output, g_not.input))
		self.output = g_not.output
