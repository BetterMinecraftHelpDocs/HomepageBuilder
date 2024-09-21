# 主页构建器-教程优化
## 用途
一个PCL主页构建器框架，从基本的XAML或者其它比如Markdown类似的代码生成一个用于PCL的主页文件，以方便复杂主页的维护

构建器可在两种模式下运行：构建器模式和服务器模式。构建器使用工程文件生成主页代码；服务器使用工程文件响应来自PCL的请求，提供联网更新

优化了快速上手 为新手提供更好的入门教程


# 快速上手
## 一、准备工作
### 1. 安装 Python
主页构建器所需 Python 版本为 3.9+

### 2. 下载 HomepageBuilder 源码
你可以通过 GitHub Releases 或 Git Clone 下载构建器的源码 

#### 通过 Release
1. 打开 [HomepageBuilder 的最新发布版](https://github.com/Light-Beacon/HomepageBuilder/releases/latest)
2. 下载 Source code 文件（如果不知道下哪个好就下 zip）
3. 解压下载的文件到想存放的位置下

#### 通过 Git Clone
1. 在存放位置处运行 `git clone https://github.com/Light-Beacon/HomepageBuilder.git .`

### 3. 安装依赖
#### 基础依赖
运行在文件夹以下命令以安装依赖
```bash
pip3 install -r requirements.txt
```
#### 服务器依赖
如果你需要使用构建器部署服务器，你需要额外安装服务器的依赖
```bash
pip3 install -r server_requirements.txt
```
## 二、构建主页
### 1. 获取主页工程模版
点击该[链接](https://github.com/Light-Beacon/HomepageProjectTemplate/archive/refs/heads/main.zip)下载工程文件模版并解压

### 2. 构建第一个主页
运行以下命令
```bash
python3 <构建器main.py的绝对路径> build <工程文件夹下Project.yml文件的绝对路径> <主页生成文件的绝对路径>
```
>[!IMPORTANT]
>如果Python3命令开头无法运行
>
>尝试将Python3改为Python即：
>
>python <构建器main.py的绝对路径> build <工程文件夹下Project.yml文件的绝对路径> <主页生成文件的绝对路径>
>
>主页生成文件的绝对路径例子：C:\Users\Administrator\Desktop\PCL\（Custom.xaml）如例子所见 需要带有文件名和.xaml


### 3. 启动 PCL 查看主页
若你生成于PCL文件夹的 Custom.xaml，这时启动 PCL，将自定义主页选择本地文件，就可以看到主页啦！

