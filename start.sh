#!/bin/bash
#
# start.sh — CGI バイナリと静的ファイルサーバーを起動

# 1) fcgiwrap で CGI バイナリをポート8000で起動
spawn-fcgi -p 8000 -n /app/cgi-bin/deepfake_quiz.cgi &

# 2) Python HTTP サーバーで静的ファイル（index.html 等）をポート8001で起動
python3 -m http.server 8001 --directory /app/quiz &

# 3) コンテナが停止しないようプロセスを待機
wait