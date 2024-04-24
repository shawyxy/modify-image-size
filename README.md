## 批量修改 markdown 文件中图片的大小格式
**使用编辑器**:typora

由于 markdown 文件转换为 HTML 后的图片尺寸很大,typora虽然可以手动地调整图片大小,但是还是很麻烦

图片格式主要有两种:
- `![]()`
- `<img>` 标签

要解决的问题:
- 把 Markdown 中的 `![]()` 格式的图片链接转换为 <img> 标签格式。
- 修改已经是 `<img>` 标签的图片，调整其 zoom 属性的值为 40%。

**注意事项**:这个脚本会处理根目录 `root_directory` 下的所有 markdown 文件

使用方法:修改你要的大小,然后运行
```
sudo Python modify_image_size.py
```
