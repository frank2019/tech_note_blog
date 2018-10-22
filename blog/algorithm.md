参考链接

1.  [神奇的λ演算](https://www.jianshu.com/p/e7db2f50b012)
2. 邱奇编码（Church Encoding）的Javascript实现练习

### 参考链接

1. https://github.com/kdn251/interviews/blob/master/README-zh-cn.md
2. [数据结构与算法——常用数据结构及其Java实现](https://segmentfault.com/a/1190000009797159)

 

## 数据结构







### 0x01 链表 Linked List

链表即是由节点（Node）组成的线性集合，每个节点可以利用指针指向其他节点。它是一种包含了多个节点的、能够用于表示序列的数据结构。 也可以不科学得理解为二叉树得一种特殊情况

**单向链表**: 链表中的节点仅指向下一个节点，并且最后一个节点指向空。

**双向链表**: 其中每个节点具有两个指针 p、n，使得 p 指向先前节点并且 n 指向下一个节点；最后一个节点的 n 指针指向 null，第一个节点得p指针指向null。

**循环链表**：每个节点指向下一个节点并且最后一个节点指向第一个节点的链表。

**循环链表**：每个节点指向下一个节点并且最后一个节点指向第一个节点的链表。

时间复杂度: 

- 索引: `O(n)`
- 搜索: `O(n)`
- 插入: `O(1)`
- 移除: `O(1)`





### 数组

java数组是一种线性得数据结构，增加和删除时间复杂度为 O(n), 修改和查询 为 O(1)

#### 基本得数组结构

int []  intarray = new int[10];

循环和遍历

1. 支持使用下标进行遍历和访问
2. 支持使用foreach 形式得遍历和访问



Arraylist



#### Arrays 类

 java.util.Arrays 类能方便地操作数组，它提供的所有方法都是静态的。

具有以下功能：

- 给数组赋值：通过 fill 方法。
- 对数组排序：通过 sort 方法,按升序。
- 比较数组：通过 equals 方法比较数组中元素值是否相等。
- 查找数组元素：通过 binarySearch 方法能对排序好的数组进行二分查找法操作。

具体说明请查看下表：

| 序号 | 方法和说明                                                   |
| ---- | ------------------------------------------------------------ |
| 1    | **public static int binarySearch(Object[] a, Object key)**  				用二分查找算法在给定数组中搜索给定值的对象(Byte,Int,double等)。数组在调用前必须排序好的。如果查找值包含在数组中，则返回搜索键的索引；否则返回 (-(*插入点*) - 1)。 |
| 2    | **public static boolean equals(long[] a, long[] a2)**  				如果两个指定的 long 型数组彼此*相等*，则返回  true。如果两个数组包含相同数量的元素，并且两个数组中的所有相应元素对都是相等的，则认为这两个数组是相等的。换句话说，如果两个数组以相同顺序包含相同的元素，则两个数组是相等的。同样的方法适用于所有的其他基本数据类型（Byte，short，Int等）。 |
| 3    | **public static void fill(int[] a, int val)**  				将指定的 int 值分配给指定 int 型数组指定范围中的每个元素。同样的方法适用于所有的其他基本数据类型（Byte，short，Int等）。 |
| 4    | **public static void sort(Object[] a)**  				对指定对象数组根据其元素的自然顺序进行升序排列。同样的方法适用于所有的其他基本数据类型（Byte，short，Int等）。 |

### 0x00  常见数据结构



以java为例

| 数据结构 | 优点 | 缺点 | 时间复杂度 |
| -------- | ---- | ---- | ---------- |
| 数组[]   |      |      |            |
| 有序数组 |      |      |            |
| zhan     |      |      |            |



![](https://images2018.cnblogs.com/blog/1120165/201711/1120165-20171124224517593-271461566.png)





![](https://images2018.cnblogs.com/blog/1120165/201711/1120165-20171124223229656-408723583.png)





----



#### 二叉树搜索树



给予一个二叉树的根节点，验证该树是否是二叉树搜索树，（在O(n)时间内），请用你熟悉的语言写出算法



二叉查找树（Binary Search Tree），（又：[二叉搜索树](https://baike.baidu.com/item/%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91)，二叉排序树）它或者是一棵空树，或者是具有下列性质的[二叉树](https://baike.baidu.com/item/%E4%BA%8C%E5%8F%89%E6%A0%91)： 若它的左子树不空，则左子树上所有结点的值均小于它的根结点的值； 若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值； 它的左、右子树也分别为[二叉排序树](https://baike.baidu.com/item/%E4%BA%8C%E5%8F%89%E6%8E%92%E5%BA%8F%E6%A0%91)。 







### Sql语句查询某列A相同值的另一列B最大值的数据

有一个用户表User （id, email)，一个付费记录表Transaction (id, transaction_type, transaction_amount)， 找出在每个付费类别里，付费总额最高的3个用户的email 和付费总额。



1. [Sql语句查询某列A相同值的另一列B最大值的数据](https://www.cnblogs.com/qubernet/p/5810257.html)





 

 



 

这是我收藏的经典算法网站，对题主或许有用
有很多游戏开发相关的算法介绍： 
[http://www.gamedev.net](https://link.zhihu.com/?target=http%3A//www.gamedev.net) 
[http://theory.stanford.edu/~amitp/GameProgramming](https://link.zhihu.com/?target=http%3A//theory.stanford.edu/%7Eamitp/GameProgramming) 
[http://www.gamasutra.com](https://link.zhihu.com/?target=http%3A//www.gamasutra.com) 
[http://www.sudoku.com](https://link.zhihu.com/?target=http%3A//www.sudoku.com) 

俄罗斯方块游戏的算法网站： 
[http://gforge.inria.fr/projects/mdptetris](https://link.zhihu.com/?target=http%3A//gforge.inria.fr/projects/mdptetris) [http://colinfahey.com/tetris/tetris.html](https://link.zhihu.com/?target=http%3A//colinfahey.com/tetris/tetris.html) 

leetcode，最近很火的算法网站： 
[http://www.leetcode.com](https://link.zhihu.com/?target=http%3A//www.leetcode.com) 

Topcoder，也很经典，每周都有竞赛，有奖金的： 
[http://community.topcoder.com/tc](https://link.zhihu.com/?target=http%3A//community.topcoder.com/tc) 

晋中教育网的“信息学竞赛辅导”： 
[http://www.jzsyz.jzedu.cn/xxjs/suanfa/index.html](https://link.zhihu.com/?target=http%3A//www.jzsyz.jzedu.cn/xxjs/suanfa/index.html) 

 

http://poj.org/

 

http://acm.hdu.edu.cn/

 

http://acm.hust.edu.cn/vjudge/toIndex.action