# DataHub 教学文档 @ readthedocs.org
## 虚拟环境
需要预先安装 `pipenv` 库，之后在 `Pipfile` 所在文件夹下使用如下命令创建并配置虚拟环境。
```
pipenv shell
pipenv install
```


## 本地预览
本文档使用 MarkDown 编写，使用 MkDocs 生成静态页面。在 `mkdocs.yml` 所在文件夹下使用如下命令在 [本地](http://127.0.0.1:8000) 进行预览。
```
mkdocs serve
```


## 链接测试
文档链接可以使用 `test.py` 测试有效性，同时程序最后会显示所有链接的顶级域名。建议使用较常见的域名，防止域名所有者忘记续费的问题，例如文档中的 [NLP](docs/field/nlp.md) 部分使用 GitHub 链接而非自己注册的 nlpprogress.com。
<details>
<summary>文档中已有域名</summary>
<li>github.com</li>
<li>gitlab.com</li>
<li>python.org</li>
<li>readthedocs.io</li>
<li>liaoxuefeng.com</li>
<li>vbird.org</li>
<li>pypi.org</li>
<li>realpython.com</li>
<li>mathworks.com</li>
</details>
