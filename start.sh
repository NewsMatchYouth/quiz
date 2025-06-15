#!/bin/bash
# 1) CGI スクリプトを FastCGI で動かす
spawn-fcgi -p 8000 -n /app/cgi-bin/deepfake_quiz.cgi &
# 2) 静的ファイル（HTML/画像）を Python HTTP サーバーで配信
python3 -m http.server 8001 --directory /app/quiz &
# 3) コンテナを停止させない
wait