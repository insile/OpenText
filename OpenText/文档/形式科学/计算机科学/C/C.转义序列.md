##### 转义序列
- 转义序列
	- 转义序列用于表示字符和字符串字面量中的某些特殊字符
- 语法

|                    |          |                                                             |
| ------------------ | -------- | ----------------------------------------------------------- |
| `\'`               | 单引号      | byte `0x27` in ASCII encoding                               |
| `\"`               | 双引号      | byte `0x22` in ASCII encoding                               |
| `\?`               | 问号       | byte `0x3f` in ASCII encoding                               |
| `\\`               | 反斜杠      | byte `0x5c` in ASCII encoding                               |
| `\a`               | 声音铃声     | byte `0x07` in ASCII encoding                               |
| `\b`               | 退格键      | byte `0x08` in ASCII encoding                               |
| `\f`               | 换页 - 新页面 | byte `0x0c` in ASCII encoding                               |
| `\n`               | 换行 - 新行  | byte `0x0a` in ASCII encoding                               |
| `\r`               | 回车       | byte `0x0d` in ASCII encoding                               |
| `\t`               | 水平制表符    | byte `0x09` in ASCII encoding                               |
| `\v`               | 垂直制表符    | byte `0x0b` in ASCII encoding                               |
| `\nnn`             | 任意八进制值   | code unit `_nnn_`                                           |
| `\xn`              | 任意十六进制值  | code unit `_n..._` (arbitrary number of hexadecimal digits) |
| `\unnnn` (C99)     | Unicode值 | code point `U+_nnnn_`                                       |
| `\Unnnnnnnn` (C99) | Unicode值 | code point `U+_nnnnnnnn_`                                   |
