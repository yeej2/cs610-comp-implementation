import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from application import students

def test_login_logout():
    rv = login.login('stu', 'pass')
    assert b'You were logged in' in rv.data
    # rv = self.logout()
    # assert b'You were logged out' in rv.data
    # rv = self.login('adminx', 'default')
    # assert b'Invalid username' in rv.data
    # rv = self.login('admin', 'defaultx')
    # assert b'Invalid password' in rv.data
