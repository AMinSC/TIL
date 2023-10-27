from typing import Dict

permission_data = {"id": "access"}


class Authorized:
	data: dict

	def __setitem__(self, key: str, value: str):
		if not isinstance(key, str):
			raise TypeError(
					f"Invalid type for dictionary key: ",
					f"expected 'str', got '{type(key).__name__}'"
					)
		if not isinstance(value, str):
			raise TypeError(
					f"Invalid type for dictionary value: ",
					f"expected 'str', got '{type(value).__name__}'"
					)
		# super().__setitem__(key, value)
	
	def __init__(self, key, value):
			self.key = key
			self.value = value

	def __dir__(self, data: dict[str, str]):
		return data[self.key]
	
	# mypy(error)issue [https://github.com/python/mypy/issues/7778]
	def is_id_check(data: Dict[str, str]) -> str:
		if data["id"] in permission_data["id"]:
			return "authorized user"
		else:
			return "denial user"
	

print(Authorized.is_id_check({"id": "access"}))
print(Authorized.__annotations__)
print(Authorized({"id": "access"}))
