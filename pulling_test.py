from user_inform import collect_inform

def is_collect_inform(_id, password):
    return True if (_id==collect_inform['_id'] \
                    and password==collect_inform['passwd']) \
                        else False
    
if __name__=='__main__':
    _id = input('id:')
    passwd = input('passwd:')

    if is_collect_inform(_id, passwd) == True:
        print('It is collect inform')
    else:
        print('It is incollect inform')
