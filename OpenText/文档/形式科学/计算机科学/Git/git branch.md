##### git branch
- `git branch`
	- 简介
		-  列出, 创建或删除分支
	- 选项
		- `--all` / `-a` 
			- 列出所有分支, 包括本地和远程分支
		- `-vv`
			- 列出所有分支及其对应上游分支
		- `--delete <branchname>` / `-d <branchname>` 
			- 删除指定的本地分支, 只能删除已经被合并的分支
		- `-m <old-branch> <new-branch>` 
			- 重命名分支
		- `--set-upstream-to=<upstream>` / `-u <upstream>`
			- 设置上游分支, 仓库名/分支名
		- `<branchname>`
			- 创建指定分支
	- 示例
```shell
git branch
# 列出所有本地分支

git branch -a
# 列出所有分支

git branch -vv
# 列出所有分支

git branch test
# 创建分支test

git branch -u origin/main
# 设置上游分支
```
