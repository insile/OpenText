##### git clone
- `git clone`
	- 简介
		- 将仓库克隆到新目录中, 为克隆仓库中的每个分支创建远程跟踪分支, 并创建初始分支
	- 选项
		- `<repository>`
			- 克隆仓库地址
		- `<directory>`
			- 新目录地址, 默认为当前目录
		- `--branch <name>` / `-b <name>`
			- 检出分支, 将新创建的 `HEAD` 指向 `<name>` 分支, 而不是克隆仓库原来所指向的
		- `--single-branch` 
			- 只克隆指定的分支, 而不是整个仓库的所有分支
	- 示例
```shell
git clone https://github.com/insile/my-notes.git
# 克隆本文档仓库
```


