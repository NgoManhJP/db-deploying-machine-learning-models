import pandas as pd
from sklearn.externals import joblib
from sklearn.pipeline import Pipeline

from regression_model.config import config
from regression_model import __version__ as _version

import logging


_logger = logging.getLogger(__name__)


def load_dataset(*, file_name: str
                 ) -> pd.DataFrame:
    _data = pd.read_csv(f'{config.DATASET_DIR}/{file_name}')
    return _data


def save_pipeline(*, pipeline_to_persist) -> None:
    """パイプラインを保存
    バージョン管理されたモデルを保存し、以前に保存されたモデルを上書きします。
    これにより、パッケージが公開されたときに、呼び出せるトレーニング済みモデルが1つだけになり、
    そのビルド方法が正確にわかります。
    """

    # バージョン管理された保存ファイル名を準備する
    save_file_name = f'{config.PIPELINE_SAVE_FILE}{_version}.pkl'
    save_path = config.TRAINED_MODEL_DIR / save_file_name

    remove_old_pipelines(files_to_keep=save_file_name)
    joblib.dump(pipeline_to_persist, save_path)
    _logger.info(f'saved pipeline: {save_file_name}')


def load_pipeline(*, file_name: str
                  ) -> Pipeline:
    """保存されたパイプラインをロード"""

    file_path = config.TRAINED_MODEL_DIR / file_name
    trained_model = joblib.load(filename=file_path)
    return trained_model


def remove_old_pipelines(*, files_to_keep) -> None:
    """
    古いモデルのパイプラインを削除。
    これは、他のアプリケーションによってインポートおよび使用されるパッケージバージョンとモデルバージョンの間に
    単純な1対1のマッピングがあることを確認するためです。
    """

    for model_file in config.TRAINED_MODEL_DIR.iterdir():
        if model_file.name not in [files_to_keep, '__init__.py']:
            model_file.unlink()
