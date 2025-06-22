#!/usr/bin/env bash
# deepfake_quiz.cgi — your Bash CGI quiz scorer with detailed feedback

# 1) HTTP header (required for python3 -m http.server --cgi)
echo "Content-Type: text/html; charset=UTF-8"
echo ""

# 2) Configuration: correct answers and labels
ANS=(1 0 1 0 1)
LABELS=("Real" "Fake")
score=0
total=${#ANS[@]}

declare -a ANSWERS
# 3) Parse GET parameters into ANSWERS array and compute score
for i in $(seq 1 $total); do
  ANSWERS[$i]=$(echo "$QUERY_STRING" | sed -n "s/.*q$i=\([^&]*\).*/\1/p")
  if [ "${ANS[$((i-1))]}" = "${ANSWERS[$i]}" ]; then
    score=$((score + 1))
  fi
done

# 4) Emit result page HTML header
cat <<EOF
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Quiz Results</title>
  <style>
    body { font-family: sans-serif; max-width: 800px; margin: auto; padding: 2em; }
    .score { font-size: 2em; text-align: center; margin: 1em 0; }
    table { width: 100%; border-collapse: collapse; margin-top: 2em; }
    th, td { border: 1px solid #ccc; padding: 0.5em; text-align: center; }
    th { background: #f0f0f0; }
    .images img { max-width: 120px; height: auto; }
    .button { display: inline-block; margin: 2em auto; padding: 0.6em 1.2em; background: #3366cc; color: #fff; text-decoration: none; border-radius: 4px; }
  </style>
</head>
<body>
  <h1>Your Quiz Results</h1>
  <p class="score">You scored <strong>$score</strong> out of <strong>$total</strong>.</p>
  <h2>Details</h2>
  <table>
    <tr><th>Q</th><th>Your Answer</th><th>Correct Answer</th><th>Image</th></tr>
EOF

# 5) Loop through each question for detailed feedback
for i in $(seq 1 $total); do
  user=${ANSWERS[$i]}
  corr=${ANS[$((i-1))]}
  if [ "$user" = "$corr" ]; then
    icon="✔️"
  else
    icon="❌"
  fi
  echo "    <tr>"
  echo "      <td>$i $icon</td>"
  echo "      <td>${LABELS[$user]}</td>"
  echo "      <td>${LABELS[$corr]}</td>"
  echo "      <td><div class=\"images\"><img src=\"/quiz/static/face${i}.jpg\" alt=\"Face ${i}\"></div></td>"
  echo "    </tr>"
done

# 6) Close table and add retry button
cat <<EOF
  </table>
  <p style="text-align:center;"><a class="button" href="/quiz/index.html">Try Again</a></p>
</body>
</html>
EOF