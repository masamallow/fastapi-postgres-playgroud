"""すべてのモデルで共有する共通ロジック.

    Base: 全リソースで共有する属性
    Create: 新しいリソースを作成する際に必須の属性
    Update: 更新することが可能な属性
    InDB: データベースから取得するリソースに存在する属性
    Public: GET, POST, PUTリクエストで返されるデータに存在する属性
"""

from pydantic import BaseModel


class CoreModel(BaseModel):
    pass


class IDModelMixin(BaseModel):
    id: int
