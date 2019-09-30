import numpy as np
from sklearn.model_selection import train_test_split

from regression_model import pipeline
from regression_model.processing.data_management import (
    load_dataset, save_pipeline)
from regression_model.config import config

# PACKAGE_ROOT = pathlib.Path(__file__).resolve().parent
# TRAINED_MODEL_DIR = PACKAGE_ROOT / 'trained_models'
# DATASET_DIR = PACKAGE_ROOT / 'datasets'

# TESTING_DATA_FILE = DATASET_DIR / 'test.csv'
# TRAINING_DATA_FILE = DATASET_DIR / 'train.csv'
# TARGET = 'SalePrice'


# FEATURES = ['MSSubClass', 'MSZoning', 'Neighborhood', 'OverallQual',
#             'OverallCond', 'YearRemodAdd', 'RoofStyle', 'MasVnrType',
#             'BsmtQual', 'BsmtExposure', 'HeatingQC', 'CentralAir',
#             '1stFlrSF', 'GrLivArea', 'BsmtFullBath', 'KitchenQual',
#             'Fireplaces', 'FireplaceQu', 'GarageType', 'GarageFinish',
#             'GarageCars', 'PavedDrive', 'LotFrontage',
#             # この変数は時間変数を計算するためだけのものです。
#             'YrSold']


# def save_pipeline(*, pipeline_to_persist) -> None:
#     """パイプラインを保存する。"""

#     save_file_name = 'regression_model.pkl'
#     save_path = TRAINED_MODEL_DIR / save_file_name
#     joblib.dump(pipeline_to_persist, save_path)

#     print('saved pipeline')


def run_training() -> None:
    """モデルを学習する。"""

    # 学習データの読み込み
    data = load_dataset(file_name=config.TRAINING_DATA_FILE)

    # 学習データとテストデータを分割
    X_train, X_test, y_train, y_test = train_test_split(
        data[config.FEATURES],
        data[config.TARGET],
        test_size=0.1,
        random_state=0)  # ここにシードを設定しています

    # ターゲットを変換する
    y_train = np.log(y_train)
    y_test = np.log(y_test)

    pipeline.price_pipe.fit(X_train[config.FEATURES],
                            y_train)

    save_pipeline(pipeline_to_persist=pipeline.price_pipe)


if __name__ == '__main__':
    run_training()
