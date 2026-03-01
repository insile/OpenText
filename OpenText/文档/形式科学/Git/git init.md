##### git init
- `git init`
	- 简介
		- 初始化空仓库或者重新初始化现存仓库. 它在目录新建一个 `.git` 目录, 然后创建一个没有任何提交的初始主分支 `master`
	- 选项
		-  `<directory>` 
			- 指定初始化目录, 默认为当前目录
		- `--initial-branch=<branch-name>` / `-b <branch-name>`
			- 指定初始分支名字
		- `--bare` 
			- 创建一个裸仓库
	- 示例
```shell
git init --initial-branch=main
# 初始化当前目录空仓库, 分支名为main

git init F:\test
# 初始化指定目录空仓库
```
