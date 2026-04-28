##### git pull
- `git pull`
	- 简介
		- 从远程仓库获取最新的更改并将这些更改合并到当前分支, 实际上是 [[git fetch]] 和 [[git merge]] 的组合
	- 选项
		- `<repository> <branch>`
			- 指定远程仓库与分支
	- 示例
```shell
git pull
# 从默认远程仓库 (通常是 origin) 拉取合并所有对应分支

git pull origin main
# 从远程仓库 origin 拉取合并分支 main 到当前分支
```
