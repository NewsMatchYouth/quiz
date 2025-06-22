#!/usr/bin/env bash
# deepfake_quiz.cgi — your Bash CGI quiz scorer

ANS=(1 0 1 0 1)
score=0
total=${#ANS[@]}


# -------------------------------
# File: cgi-bin/deepfake_quiz.cgi
#!/usr/bin/env bash
# deepfake_quiz.cgi — Bash CGI script for scoring the 5-image quiz
# Place this file in cgi-bin/ and chmod 755 it

# 1) HTTP header
echo "Content-Type: text/html; charset=UTF-8"
echo ""

# 2) Correct answers array (0=Real, 1=Fake)
ANS=(1 0 1 0 1)
score=0
total=${#ANS[@]}

# 3) Parse GET parameters q1…q5 from QUERY_STRING and score
for i in $(seq 1 $total); do
  # URL-decode and extract parameter value
  val=$(echo "$QUERY_STRING" | sed -n "s/.*q$i=\([^&]*\).*/\1/p")
  if [ "$val" = "${ANS[$((i-1))]}" ]; then
    score=$((score + 1))
  fi
done

# 4) Emit result HTML
cat <<EOF
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Quiz Results</title>
  <style>
    body { font-family: sans-serif; max-width: 600px; margin: auto; padding: 2em; text-align: center; }
    .score { font-size: 2em; margin: 1em 0; }
    .wrong-images img { max-width: 150px; margin: 0.5em; }
    a.button { display: inline-block; padding: 0.6em 1.2em; background: #3366cc; color: #fff; text-decoration: none; border-radius: 4px; }
  </style>
</head>
<body>
  <h1>Your Quiz Results</h1>
  <p class="score">You scored <strong>$score</strong> out of <strong>$total</strong>.</p>
EOF

# 5) Show wrong images (if any)
if [ $score -lt $total ]; then
cat <<IMG
  <h2>Images you got wrong:</h2>
  <div class="wrong-images">
IMG
  for i in $(seq 1 $total); do
    val=$(echo "$QUERY_STRING" | sed -n "s/.*q$i=\([^&]*\).*/\1/p")
    correct=${ANS[$((i-1))]}
    if [ "$val" != "$correct" ]; then
      echo "  <img src=\"/quiz/static/face${i}.jpg\" alt=\"Face ${i}\" >"
    fi
  done
cat <<END
  </div>
END
fi

# 6) Try again link & close HTML
cat <<EOF
  <a class="button" href="/quiz/index.html">Try Again</a>
</body>
</html>
EOF