"""データベースコネクションへの参照を有するリポジトリレイヤーのベース.

特定のリソースに対しデータベース機能をカプセル化し、ロジックをアプリケーションから分離することを目的に用意。

ref. インフラストラクチャの永続レイヤーの設計 | Microsoft Docs
 https://docs.microsoft.com/ja-jp/dotnet/architecture/microservices/microservice-ddd-cqrs-patterns/infrastructure-persistence-layer-design
"""

from databases import Database


class BaseRepository:
    def __init__(self, db: Database) -> None:
        self.db = db
