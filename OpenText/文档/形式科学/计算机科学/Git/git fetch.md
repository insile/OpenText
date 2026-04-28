##### git fetch
- `git fetch`
	- 简介
		- 从远程仓库下载所有最新的提交, 分支和标签, 但不会自动合并这些更改到当前分支, 它允许你在合并或查看更新前审查远程更改
	- 选项
		- `<repository> <branch>`
			- 指定远程仓库与分支
		- `--all`
			- 所有远程仓库
	- 示例
```shell
git fetch origin
# 获取默认远程仓库 origin 的更新

git fetch origin main
# 获取默认远程仓库 origin 分支 main 的更新
```
