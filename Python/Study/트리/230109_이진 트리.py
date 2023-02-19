# https://m.blog.naver.com/leeinje66/221622228795

class Node:
    def __init__(self, value):
        self.data = value
        self.left, self.right = None, None

    # 현재 노드 기준 트리의 크기
    def size(self):
        l = self.left.size() if self.left else 0
        r = self.right.size() if self.right else 0
        return l + r + 1

    # 현재 노드 기준 트리의 깊이
    def depth(self):
        l = self.left.depth() if self.left else 0
        r = self.right.depth() if self.right else 0
        return max(l, r) + 1

    # 현재 노드 기준 중위 순회
    def inorder(self):
        tr = []
        if self.left: tr += self.left.inorder()
        tr.append(self.data)
        if self.right: tr += self.right.inorder()
        return tr

    # 현재 노드 기준 전위 순회
    def preorder(self):
        tr = []
        tr.append(self.data)
        if self.left: tr += self.left.preorder()
        if self.right: tr += self.right.preorder()
        return tr

    # 현재 노드 기준 중위 순회
    def postorder(self):
        tr = []
        if self.left: tr += self.left.postorder()
        if self.right: tr += self.right.postorder()
        tr.append(self.data)
        return tr


class BinaryTree:
    def __init__(self, r):
        self.root = r

    # 트리의 크기
    def size(self):
        return self.root.size() if self.root else 0

    # 트리의 깊이
    def depth(self):
        return self.root.deepth() if self.root else 0

    # 중위 순회
    def inorder(self):
        return self.root.inorder() if self.root else 0

    # 전위 순회
    def preorder(self):
        return self.root.preorder() if self.root else 0

    # 중위 순회
    def postorder(self):
        return self.root.postorder() if self.root else 0
