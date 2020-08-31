
while True:
    name = input("请输入名字:")
    age = input("请输入年龄:")
    job = input("请输入工作:")
    hobby = input("请输入爱好:")
    msg = '''
    --------------- info of %s ----------------
    Name:   %s
    Age:    %s
    Job:    %s
    Hobby:  %s
    ------------------ end --------------------
    ''' % (name,name,age,job,hobby)

    print(msg)