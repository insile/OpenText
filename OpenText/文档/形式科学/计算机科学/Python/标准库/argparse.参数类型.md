##### argparse.参数类型
- 这是一段示例，可保存为`test.py`，在终端通过下面脚本调用
- `python test.py input.txt output.txt --mode read --verbose --debug --num 10000 --uppercase`
```python
import argparse
# 保存test.py文件通过命令行调用传参
# python test.py input.txt output.txt --mode read --verbose --debug --num 10000 --uppercase

def main():
	# 创建解析器
    parser = argparse.ArgumentParser(description='A comprehensive argparse example')

    # 位置参数，位置参数是在命令行上按照顺序出现的参数，不需要指定参数名
    parser.add_argument('input_file', help='Input file path')
    parser.add_argument('output_file', help='Output file path')

    # 必选参数, required=True
    parser.add_argument('--mode', required=True, choices=['read', 'write'], help='Choose operation mode')  # choices 有效参数列表

    # 可选参数
    parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose mode')
    parser.add_argument('--debug', action='store_true', help='Enable debug mode')
    parser.add_argument('--num', type=int, default=5, help='Number of iterations')

    # 布尔参数，通常用于启用或禁用某些功能
    parser.add_argument('--uppercase', action='store_true', help='Convert to uppercase')

    args = parser.parse_args()

    if args.verbose:
        print("Verbose mode enabled")

    if args.debug:
        print("Debug mode enabled")

    print(f"Input file: {args.input_file}")
    print(f"Output file: {args.output_file}")
    print(f"Mode: {args.mode}")
    print(f"Number of iterations: {args.num}")

    if args.uppercase:
        print("Uppercase conversion enabled")

    if args.encrypt:
        print("Encryption enabled")
    elif args.decrypt:
        print("Decryption enabled")

if __name__ == '__main__':
    main()

```

