import uuid
def get_id1():
    return ''.join(str(uuid.uuid4()).split('-'))
if __name__ == '__main__':
    print(get_id1())
