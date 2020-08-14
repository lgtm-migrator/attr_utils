# Demo for autodoc_typehints_attrs

# stdlib
import typing
from typing import Any, Dict, List, Tuple

# 3rd party
import attr

# this package
from attr_utils.annotations import add_init_annotations
from attr_utils.docstrings import add_attrs_doc


def my_converter(arg: List[Dict[str, Any]]):
	return arg


def untyped_converter(arg):
	return arg


@attr.s
class SomeClass:
	a_string: str = attr.ib(converter=str)
	custom_converter: Any = attr.ib(converter=my_converter)
	untyped: Tuple[str, int, float] = attr.ib(converter=untyped_converter)  # type: ignore


def test_add_attrs_doc():

	doc = "\n        Automatically created by attrs.\n        "

	assert SomeClass.__eq__.__doc__ is None
	assert SomeClass.__ge__.__doc__ == doc
	assert SomeClass.__gt__.__doc__ == doc
	assert SomeClass.__lt__.__doc__ == doc
	assert SomeClass.__le__.__doc__ == doc
	assert SomeClass.__ne__.__doc__ == "\n    Check equality and either forward a NotImplemented or return the result\n    negated.\n    "
	assert SomeClass.__repr__.__doc__ == doc

	add_attrs_doc(SomeClass)

	assert SomeClass.__eq__.__doc__ == "Return ``self == other``."
	assert SomeClass.__ge__.__doc__ == "Return ``self >= other``."
	assert SomeClass.__gt__.__doc__ == "Return ``self > other``."
	assert SomeClass.__lt__.__doc__ == "Return ``self < other``."
	assert SomeClass.__le__.__doc__ == "Return ``self <= other``."
	assert SomeClass.__ne__.__doc__ == "Return ``self != other``."
	assert SomeClass.__repr__.__doc__ == f"Return a string representation of the :class:`~.SomeClass`."
