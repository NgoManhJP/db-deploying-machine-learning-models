import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class CategoricalImputer(BaseEstimator, TransformerMixin):
    """sklearn imputerでカテゴリデータの欠損値を処理する。"""

    def __init__(self, variables=None) -> None:
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables

    def fit(self, X: pd.DataFrame, y: pd.Series = None
            ) -> 'CategoricalImputer':
        """sklearnパイプラインに対応するステートメントを適合する。"""

        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        """変換を対象データフレームに適用する。"""

        X = X.copy()
        for feature in self.variables:
            X[feature] = X[feature].fillna('Missing')

        return X

class NumericalImputer(BaseEstimator, TransformerMixin):
    """数値欠損値の対応"""

    def __init__(self, variables=None):
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables

    def fit(self, X, y=None):
        # 辞書のpersistモード
        self.imputer_dict_ = {}
        for feature in self.variables:
            self.imputer_dict_[feature] = X[feature].mode()[0]
        return self

    def transform(self, X):
        X = X.copy()
        for feature in self.variables:
            X[feature].fillna(self.imputer_dict_[feature], inplace=True)
        return X


class TemporalVariableEstimator(BaseEstimator, TransformerMixin):
    """時間変数の計算機"""

    def __init__(self, variables=None, reference_variable=None):
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables

        self.reference_variables = reference_variable

    def fit(self, X, y=None):
        # sklearnパイプラインに適合するためにこのステップが必要
        return self

    def transform(self, X):
        X = X.copy()
        for feature in self.variables:
            X[feature] = X[self.reference_variables] - X[feature]

        return X


class RareLabelCategoricalEncoder(BaseEstimator, TransformerMixin):
    """まれなラベルのカテゴリカルエンコーダー"""

    def __init__(self, tol=0.05, variables=None):
        self.tol = tol
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables

    def fit(self, X, y=None):
        # 頻繁なラベルを辞書に保持する
        self.encoder_dict_ = {}

        for var in self.variables:
            # エンコーダーは最も頻繁なカテゴリーを学習
            t = pd.Series(X[var].value_counts() / np.float(len(X)))
            # 頻繁なラベル:
            self.encoder_dict_[var] = list(t[t >= self.tol].index)

        return self

    def transform(self, X):
        X = X.copy()
        for feature in self.variables:
            X[feature] = np.where(X[feature].isin(
                self.encoder_dict_[feature]), X[feature], 'Rare')

        return X


class CategoricalEncoder(BaseEstimator, TransformerMixin):
    """数値カテゴリカルエンコーダーへの文字列。"""

    def __init__(self, variables=None):
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables

    def fit(self, X, y):
        temp = pd.concat([X, y], axis=1)
        temp.columns = list(X.columns) + ['target']

        # 変換辞書の永続化
        self.encoder_dict_ = {}

        for var in self.variables:
            t = temp.groupby([var])['target'].mean().sort_values(
                ascending=True).index
            self.encoder_dict_[var] = {k: i for i, k in enumerate(t, 0)}

        return self

    def transform(self, X):
        # ラベルをエンコードする
        X = X.copy()
        for feature in self.variables:
            X[feature] = X[feature].map(self.encoder_dict_[feature])

        # トランスフォーマーがNaNを導入するかどうかを確認
        if X[self.variables].isnull().any().any():
            null_counts = X[self.variables].isnull().any()
            vars_ = {key: value for (key, value) in null_counts.items()
                     if value is True}
            raise ValueError(
                f'Categorical encoder has introduced NaN when '
                f'transforming categorical variables: {vars_.keys()}')

        return X


class LogTransformer(BaseEstimator, TransformerMixin):
    """対数変換器。"""

    def __init__(self, variables=None):
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables

    def fit(self, X, y=None):
        # パイプラインに対応するため
        return self

    def transform(self, X):
        X = X.copy()

        # 対数変換の値が負でないことを確認
        if not (X[self.variables] > 0).all().all():
            vars_ = self.variables[(X[self.variables] <= 0).any()]
            raise ValueError(
                f"Variables contain zero or negative values, "
                f"can't apply log for vars: {vars_}")

        for feature in self.variables:
            X[feature] = np.log(X[feature])

        return X


class DropUnecessaryFeatures(BaseEstimator, TransformerMixin):

    def __init__(self, variables_to_drop=None):
        self.variables = variables_to_drop

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # ラベルをエンコードする
        X = X.copy()
        X = X.drop(self.variables, axis=1)

        return X

