A Small Compilation Programme written by Python3


Version specification
    This programme is based on Python 3.6.1 and PLY.
    Please download PLY on PLY homepage( http://www.dabeaz.com/ply/ ) and copy the fold into Python3/Lib or Python3/libs.
    The programme read your "code" from both lab1_testData.txt and lab2_testData.txt ,so write down your "code" into these two txts and run lab1.py or lab2&3.py .


Solution of shift/reduce conflicts

    By default, all shift/reduce conflicts are resolved in favor of shifting.
    Therefore, in the above example, the parser will always shift the + instead of reducing.
    Although this strategy works in many cases (for example, the case of "if-then" versus "if-then-else"), it is not enough for arithmetic expressions.
    In fact, in the above example, the decision to shift + is completely wrong---we should have reduced expr * expr since multiplication has higher mathematical precedence than addition.

    copy from  http://www.dabeaz.com/ply/ply.html  |  6.6 Dealing With Ambiguous Grammars


Terminal Output:

D:\Anaconda3\python.exe D:/Working_repository/compilation/lab2&3.py
while a3+15>10 do if x2=7 then while y<z do y=x*y/z; c=b*c+d;
	while a3+15>10 do if x2=7 then while y<z do y=x*y/z;
		while a3+15>10 do if x2=7 then while y<z do y=x*y/z
			a3+15>10
				a3+15
					a3+15
						a3+15
							a3+15
								a3
									a3
										a3
								15
									15
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