FROM debian:bookworm-slim

# Bash CGI と Python HTTP サーバー用のパッケージ
RUN apt-get update && \
    apt-get install -y \
      bash fcgiwrap spawn-fcgi \
      python3 && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# CGI スクリプトと静的ファイルをコピー
COPY cgi-bin/ ./cgi-bin
COPY quiz/   ./quiz
COPY start.sh .

# ポートを開ける
EXPOSE 8000 8001

CMD ["bash", "./start.sh"]