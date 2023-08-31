# 演習環境
本書では、演習にDockerコンテナを用います。

## 動かし方

```
$ docker compose up -d
```

## 各コンテナの情報

|概要 |IPアドレス                         |
|:--        |:--                        |
|BINDサーバ |10.8.9.2 |
|nginxサーバ |10.8.9.3 |
|PostgreSQLサーバ |10.8.9.4 |
|SSHサーバ |10.8.9.5 |
|Log4jサーバ |10.8.9.6 |
|ペンテスターの端末を模したコンテナ |10.8.9.7 |


## 謝辞
次のリポジトリを演習環境で使用させていただいております。
この場を借りてお礼申し上げます。

- https://github.com/knqyf263/CVE-2020-8617
- https://github.com/christophetd/log4shell-vulnerable-app