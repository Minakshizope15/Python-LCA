def triangle():
    s1=12
    s2=14
    s3=12
    if( s1==s2==s3): 
        print("equilateral triangle")
    elif (s1==s2 or s2==s3 or s3==s1):
         print("isosceles triangle")
    else: print("scalar triangle") 

triangle()
