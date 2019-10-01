import pathlib

import regression_model


PACKAGE_ROOT = pathlib.Path(regression_model.__file__).resolve().parent
TRAINED_MODEL_DIR = PACKAGE_ROOT / 'trained_models'
DATASET_DIR = PACKAGE_ROOT / 'datasets'

# データ
TESTING_DATA_FILE = 'test.csv'
TRAINING_DATA_FILE = 'train.csv'
TARGET = 'SalePrice'


# 変数
FEATURES = ['MSSubClass', 'MSZoning', 'Neighborhood',
            'OverallQual', 'OverallCond', 'YearRemodAdd',
            'RoofStyle', 'MasVnrType', 'BsmtQual', 'BsmtExposure',
            'HeatingQC', 'CentralAir', '1stFlrSF', 'GrLivArea',
            'BsmtFullBath', 'KitchenQual', 'Fireplaces', 'FireplaceQu',
            'GarageType', 'GarageFinish', 'GarageCars', 'PavedDrive',
            'LotFrontage',
            # この変数は時間変数を計算するためだけのものです。
            'YrSold']

# この変数は時間変数を計算するためのものです。
# 後で削除できます。
DROP_FEATURES = 'YrSold'

# 学習データにNAがある数値変数
NUMERICAL_VARS_WITH_NA = ['LotFrontage']

# 学習データにNAがあるカテゴリー変数
CATEGORICAL_VARS_WITH_NA = ['MasVnrType', 'BsmtQual', 'BsmtExposure',
                            'FireplaceQu', 'GarageType', 'GarageFinish']

TEMPORAL_VARS = 'YearRemodAdd'

# ログ変換する変数
NUMERICALS_LOG_VARS = ['LotFrontage', '1stFlrSF', 'GrLivArea']

# エンコードするカテゴリ変数
CATEGORICAL_VARS = ['MSZoning', 'Neighborhood', 'RoofStyle', 'MasVnrType',
                    'BsmtQual', 'BsmtExposure', 'HeatingQC', 'CentralAir',
                    'KitchenQual', 'FireplaceQu', 'GarageType', 'GarageFinish',
                    'PavedDrive']

NUMERICAL_NA_NOT_ALLOWED = [
    feature for feature in FEATURES
    if feature not in CATEGORICAL_VARS + NUMERICAL_VARS_WITH_NA
]

CATEGORICAL_NA_NOT_ALLOWED = [
    feature for feature in CATEGORICAL_VARS
    if feature not in CATEGORICAL_VARS_WITH_NA
]
