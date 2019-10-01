import numpy as np
from sklearn.model_selection import train_test_split

from regression_model import pipeline
from regression_model.processing.data_management import (
    load_dataset, save_pipeline)
from regression_model.config import config


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
