##### 使用 Quartz 4.0 和 GitHub Pages 发布托管 Obsidian 笔记
- **步骤 0. 先决条件**
	- 在继续之前, 您需要安装以下软件
		- NodeJS (v20.16+) : https://nodejs.org/zh-cn 
		- [[Git]]: https://git-scm.com/
		- Obsidian: https://obsidian.md/ 
- **步骤 1. 下载并安装 Quartz**
	- 打开终端并运行以下命令
		- `git clone https://github.com/jackyzha0/quartz.git`
			- [[git clone|克隆]] Quartz 仓库, 并将其存储在当前文件夹的 quartz 中
		- `cd quartz`
			- 进入 quartz 目录
		- `npm i`
			- 安装 Quartz 依赖项
		- `npx quartz create`
			- 创建一个新的 Quartz 项目
	- 选择初始化选项, 默认即可
		- 初始化目录中的内容
			- `Empty Quartz`
			- `Copy an existing folder`
			- `Symlink an existing folder`
		- Obsidian 路径设置
			- `Treat links as absolute path`
			- `Treat links as shortest path`
			- `Treat links as relative paths`
		- 设置完成
			- `You're all set! Not sure what to try next? Try:`
			- `Customizing Quartz a bit more by editing 'quartz.config.ts'`
			- `Running 'npx quartz build --serve' to preview your Quartz locally`
			- `Hosting your Quartz online (see: https://quartz.jzhao.xyz/hosting)`
- **步骤 2. 设置 GitHub 存储库** 
	- 在 GitHub 上[新建仓库](https://github.com/new), 不要使用 README , 许可证或 gitignore 文件初始化新仓库
	- 在 GitHub 的 “快速设置” 页面上存储库的顶部, 单击剪贴板以复制远程仓库 URL: `https://github.com/<user>/<repository>.git`
	- 继续在 Quartz 目录终端并运行命令
		- `git remote -v`
			- [[git remote|管理]]被跟踪的远程仓库
			- `origin  https://github.com/jackyzha0/quartz.git (fetch)`
			- `origin  https://github.com/jackyzha0/quartz.git (push)`
			- `upstream        https://github.com/jackyzha0/quartz.git (fetch)`
			- `upstream        https://github.com/jackyzha0/quartz.git (push)`
		- `git remote set-url origin <URL>`
			- [[git remote|修改]] origin 远程仓库并替换为自己复制的 URL
		- `npx quartz sync --no-pull`
			- 将对本地仓库所做的更改推送到远程仓库上的
			- 末尾带有绿色 Done! 
- **步骤 3. 创建 Obsidian 库**
	- 在 Obsidian 中将 quartz 目录里的 `content` 文件夹作为 Obsidian 库打开，然后就可以按照以往习惯写文档, `index.md` 是网站首页不要删除
	- 每次更改后记得更新推送到远程仓库上
		- `npx quartz sync`
- **步骤 4. 设置 GitHub Actions 自动部署 GitHub Pages**
	- 在本地 Quartz 中, 按以下路径创建一个新文件, 并且保存以下内容 
		- `quartz/.github/workflows/deploy.yml`
	- 前往 GitHub 仓库，点击 Settings>Pages>Source 下拉菜单，选择 GitHub Actions
	- 最后提交更改，网站将部署到 `<github-username>.github.io/<repository-name>`，Pages 页面将会有以下提示 `Your site is live at https://insile.github.io/my-notes/`
		- `npx quartz sync`
```yaml
name: Deploy Quartz site to GitHub Pages
 
on:
  push:
    branches:
      - v4
 
permissions:
  contents: read
  pages: write
  id-token: write
 
concurrency:
  group: "pages"
  cancel-in-progress: false
 
jobs:
  build:
    runs-on: ubuntu-22.04
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0 # Fetch all history for git info
      - uses: actions/setup-node@v4
        with:
          node-version: 22
      - name: Install Dependencies
        run: npm ci
      - name: Build Quartz
        run: npx quartz build
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: public
 
  deploy:
    needs: build
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```
- **步骤 5. 更多个性化设置**
	- https://quartz.jzhao.xyz/

