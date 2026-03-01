##### 使用 Git 协作
- 使用 Git 协作
	- 欢迎各位朋友使用 [[Git]] 协作, 您可以对任何内容进行增删改, 从一个标点符号, 到一个知识点, 乃至整体框架, 只要新内容是结构化的契合整体并且有充足理由. 这比代码协作容易多了, 毕竟不需要保证运行正确
		- 分叉存储库
			- 在[仓库](https://github.com/insile/my-notes)点击 `Fork` 分叉仓库
				- ![[屏幕截图1.png|400]]
			- 创建新的分叉
				- ![[屏幕截图2.png|400]]
			- 完成创建, `Contribute` 表示为上游贡献内容. `Sync fork` 表示与上游同步内容, 可从 `Code` 复制 Git URL: `https://github.com/roomplayer/my-notes.git`
				- ![[屏幕截图3.png|400]]
		- 对分叉进行更改
			- 克隆分叉仓库
				- `git clone https://github.com/roomplayer/my-notes.git`
			- 更改文档内容
				- 使用 Obsidian 打开仓库 `content` 目录编辑
			- 推送前与上游同步
				- `git remote add upstream https://github.com/insile/my-notes`
				- `git pull upstream v4`
			- 推送分叉仓库
				- `git add .`
				- `git commit -m "commit"`
				- `git push origin v4`
		- 发起拉取请求
			- 在分叉仓库点击 `Contribute` 发起拉取请求
				- ![[屏幕截图4.png|400]]
				- ![[屏幕截图5.png|400]]
			- 合并后保持同步
				- `git pull upstream v4`




