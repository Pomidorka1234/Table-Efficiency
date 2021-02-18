import math
from typing import Iterable, TypeVar

def G(y: int, x: int, n: int) -> int:
    """[y, x of the slope's integer part multiplication by a value]

    Args:
        y (int): [the y value of the slope]
        x (int): [the x value of the slope]
        n (int): [the multiplicator]

    Returns:
        int: [Multiplied slope's integer part]
    """
    return math.floor(y / x) * n

_Trn = TypeVar('Tr', object)

class NaryTree(object):
    def __init__(self, node: dict(Iterable[_Trn]), value: object) -> None:
        self.node = node
        self.value = value

    def hasNode(self):
        for value in self.node:
            if value == NameError:
                return False
        return True

    def appendNode(self, node: tuple(Iterable[_Trn]), n: int) -> None:
        self.node.insert(n, node)

    def replaceChild(self, n: int, m: int) -> None:
        temp = self.node[n]
        self.node[n] = self.node[m]
        self.node[m] = temp

    def replaceChildValue(self, n: int, m: int) -> None:
        temp = self.node[n].value
        self.node[n].value = self.node[m].value
        self.node[m].value = temp

    def replaceChildParent(self, n: int) -> None:
        temp = self.node[n].value
        self.node[n].value = self.value
        self.value = temp

class BinaryTree(object):
    def __init__(self, left: NaryTree, right: NaryTree, value: object) -> None:
        self.left = left
        self.right = right
        self.value = value

    def hasNode(self):
        return self.left != NameError or self.right != NameError

    def appendNode(self, node: NaryTree, n: int) -> None:
        self.node.insert(n, node)

    def replaceChild(self) -> None:
        temp = self.left
        self.left = self.right
        self.right = temp

    def replaceChildValue(self) -> None:
        temp = self.left.value
        self.left.value = self.right.value
        self.right.value = temp

    def replaceChildParent(self, node: NaryTree) -> None:
        temp = node.value
        node.value = self.value
        self.value = temp
