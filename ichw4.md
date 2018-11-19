1.作业是要求计算机所做工作的集合

进程是计算机中的程序关于某数据集合上的一次运行活动，是系统进行资源分配和调度的基本单位，是操作系统结构的基础

线程是在计算机处理文件时两个文件同时运行时程序执行流的最小单元

进程的提出解决了多道程序运行时资源的分配和调度的问题

线程的提出解决了进程作为资源拥有者，创建、撤消与切换存在较大的时空开销以及多个进程并行开销过大的问题

2.虚拟存储器

概念：计算机系统内存管理的一种技术。

工作原理：①中央处理器访问主存的逻辑地址分解成组号a和组内地址b，并对组号a进行地址变换，即将逻辑组号a作为索引，查地址变换表，以确定该组信息是否存放在主存内。
②如该组号已在主存内，则转而执行④；如果该组号不在主存内，则检查主存中是否有空闲区，如果没有，便将某个暂时不用的组调出送往辅存，以便将这组信息调入主存。
③从辅存读出所要的组，并送到主存空闲区，然后将那个空闲的物理组号a和逻辑组号a登录在地址变换表中。
④从地址变换表读出与逻辑组号a对应的物理组号a。
⑤从物理组号a和组内字节地址b得到物理地址。
⑥根据物理地址从主存中存取必要的信息。

作用：1）缓存，解决内存不够的问题  2）利用虚拟地址来映射物理地址，使得可以让多个进程的不同虚拟地址映射同一块物理地址  3）保护存储器