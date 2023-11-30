import opencc
import os
import sys


def get_input_text():
    return input("请输入要转换的文本：")


def get_output_format():
    print("请选择转换方式:")
    number = 1
    options_text = [
        "简体到繁体", "简体到台湾正体", "简体到繁体（台湾正体标准）并转换为台湾常用词汇", "简体到香港繁体",
        "繁体到简体", "繁体（OpenCC 标准）到台湾正体", "繁体（OpenCC 标准）到香港繁体", "台湾正体到简体",
        "繁体（台湾正体标准）到简体并转换为中国大陆常用词汇", "台湾正体到繁体（OpenCC 标准）",
        "香港繁体到简体", "香港繁体到繁体（OpenCC 标准）", "繁体（OpenCC 标准，旧字体）到日文新字体",
        "日文新字体到繁体（OpenCC 标准，旧字体）"
    ]
    for option_text in options_text:
        print(f"{number}.{option_text}")
        number += 1

    choice = int(input("请选择转换方式：")) - 1

    options = ["s2t", "s2tw", "s2twp", "s2hk", "t2s", "t2tw", "t2hk", "tw2s", "tw2sp", "tw2t", "hk2s", "hk2t", "t2jp", "jp2t"]

    return options[choice]


def convert_text(input_text, config):
    converter = opencc.OpenCC(config)
    return converter.convert(input_text)


def main():
    if len(sys.argv) > 1 and (sys.argv[1].endswith('.txt') or sys.argv[1].endswith('.md')):
        # 如果拖入文档
        input_file = sys.argv[1]
        output_format = get_output_format()

        with open(input_file, 'r', encoding='utf-8') as file:
            input_text = file.read()

        converted_text = convert_text(input_text, output_format + ".json")

        # 构建输出文件名
        output_file = f"{os.path.splitext(input_file)[0]} - {output_format}{os.path.splitext(input_file)[1]}"

        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(converted_text)

        print(f"转换完成，结果已保存至 {output_file}")
    else:
        # 如果直接运行程序
        input_text = get_input_text()
        output_format = get_output_format()

        converted_text = convert_text(input_text, output_format + ".json")

        print("转换结果：")
        print(converted_text)
        # 确保有机会复制结果
        input("按任意键退出...")

if __name__ == "__main__":
    main()
