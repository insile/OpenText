# -*- coding: utf-8 -*-
"""
从 words 生成索引文件
https://opentext.net.cn/
"""

from pathlib import Path
import pandas as pd

level = ["级别/小学", "级别/中考", "级别/高考四级", "级别/考研",
         "级别/六级", "级别/雅思", "级别/托福", "级别/GRE",
         "词性/n", "词性/v", "词性/vt", "词性/vi", "词性/modal",
         "词性/aux", "词性/inf", "词性/adj", "词性/adv",
         "词性/prep", "词性/pron", "词性/conj", "词性/det",
         "词性/num", "词性/art", "词性/int", "词性/abbr"]


def main(current_dir):
    words_dir = current_dir / 'words'
    index_dir = current_dir / '索引'

    datas = []
    words_path = words_dir.rglob('*.md')
    for word_path in words_path:
        with open(word_path, 'r', encoding='utf-8') as f:
            data = []
            data.append(word_path.stem)
            text = f.read()
            for lll in level:
                if lll in text:
                    data.append(1)
                else:
                    data.append(0)
            datas.append(data)
            print(data)
    columns = ['级别/全索引'] + level
    df = pd.DataFrame(datas, columns=columns)
    row_sums = df.iloc[:, 1:].sum(axis=1)
    # df[row_sums < 2] 单词标签不完整

    for i in range(9):
        level_index_dir = (index_dir / columns[i].split('/')[-1])
        level_index_dir.mkdir(parents=True, exist_ok=True)
        level_index_file = level_index_dir / f'单词索引.{level_index_dir.stem}.md'

        with open(level_index_file, 'w', encoding='utf-8', newline="\n") as lif:
            level_index_df = []
            if i == 0:
                lif.write(f'##### {level_index_file.stem} {len(df)}\n')
            else:
                lif.write(f'##### {level_index_file.stem} {len(df[df[columns[i]] == 1])}\n')

            for j in range(ord('a'), ord('z') + 1):
                word_file = level_index_dir / f'{level_index_dir.stem}.{chr(j).upper()}.md'

                if i == 0:
                    ds = df[df[columns[0]].str.startswith(chr(j))][columns[0]]
                else:
                    ds = df[(df[columns[i]] == 1) & (df[columns[0]].str.startswith(chr(j)))][columns[0]]
                ds = ds.apply(lambda x: f"- [ ] [[{x}]]\n")

                with open(word_file, 'w', encoding='utf-8', newline="\n") as f:
                    f.write(f'##### {word_file.stem} {len(ds)}\n')
                    f.write(''.join(ds.to_list()))

                level_index_df.append([f'[{chr(j).upper()}]({word_file.stem})', len(ds)])
                print(f'{columns[i]} {chr(j)}')

            level_index_df = pd.DataFrame(level_index_df)
            lif.write(level_index_df.to_markdown(index=False))


if __name__ == '__main__':
    current_dir = Path(__file__).parent
    main(current_dir)
    print('完成')
