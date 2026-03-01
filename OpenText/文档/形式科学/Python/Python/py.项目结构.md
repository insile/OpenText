##### 项目结构
- 项目结构
	- Python 项目结构是项目所有文件的目录层次, 合理的项目结构不仅有助于团队协作, 还能方便项目的测试, 部署和文档化, 是项目可维护性, 可扩展性和可读性的基础. 以下是一个典型的项目结构. 每个项目应该
		- 模块化设计, 将功能拆分为多个模块和子包, 避免将所有代码放在一个文件中
		- 使用虚拟环境, 隔离项目依赖
		- 编写测试, 为每个模块编写单元测试, 确保代码的正确性
		- 文档化, 为项目编写清晰的文档, 包括模块说明, API 文档和使用示例
		- 版本控制, 使用版本控制软件
		- 自动化工具, 使用工具自动化构建, 测试和部署流程


```shell
my_project/
├── my_project/               # 项目主包
│   ├── __init__.py           # 包初始化文件
│   ├── module1.py            # 模块1
│   ├── module2.py            # 模块2
│   └── utils/                # 工具模块
│       ├── __init__.py
│       └── helper.py
├── tests/                    # 测试代码
│   ├── __init__.py
│   ├── test_module1.py
│   └── test_module2.py
├── docs/                     # 文档
│   └── index.md
├── scripts/                  # 脚本文件
│   └── setup_environment.sh
├── requirements.txt          # 依赖列表
├── setup.py                  # 项目安装脚本
├── pyproject.toml            # 构建配置文件（可选）
├── README.md                 # 项目说明
└── .gitignore                # Git 忽略文件
```