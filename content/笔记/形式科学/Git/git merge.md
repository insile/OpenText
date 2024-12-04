##### git merge
- `git merge`
	- 简介
		- 将另外一个分支的更改合并到当前分支, 它将两个分支的历史记录结合在一起, 并生成一个新的合并提交, 可能会产生[[Git.分支|合并冲突]]
	- 选项
		- `<branch>`
			- 合并分支
	- 示例
```shell
git merge feature-branch
# 合并另一个分支到当前分支

git merge origin/feature-branch
# 合并另一个远程分支到当前分支
```

