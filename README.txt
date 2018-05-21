代码说明：

	本代码运行于 python 3.6.1 及以上版本，无需安装任何第三方库。
	lab1.py为实验一要求的内容
	把需要进行词法分析的内容(如表达式)写在 lab1_testData.txt 中，运行lab1.py即可。

	5/15/2018
	同理，把需要进行语法分析的内容(代码)写在 lab2_testData.txt 中，运行lab2&3.py即可。

	代码中还有一些小BUG，但是答辩和写报告是完全足够了。
	
	请把文档和报告以及需要写的东西做的精美些，谢谢！
	ps:如有疑问随时微信我。


输出结果：
D:\Anaconda3\python.exe D:/Working_repository/compilation/lab2&3.py
while a3+15>10 do if x2=7 then while y<z do y=x*y/z; c=b*c+d;
	while a3+15>10 do if x2=7 then while y<z do y=x*y/z;
		while a3+15>10 do if x2=7 then while y<z do y=x*y/z
			a3+15>10
				a3+15
					a3+15
						a3+15
						a3+15
				10
					10
						10
			if x2=7 then while y<z do y=x*y/z
				x2=7
					x2
						x2
							x2
				while y<z do y=x*y/z
					y<z
						y
							y
								y
						z
							z
								z
					y=x*y/z
						x*y/z
							x*y/z
								x*y
									x
										x
									y
								z
	c=b*c+d;
		c=b*c+d;
			c=b*c+d
				b*c+d
					b*c
						b*c
							b
								b
							c
					d
						d

Process finished with exit code 0