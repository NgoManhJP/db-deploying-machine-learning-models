from marshmallow import Schema, fields
from marshmallow import ValidationError

import typing as t
import json


class InvalidInputError(Exception):
    """モデル入力が無効"""


SYNTAX_ERROR_FIELD_MAP = {
    '1stFlrSF': 'FirstFlrSF',
    '2ndFlrSF': 'SecondFlrSF',
    '3SsnPorch': 'ThreeSsnPortch'
}


class HouseDataRequestSchema(Schema):
    Alley = fields.Str(allow_none=True)
    BedroomAbvGr = fields.Integer()
    BldgType = fields.Str()
    BsmtCond = fields.Str()
    BsmtExposure = fields.Str(allow_none=True)
    BsmtFinSF1 = fields.Float()
    BsmtFinSF2 = fields.Float()
    BsmtFinType1 = fields.Str()
    BsmtFinType2 = fields.Str()
    BsmtFullBath = fields.Float()
    BsmtHalfBath = fields.Float()
    BsmtQual = fields.Str(allow_none=True)
    BsmtUnfSF = fields.Float()
    CentralAir = fields.Str()
    Condition1 = fields.Str()
    Condition2 = fields.Str()
    Electrical = fields.Str()
    EnclosedPorch = fields.Integer()
    ExterCond = fields.Str()
    ExterQual = fields.Str()
    Exterior1st = fields.Str()
    Exterior2nd = fields.Str()
    Fence = fields.Str(allow_none=True)
    FireplaceQu = fields.Str(allow_none=True)
    Fireplaces = fields.Integer()
    Foundation = fields.Str()
    FullBath = fields.Integer()
    Functional = fields.Str()
    GarageArea = fields.Float()
    GarageCars = fields.Float()
    GarageCond = fields.Str()
    GarageFinish = fields.Str(allow_none=True)
    GarageQual = fields.Str()
    GarageType = fields.Str(allow_none=True)
    GarageYrBlt = fields.Float()
    GrLivArea = fields.Integer()
    HalfBath = fields.Integer()
    Heating = fields.Str()
    HeatingQC = fields.Str()
    HouseStyle = fields.Str()
    Id = fields.Integer()
    KitchenAbvGr = fields.Integer()
    KitchenQual = fields.Str()
    LandContour = fields.Str()
    LandSlope = fields.Str()
    LotArea = fields.Integer()
    LotConfig = fields.Str()
    LotFrontage = fields.Float(allow_none=True)
    LotShape = fields.Str()
    LowQualFinSF = fields.Integer()
    MSSubClass = fields.Integer()
    MSZoning = fields.Str()
    MasVnrArea = fields.Float()
    MasVnrType = fields.Str(allow_none=True)
    MiscFeature = fields.Str(allow_none=True)
    MiscVal = fields.Integer()
    MoSold = fields.Integer()
    Neighborhood = fields.Str()
    OpenPorchSF = fields.Integer()
    OverallCond = fields.Integer()
    OverallQual = fields.Integer()
    PavedDrive = fields.Str()
    PoolArea = fields.Integer()
    PoolQC = fields.Str(allow_none=True)
    RoofMatl = fields.Str()
    RoofStyle = fields.Str()
    SaleCondition = fields.Str()
    SaleType = fields.Str()
    ScreenPorch = fields.Integer()
    Street = fields.Str()
    TotRmsAbvGrd = fields.Integer()
    TotalBsmtSF = fields.Float()
    Utilities = fields.Str()
    WoodDeckSF = fields.Integer()
    YearBuilt = fields.Integer()
    YearRemodAdd = fields.Integer()
    YrSold = fields.Integer()
    FirstFlrSF = fields.Integer()
    SecondFlrSF = fields.Integer()
    ThreeSsnPortch = fields.Integer()


def _filter_error_rows(errors: dict,
                       validated_input: t.List[dict]
                       ) -> t.List[dict]:
    """エラーのある入力データ行を削除"""

    indexes = errors.keys()
    # それらを逆の順序で削除して、後続のインデックスを破棄しないようにします。
    for index in sorted(indexes, reverse=True):
        del validated_input[index]

    return validated_input


def validate_inputs(input_data):
    """スキーマに対して予測入力を確認"""

    # set many=True リストの受け渡しを許可
    schema = HouseDataRequestSchema(strict=True, many=True)

    # 構文エラーフィールド名の変換（数字で始まる）
    for dict in input_data:
        for key, value in SYNTAX_ERROR_FIELD_MAP.items():
            dict[value] = dict[key]
            del dict[key]

    errors = None
    try:
        schema.load(input_data)
    except ValidationError as exc:
        errors = exc.messages

    # 構文エラーのフィールド名を元に戻す
    # 最初の文字に数字を使用してデータフィールドに名前を付けない
    for dict in input_data:
        for key, value in SYNTAX_ERROR_FIELD_MAP.items():
            dict[key] = dict[value]
            del dict[value]

    if errors:
        validated_input = _filter_error_rows(
            errors=errors,
            validated_input=input_data)
    else:
        validated_input = input_data

    return validated_input, errors
