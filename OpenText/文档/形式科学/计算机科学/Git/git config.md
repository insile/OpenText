##### git config
- `git config`
	- 简介
		- 查询, 设置, 替换, 取消 Git 配置选项, 选项都是键值对, 很对命令默认的参数来自于此
	- 子命令
		- `git config list` 列出配置文件中设置的所有选项及其值
		- `git config get` 查询指定选项的值
		- `git config set` 设置指定选项的值
		- `git config unset` 取消指定选项的值
		- `git config rename-section` 指定选项重命名
		- `git config remove-section` 删除指定选项
		- `git config edit` 打开编辑器来修改指定的配置文件
	- 选项
		- `--global` 
			- 仅从全局读取或写入全局, 默认从系统, 全局和当前仓库配置文件中读取, 写入当前仓库配置文件
		- `--local` 
			- 仅从当前读取或写入当前, 默认从系统, 全局和当前仓库配置文件中读取, 写入当前仓库配置文件
	- 示例
```shell
git config list
# 列出所有选项及其值

git config get --global user.name
# 查询全局用户名

git config get --local user.name
# 查询当前仓库用户名

git config set user.name newname
# 设置当前仓库用户名
```
