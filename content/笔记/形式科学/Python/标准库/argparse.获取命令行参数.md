##### argparse.获取命令行参数
- 这是一段示例，可保存为`test.py`，在终端通过下面脚本调用
- `python test.py --input input.txt --output output.txt --verbose`
```python
import argparse

def main():
	# 创建解析器
    parser = argparse.ArgumentParser(description="Example script with named arguments.")

	# 添加参数 
	# 必选参数input
    parser.add_argument('--input', required=True, help='Input file name')
    # 必选参数output
    parser.add_argument('--output', required=True, help='Output file name')
    # 布尔参数verbose，默认True
    parser.add_argument('--verbose', action='store_true', help='Enable verbose mode')

	# 解析参数获得参数键值对
    args = parser.parse_args()

    print("Input file:", args.input)
    print("Output file:", args.output)
    if args.verbose:
        print("Verbose mode is enabled")

if __name__ == '__main__':
    main()
```
