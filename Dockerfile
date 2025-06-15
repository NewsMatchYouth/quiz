# ベースに軽量な Debian を利用
FROM debian:bookworm-slim

# 必要パッケージのインストール
RUN apt-get update && \
    apt-get install -y g++ libc6-dev bash fcgiwrap spawn-fcgi && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# ソースと CGI スクリプトをコピー
COPY cgi-bin/ ./cgi-bin
COPY quiz/ ./quiz

# C++ バイナリをビルド
WORKDIR /app/cgi-bin
RUN g++ -std=c++17 -O2 deepfake_quiz.cpp -o deepfake_quiz.bin && \
    chmod 755 deepfake_quiz.bin deepfake_quiz.cgi

# fcgiwrap を使って CGI を起動するシェルスクリプトを用意
WORKDIR /app
COPY start.sh .

# ポートと起動コマンド
EXPOSE 8000
CMD ["bash", "./start.sh"]