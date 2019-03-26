



#### 下载代码

```
git  clone   gitlab@120.78.87.224:zy_tools/FirwareTestApp.git
```



### 创建分支并提交到远程

1，查看远端分支情况

```
git   branch  -r
```

2，本地创建分支

```
git   branch -b dev  //创建本地分支
```

3，提交本地分支到远程

```
git  push origin dev：dev     //本地分支名:远程分支名
```



### git fetch 和git pull 的差别



1，git fetch 相当于是从远程获取最新到本地，不会自动merge

2，git pull：相当于是从远程获取最新版本并merge到本地

指令示例

```bash
git fetch orgin master //将远程仓库的master分支下载到本地当前branch中
git log -p master  ..origin/master //比较本地的master分支和origin/master分支的差别
git merge origin/master //进行合并
```

也可以用如下指令

```
git fetch origin master:tmp //从远程仓库master分支获取最新，在本地建立tmp分支

git diff tmp //將當前分支和tmp進行對比

git merge tmp //合并tmp分支到当前分支
```



```
git pull origin master   //git pull 相当于从远程获取最新版本并merge到本地
```





在实际使用中，git fetch更安全一些





git add   filename



`git reset HEAD <撤销的文件1>`





### 参考链接

1. [git fetch 和git pull 的差别](https://www.cnblogs.com/qiu-Ann/p/7902855.html)
2. 