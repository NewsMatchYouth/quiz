#!/bin/bash
# deepfake_quiz.cgi — Bash CGI script for scoring the 5-image quiz
# place this file in cgi-bin/ and chmod 755 it

# 1) HTTP ヘッダー
echo "Content-Type: text/html; charset=UTF-8"
echo ""

# 2) 正解配列 (0=Real, 1=Fake)
ANS=(1 0 1 0 1)
score=0
total=${#ANS[@]}

# 3) GET パラメータから q1…q5 の値を取り出して採点
for i in $(seq 1 $total); do
  # sed で URLデコード抜き出し
  val=$(echo "$QUERY_STRING" | sed -n "s/.*q$i=\([^&]*\).*/\1/p")
  if [ "$val" = "${ANS[$((i-1))]}" ]; then
    score=$((score + 1))
  fi
done

# 4) 結果HTMLを出力
cat <<EOF
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Quiz Results</title>
  <style>
    body { font-family: sans-serif; max-width: 600px; margin: auto; padding: 2em; text-align: center; }
    .score { font-size: 2em; margin: 1em 0; }
    a.button { display: inline-block; padding: 0.6em 1.2em; background: #3366cc; color: #fff; text-decoration: none; border-radius: 4px; }
  </style>
</head>
<body>
  <h1>Your Quiz Results</h1>
  <p class="score">You scored <strong>$score</strong> out of <strong>$total</strong>.</p>
  <a class="button" href="/quiz/index.html">Try Again</a>
</body>
</html>
EOF