##### git push
- `git push`
	- 将本地仓库中的提交推送到远程仓库, 通常会将当前分支的所有新提交推送到对应的远程分支, 
- 选项
	- `<repository> <branch>`
		- 指定远程仓库与分支
	- `-u`
		- 指定远程仓库一个新分支
- 示例
```shell
git push origin main
# 推送当前 main 分支到远程仓库 origin 分支 main 

git push -u origin feature-branch
# 推送当前 main 分支到远程仓库 origin 新分支 feature-branch

git push origin main:feature-branch
# 推送当前 main 分支到远程仓库 origin 分支 feature-branch 
```
