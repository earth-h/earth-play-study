# 트리 순회 알고리즘

## 전위 순회(pre-order traversal)

전위 순회는 `뿌리 노드 → 왼쪽 서브 트리 → 오른쪽 서브 트리` 순으로 순회합니다.

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/dd71d086-9f7a-4bdb-882c-34fc9ec2d670/.gif](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/dd71d086-9f7a-4bdb-882c-34fc9ec2d670/.gif)

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

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1a929983-31f4-4f38-9f82-065974e3a2c5/_(1).gif](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1a929983-31f4-4f38-9f82-065974e3a2c5/_(1).gif)

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

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1008d308-d1f0-44ac-b11e-b7cd9298d921/_(2).gif](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1008d308-d1f0-44ac-b11e-b7cd9298d921/_(2).gif)

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

[https://austingwalters.com/binary-trees-traversals-everyday-algorithms/](https://austingwalters.com/binary-trees-traversals-everyday-algorithms/)