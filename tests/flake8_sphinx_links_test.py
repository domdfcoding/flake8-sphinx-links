# stdlib
import ast

# 3rd party
import pytest

# this package
from flake8_sphinx_links import Plugin, SXL001
from flake8_sphinx_links import py_obj, py_obj_python, exc, class_


def results(s):
	return {"{}:{}: {}".format(*r) for r in Plugin(ast.parse(s)).run()}


@pytest.mark.parametrize("obj", py_obj)
def test_bad_docstring_py_obj(obj):
	test_code = f'''"""

``{obj}``

"""

class BadDocstring:
	"""``{obj}``
	"""

def bad_docstring():
	"""
	``{obj}``
	"""

class GoodDocstring:
	""":py:obj:`{obj}`
	"""

def good_docstring():
	"""
	:py:obj:`{obj}`
	"""

'''

	assert results(test_code
					) == {  # noqa: sphinx_links001
							f"3:0: {SXL001}",
							f"8:0: {SXL001}",
							f"13:1: {SXL001}",
							}


@pytest.mark.parametrize("obj", py_obj_python)
def test_bad_docstring_py_obj_python(obj):
	test_code = f'''"""

``{obj}``

"""

class BadDocstring:
	"""``{obj}``
	"""

class bad_docstring():
	"""
	``{obj}``
	"""

class GoodDocstring:
	""":py:obj:`python:{obj}`
	"""

class good_docstring():
	"""
	:py:obj:`python:{obj}`
	"""

'''

	assert results(test_code
					) == {  # noqa: sphinx_links001
							f"3:0: {SXL001}",
							f"8:0: {SXL001}",
							f"13:1: {SXL001}",
							}


@pytest.mark.parametrize("obj", exc)
def test_bad_docstring_exc(obj):
	test_code = f'''"""

``{obj}``

"""

class BadDocstring:
	"""``{obj}``
	"""

class bad_docstring():
	"""``{obj}``"""

class GoodDocstring:
	""":exc:`{obj}`
	"""

class good_docstring():
	"""
	:exc:`{obj}`
	"""

'''

	assert results(test_code
					) == {  # noqa: sphinx_links001
							f"3:0: {SXL001}",
							f"8:0: {SXL001}",
							f"12:0: {SXL001}",
							}


@pytest.mark.parametrize("obj", class_)
def test_bad_docstring_class_(obj):
	test_code = f'''"""

``{obj}``

"""

class BadDocstring:
	"""``{obj}``
	"""

class bad_docstring():
	"""
	``{obj}``
	"""

class GoodDocstring:
	""":class:`{obj}`
	"""

class good_docstring():
	""":class:`{obj}`"""

'''

	assert results(test_code
					) == {  # noqa: sphinx_links001
							f"3:0: {SXL001}",
							f"8:0: {SXL001}",
							f"13:1: {SXL001}",
							}
