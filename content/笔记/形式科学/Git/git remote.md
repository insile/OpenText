##### git remote
- `git remote`
	- 简介
		- 管理跟踪其分支的一组远程仓库, 涉及到推送拉取的要记得管理远程仓库
	- 子命令
		- `git remote add <name> <URL>` 
			- 添加新的远程仓库
		- `git remote rename <old> <new>`
			- 重命名远程仓库
		- `git remote remove <name>`
			- 删除远程仓库
		- `git remote set-url <name> <newurl>`
			- 修改远程仓库名字与 URL
	- 选项
		- `--verbose` / `-v`
			- 显示远程仓库名称与 URL
	- 示例
```shell
git remote -v
# 查看所有远程仓库及其 URL

git remote add origin https://github.com/user/repo.git
# 添加一个新的原始远程仓库, 名为origin

git remote add upstream https://github.com/user/repo.git
# 添加一个新的分叉远程仓库, 名为upstream
```



