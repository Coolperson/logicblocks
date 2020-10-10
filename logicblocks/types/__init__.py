from typing import Protocol


class Updateable(Protocol):
	def update(self) -> None:
		pass
