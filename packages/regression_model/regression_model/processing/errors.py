class BaseError(Exception):
    """基本パッケージエラー。"""


class InvalidModelInputError(BaseError):
    """モデル入力にエラーが含まれています。"""
