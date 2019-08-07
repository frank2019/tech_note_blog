git 打标签





# 1，什么是Tag

1. tag是git版本库的一个标记，指向某个commit的指针。
2. tag主要用于发布版本的管理，一个版本发布之后，我们可以为git打上 v.1.0.1 v.1.0.2 ...这样的标签
3. 

# 2，创建

```bash
git tag <tagName> 			//创建本地tag
git push origin <tagName> 	//推送到远程仓库
git push origin --tags     //推送本地的所有tag到远程
git tag -a <tagName> <commitId>    //打标签到指定commit
git log --pretty=oneline //查看当前分支的提交历史 里面包含 commit id
git tag -a <tagname> -m "XXX..." //创建标签可以指定标签信息。
```

# 3，查看标签

```bash
git show <tagName>   //查看本地指定标签
git tag 			//查看本地所有标签
git tag -l			//查看本地所有标签
git ls-remote --tags origin  //查看远程所有 tag
```



# 4，删除标签



```bash
git tag -d <tagName>			//本地 tag 的删除
git push origin :<tagName>		//远程 tag 的删除：
```



# 5， 检出标签



```bash
git checkout -b <branchName> <tagName>
```

