MakeFile
========
[MakeFile note](https://blog.csdn.net/weixin_38391755/article/details/80380786 "a makefile documetation")

```
ifdef DEFINE_VRE
    VRE = “Hello World!”
else
endif

ifeq ($(OPT),define)
    VRE ?= “Hello World! First!”
endif

ifeq ($(OPT),add)
    VRE += “Kelly!”
endif

ifeq ($(OPT),recover)
    VRE := “Hello World! Again!”
endif

all:
    @echo $(VRE)
```
敲入以下make命令：<br>
make DEFINE_VRE=true OPT=define 输出：Hello World! <br>
make DEFINE_VRE=true OPT=add 输出：Hello World! Kelly! <br>
make DEFINE_VRE=true OPT=recover  输出：Hello World! Again! <br>
make DEFINE_VRE= OPT=define 输出：Hello World! First! <br>
make DEFINE_VRE= OPT=add 输出：Kelly! <br>
make DEFINE_VRE= OPT=recover 输出：Hello World! Again! <br>

从上面的结果中我们可以清楚的看到他们的区别了<br>
= 是最基本的赋值 <br>
:= 是覆盖之前的值 <br>
?= 是如果没有被赋值过就赋予等号后面的值 <br>
+= 是添加等号后面的值<br>

