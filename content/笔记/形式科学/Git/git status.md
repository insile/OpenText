##### git status
- `git status`
	- 简介
		- 返回文件版本状态, 可以帮助了解项目当前的状态, 有三种: 暂存区和当前 `HEAD` 提交之间存在差异的文件, 暂存区和工作树之间存在差异的文件, 工作树中未被 Git 跟踪的文件. 输出一段格式化的信息 
	- 示例
```shell
git status

# On branch master
# 分支
# No commits yet
# 未提交
# Untracked files:
#   (use "git add <file>..." to include in what will be committed)
#         t.txt
# 未跟踪文件是 t.txt
# nothing added to commit but untracked files present (use "git add" to track)
# 需要添加暂存
```
