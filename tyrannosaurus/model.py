from __future__ import annotations
import re
import abc
from dataclasses import dataclass
import enum
from functools import total_ordering
from typing import Optional, Sequence, Set, Union, Tuple as Tup

class ServiceName(str):
	"""
	Services that contain dependency lists.
	"""

class PackageName(str):
	pass

class Error(Exception): pass

class ComparisonError(Error):
	pass

class ComparisonTypeError(ComparisonError):
	def __init__(self, this, other):
		super().__init__("{} has type {}; expected {}".format(other, type(other), type(this)))
		self.this, self.other = this, other

class VersionSyntaxError(Error):
	def __init__(self, text: str):
		super().__init__("Version specifier {} is invalid".format(text))
		self.text = text

class SuffixList:
	components: Sequence[Union[str, int]]
	@property
	def text(self) -> str:
		return ".".join([str(s) for s in self.components])
	def __repr__(self):
		return self.text
	def __str__(self):
		return self.text
	def __lt__(self, other):
		if not isinstance(other, SuffixList):
			raise ComparisonTypeError(self, other)
		if [type(i) for i in self.components] != [type(i) for i in other.components]:
			raise ComparisonError("Components do not match between {} and {}".format(self, other))
		return self.components < other.components

@total_ordering
@dataclass
class SemanticVersion:
	major: int
	minor: int
	patch: int
	suffix_list: SuffixList
	@property
	def text(self):
		return "{}.{}.{}-{}".format(self.major, self.minor, self.patch, self.suffix_list.text)
	def __repr__(self):
		return self.text
	def __str__(self):
		return self.text
	def __lt__(self, other):
		if not isinstance(other, SemanticVersion):
			raise TypeError("{} has type {}".format(other, type(other)))
		return (self.major, self.minor, self.patch, self.suffix_list) < (other.major, other.minor, other.patch, other.suffix_list)


class Operator(enum.Enum):
	lt = '<'
	le = '<='
	gt = '>'
	ge = '>='
	eq = '=='
	neq = '!='


class VersionRange:
	def __init__(self, operations: Sequence[Tup[Operator, SemanticVersion, SemanticVersion]]):
		self.operations = operations


@total_ordering
@dataclass
class Dependency:
	name: str
	version: str
	component: Optional[str]
	source: ServiceName


class DependencyList:
	def __init__(self, lst: Sequence[Dependency]):
		self.deps = lst

	def sorted(self) -> DependencyList:
		return DependencyList(sorted(self.deps))
