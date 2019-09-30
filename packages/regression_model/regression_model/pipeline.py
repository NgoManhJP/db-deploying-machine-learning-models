from sklearn.linear_model import Lasso
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler

# import preprocessors as pp
from regression_model import preprocessors as pp


# 学習データ内のNAを持つカテゴリ変数
CATEGORICAL_VARS_WITH_NA = [
    'MasVnrType', 'BsmtQual', 'BsmtExposure',
    'FireplaceQu', 'GarageType', 'GarageFinish'
]

TEMPORAL_VARS = 'YearRemodAdd'

# この変数は時間変数を計算するためのもので、後で削除できます
DROP_FEATURES = 'YrSold'

# ログ変換する変数
NUMERICALS_LOG_VARS = ['LotFrontage', '1stFlrSF', 'GrLivArea']

# 学習データ内のNAを持つ数値変数
NUMERICAL_VARS_WITH_NA = ['LotFrontage']

# エンコードするカテゴリ変数
CATEGORICAL_VARS = ['MSZoning', 'Neighborhood', 'RoofStyle', 'MasVnrType',
                    'BsmtQual', 'BsmtExposure', 'HeatingQC', 'CentralAir',
                    'KitchenQual', 'FireplaceQu', 'GarageType', 'GarageFinish',
                    'PavedDrive']


price_pipe = Pipeline(
    [
        ('categorical_imputer',
            pp.CategoricalImputer(variables=CATEGORICAL_VARS_WITH_NA)),
        ('numerical_inputer',
            pp.NumericalImputer(variables=NUMERICAL_VARS_WITH_NA)),
        ('temporal_variable',
            pp.TemporalVariableEstimator(
                variables=TEMPORAL_VARS,
                reference_variable=DROP_FEATURES)),
        ('rare_label_encoder',
            pp.RareLabelCategoricalEncoder(
                tol=0.01,
                variables=CATEGORICAL_VARS)),
        ('categorical_encoder',
            pp.CategoricalEncoder(variables=CATEGORICAL_VARS)),
        ('log_transformer',
            pp.LogTransformer(variables=NUMERICALS_LOG_VARS)),
        ('drop_features',
            pp.DropUnecessaryFeatures(variables_to_drop=DROP_FEATURES)),
        ('scaler', MinMaxScaler()),
        ('Linear_model', Lasso(alpha=0.005, random_state=0))
    ]
)
