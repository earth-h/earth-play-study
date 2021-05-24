# 트리 순회 알고리즘

## 전위 순회(pre-order traversal)

전위 순회는 `뿌리 노드 → 왼쪽 서브 트리 → 오른쪽 서브 트리` 순으로 순회합니다.

![pre-order traversal](https://austingwalters.com/wp-content/uploads/2014/10/binary-tree-1-pre-order-small.gif)

### pseudo code

```python
def pre_order_traversal(self):
	def _pre_order_traversal(root):
		if root is None:
			pass
		else:
			print(root.val)
			_pre_order_traversal(root.left)
			_pre_order_traversal(root.right)
	_pre_order_traversal(self.root)
```

## 후위 순회(post-order traversal)

후위 순회는 `왼쪽 서브 트리 → 오른쪽 서브 트리 → 뿌리 노드` 순으로 순회합니다.

![post-order traversal](https://austingwalters.com/wp-content/uploads/2014/10/binary-tree-1-post-order-small.gif)

### pseudo code

```python
def post_order_traversal(self):
	def _post_order_traversal(root):
		if root is None:
			pass
		else:
			_post_order_traversal(root.left)
			_post_order_traversal(root.right)
			print(root.val)
	_post_order_traversal(self.root)
```

## 정위 순회(in-order traversal)

정위 순회는 `왼쪽 서브 트리 → 뿌리 노드 → 오른쪽 서브 트리` 순으로 순회합니다.

![in-order traversal](https://austingwalters.com/wp-content/uploads/2014/10/binary-tree-1-order-small.gif)

### pseudo code

```python
def in_order_traversal(self):
	def _in_order_traversal(root):
		if root is None:
			pass
		else:
			_in_order_traversal(root.left)
			print(root.val)
			_in_order_traversal(root.right)
	_in_order_traversal(self)
root)
```

## 출처

[출처](https://austingwalters.com/binary-trees-traversals-everyday-algorithms/)