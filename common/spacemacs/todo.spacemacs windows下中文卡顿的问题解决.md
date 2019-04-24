



解决在windows下在有中文的时候特别卡顿的问题

```
不积跬步,无以至千里;不积小流,无以成江海。
																		-荀子《劝学篇》
```



#### 解决办法

在配置文件`.spacemacs`中，增加如下配置

```lisp
(when 
  (eq system-type 'windows-nt)
  (setq gc-cons-threshold (* 512 1024 1024))
  (setq gc-cons-percentage 0.5)
  (run-with-idle-timer 5 t #'garbage-collect)
  (setq garbage-collection-messages t))
```

#### 原理分析



#### 相关命令



| Key Binding | Description    |
| ----------- | -------------- |
| `SPC f e d` | 打开配置文件   |
| `SPC f e R` | 应用配置当当前 |



#### 参考链接

1. http://yihuawanglv.github.io/2018/09/13/%E6%88%91%E7%9A%84Emacs-spacemacs%E4%BD%BF%E7%94%A8%E9%85%8D%E7%BD%AE%E8%AE%B0%E5%BD%95/