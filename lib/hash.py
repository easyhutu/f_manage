"""
CREATE: 2018/5/13
AUTHOR:　HEHAHUTU
"""
import hashlib


def hash_sha256(value):
    h = hashlib.sha256()
    h.update(value.encode('utf8'))
    return h.hexdigest().upper()


# if __name__ == '__main__':
#     print(hash_data('aaa'))
