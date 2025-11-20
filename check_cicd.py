"""
CI/CD チェック用のテストファイル

このファイルには意図的に以下の問題を含めています:
- Ruff linting issues
- Ruff formatting issues
- mypy type errors
"""

# Ruff linting issues
import os  # 未使用のインポート
import sys  # 未使用のインポート
from typing import List,Dict,Optional  # フォーマット問題: カンマの後にスペースなし


def bad_function_with_very_long_name_that_exceeds_the_line_length_limit_and_should_be_flagged_by_ruff(param1, param2, param3):
    """長すぎる関数名と行"""
    unused_variable = 10  # 未使用変数
    x=1+2  # フォーマット問題: 演算子の前後にスペースなし

    # 不要な比較
    if x == True:
        print("bad")

    return param1+param2+param3  # フォーマット問題


# mypy type errors: 型アノテーションなし
def no_type_annotations(a, b):
    return a + b


# mypy type error: 型の不一致
def type_mismatch() -> int:
    return "string"  # intを返すべきなのにstrを返している


# mypy type error: Noneの不適切な使用
def none_error(value: Optional[str]) -> str:
    return value.upper()  # valueがNoneの可能性があるのにチェックなし


# mypy type error: 引数の型が間違っている
def wrong_argument_type(numbers: List[int]) -> int:
    result = sum(numbers)
    return result


# 複数の問題を持つクラス
class   BadClass:  # フォーマット問題: クラス名の前に余分なスペース
    def __init__(self,name,age):  # mypy: 型アノテーションなし、フォーマット: スペースなし
        self.name=name  # フォーマット問題
        self.age=age
        self.unused_attr = "not used"  # 未使用属性

    def bad_method(self,x):  # mypy: 型アノテーションなし
        if x==None:  # フォーマット問題、比較問題
            return 0
        return x*2


# さらなる型エラー
def mixed_types(value):  # mypy: 型アノテーションなし
    if isinstance(value, int):
        return value + "string"  # 型の不一致
    return value


# 長すぎる行
very_long_dictionary = {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4", "key5": "value5", "key6": "value6"}


if __name__ == "__main__":
    # 不要な条件
    if True:
        print("This always runs")

    # 型エラーのある呼び出し
    result = wrong_argument_type(["a", "b", "c"])  # List[str]を渡しているがList[int]が期待される
    print(result)
