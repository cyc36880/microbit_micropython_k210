# micro:bit python库



***详细使用请查看[用户手册（docs/user_manual.pdf）](./docs/user_manual.md)***



## 导入库说明

- hex文件直接导入为一个导入库的空项目
- py为源文件 



[micro:bit Python Editor 网站](https://python.microbit.org/v/3/project)



### 切换为中文

<img src="./assets/image-20250119210934328.png" alt="image-20250119210934328" style="zoom:50%;" />

<img src="./assets/image-20250119211004037.png" alt="image-20250119211004037" style="zoom:50%;" />



<img src="./assets/image-20250119211032537.png" alt="image-20250119211032537" style="zoom:50%;" />



### 导入示例项目

> 此方式是直接导入了一个新的项目，注意将原来编写的代码保存



### 按文件导入

<img src="./assets/image-20250119212736006.png" alt="image-20250119212736006" style="zoom: 33%;" />

<img src="./assets/image-20250119212824647.png" alt="image-20250119212824647" style="zoom:33%;" />

<img src="./assets/image-20250119213132214.png" alt="image-20250119213132214" style="zoom:33%;" />

<img src="./assets/image-20250119213341499.png" alt="image-20250119213341499" style="zoom:33%;" />

<font color=red><big>***特别注意***</big></font>

~~最好将库文件全部导入。除非明确知道单个文件的作用，否则不要只导入单个文件。<mark>文件间存在依赖关系</mark>。~~

`iic_base.py` 、`color.py` 、`DC_motor` 为必须导入的文件，其他请按需导入，否则可能会导致内存过大无法使用



