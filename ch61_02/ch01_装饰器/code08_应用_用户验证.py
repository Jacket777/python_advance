"""
装饰器应用---用户验证
在运行装饰方法之前执行某种正确性检查
"""
import functools


# TODO 1 编写用户类型，属性中有姓名和邮件
class User(object):
    """A representation of a user in our application"""

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def display_info(self):
        print(self.username+" "+self.email)


# TODO 2 匿名用户类，用来替代真正的用户类
class AnonymousUser(User):
    """An anonymous user; a stand-in for an actual user that nonetheless is not an actual user"""

    def __init__(self):
        self.username = None
        self.email = None

    def __nonzero__(self):
        return False


# TODO 3 装饰器，用来验证用户是否真实
def requires_user(func):
    @functools.wraps(func)
    def inner(user, *args, **kwargs):
        if user and isinstance(user, User):
            return func(user, *args, **kwargs)
        else:
            raise ValueError('A valid user is required to return this')
    return inner


@requires_user
def test(user):
    user.display_info()


def test01():
    print("测试真实用户")
    user = User("jack", "12")
    test(user)
    print("测试匿名用户")
    # user = AnonymousUser()
    # test(user)
    print("测试SB用户")
    user = 12
    test(user)



if __name__ == '__main__':
    test01()
