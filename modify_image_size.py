import os
import re

def modify_image_format_in_directory(directory):
    # 遍历指定目录下的所有文件和子目录
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".md"):
                filepath = os.path.join(root, filename)
                # 读取 Markdown 文件内容
                with open(filepath, "r", encoding="utf-8") as file:
                    markdown_content = file.read()
                # 修改图片链接格式
                modified_content = modify_image_format(markdown_content)
                # 将修改后的内容写回原文件
                with open(filepath, "w", encoding="utf-8") as file:
                    file.write(modified_content)
                print(f"文件 '{filename}' 中的图片链接格式已修改！")

def modify_image_format(markdown_text):
    # 首先转换 Markdown 图片格式 ![]()
    markdown_text = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1" style="zoom:40%;" />', markdown_text)
    # 然后调整已是 <img> 标签的图片的 zoom 大小
    modified_text = re.sub(r'<img src="(.*?)" alt="(.*?)" style="zoom:(.*?);(.*?)" />', r'<img src="\1" alt="\2" style="zoom:40%;" />', markdown_text)
    return modified_text

# 指定要处理的根目录
# root_directory = "/Users/man9o/Desktop/Blog/content/Blogs"  # 将根目录路径替换为你的根目录路径
root_directory = "/Users/man9o"  # 将根目录路径替换为你的根目录路径

# 执行递归处理
modify_image_format_in_directory(root_directory)
