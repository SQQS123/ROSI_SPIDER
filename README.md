# ROSI_SPIDER
git上下了一个爬ROSI的，然后发现好像不好用，我就新写了一个，由于我是一个穷屌(技术不够牛逼)，所以，只能每组下载三张图片，接下来我估计会研究研究怎么爬取收费的东西了，开源精神嘛，就是要突破那些土豪的限制

新建一个pics文件夹

然后scrapy crawl rosi_spider

应该就可以在pics里面看到图片了，里面根据hash生成的图片名称，如果中断任务，下次下载会自动忽略已经下载的图片的。

最后奉劝各位注意身体啊~~~

补充知识，如果没有scrapy.cfg文件可以使用如下方式解决：
把pics文件夹拉到spider文件夹，然后在spider文件夹执行scrapy runspider rosi_spider.py即可

但是如果我们想要更优雅的解决方式呢？
我们可以自己写个scrapy.cfg文件，内容不多如下，需要放在ROSI目录旁边：
[settings]
default = ROSI.settings

[deploy]
project = ROSI

如果有什么想探讨的，我的联系方式:
QQ:749804235
mobile:17513257267
