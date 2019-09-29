import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class CategoricalImputer(BaseEstimator, TransformerMixin):
    """sklearn imputerでカテゴリデータの欠損値を処理する。"""

    def __init__(self, variables=None) -> None:
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables

    def fit(self, X: pd.DataFrame, y: pd.Series = None) -> 'CategoricalImputer':
        """sklearnパイプラインに対応するステートメントを適合する。"""

        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        """変換を対象データフレームに適用する。"""

        X = X.copy()
        for feature in self.variables:
            X[feature] = X[feature].fillna('Missing')

        return X
