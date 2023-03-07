from test import Add
def TestAdd():
    assert Add(1,10)==11
    assert Add(20,12)==32
    print("Right")
if __name__=='__main__':
    TestAdd()
