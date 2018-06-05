class Code:
    SUCCESS = 0
    FAILED = 2
    NO_PARAM = 400

    # login code
    AUTHORIZED_FAILED = 100
    USERNAME_EMPTY = 101
    PASSWORD_ERROR = 102

    msg = {
        SUCCESS: "success",
        FAILED: 'request failed',
        NO_PARAM: "invalid param",
        USERNAME_EMPTY: 'username empty',
        PASSWORD_ERROR: 'password error',
        AUTHORIZED_FAILED: 'authorized failed'

    }


def to_json(**kwargs):
    data = {}
    for key, value in kwargs.items():
        data[key] = value
    return data


class Msg:
    @staticmethod
    def success(msg, **kwargs):
        if kwargs:
            return {'code': Code.SUCCESS, 'message': msg, 'data': to_json(**kwargs)}
        else:
            return {'code': Code.SUCCESS, 'message': msg}

    @staticmethod
    def failed(msg, **kwargs):
        if kwargs:
            return {'code': Code.FAILED, 'message': msg, 'data': to_json(**kwargs)}
        else:
            return {'code': Code.FAILED, 'message': msg}

    @staticmethod
    def failed_dict(code: int, **kwargs):
        if kwargs:
            return {'code': code, 'message': code_dict.get(str(code), ''), 'data': to_json(**kwargs)}
        else:
            return {'code': code, 'message': code_dict.get(str(code), '')}

    @staticmethod
    def login_username_error(msg):
        return {'code': Code.USERNAME_EMPTY, 'message': msg}

    @staticmethod
    def login_password_error(msg):
        return {'code': Code.PASSWORD_ERROR, 'message': msg}

    @staticmethod
    def authorized_failed(code=Code.AUTHORIZED_FAILED, **kwargs):
        return {'code': code, 'message': Code.msg[code], 'data': to_json(**kwargs)}


code_dict = {
    '1001': '磁盘空间不足，无法上传',
    '1002': '无效的id',
    '2001': "need admin role auth",
    '2002': "need group role auth"
}
