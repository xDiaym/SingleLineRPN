print((lambda f,i:f.reduce((lambda s,_:(lambda t,d:{'+':lambda a,b:a+b,'-':lambda a,b:a-b,'*':lambda a,b:a*b,'/':lambda a,b:a/b}.get(t)(s, d))(i.pop(0),float(i.pop(0)))),i,float(i.pop(0))))(__import__('functools'),__import__('sys').argv[1:]+['']))