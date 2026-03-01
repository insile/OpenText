##### git revert
- `git revert`
	- 简介
		- 用一次新的提交回退到某个特定的提交, 从而保持提交历史的完整性
	- 选项
		- `<commit>`
			- 回退到指定提交
	- 示例
```shell
git revert HEAD
# 还原最近一次提交

git revert abc1234
# 还原指定的提交 (用提交哈希标识)
```
