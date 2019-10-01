from regression_model.config import config

import pandas as pd


def validate_inputs(input_data: pd.DataFrame) -> pd.DataFrame:
    """モデル入力で処理できない値を確認"""

    validated_data = input_data.copy()

    # トレーニング中に見られないNAの数値変数をチェック
    if input_data[config.NUMERICAL_NA_NOT_ALLOWED].isnull().any().any():
        validated_data = validated_data.dropna(
            axis=0, subset=config.NUMERICAL_NA_NOT_ALLOWED)

    # トレーニング中に見られないNAのカテゴリ変数をチェック
    if input_data[config.CATEGORICAL_NA_NOT_ALLOWED].isnull().any().any():
        validated_data = validated_data.dropna(
            axis=0, subset=config.CATEGORICAL_NA_NOT_ALLOWED)

    # 対数変換された変数の値<= 0をチェック
    if (input_data[config.NUMERICALS_LOG_VARS] <= 0).any().any():
        vars_with_neg_values = config.NUMERICALS_LOG_VARS[
            (input_data[config.NUMERICALS_LOG_VARS] <= 0).any()]
        validated_data = validated_data[
            validated_data[vars_with_neg_values] > 0]

    return validated_data
