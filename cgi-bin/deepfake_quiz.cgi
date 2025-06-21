# File: start.sh
#!/usr/bin/env bash
# start.sh — Launch Python built-in server in CGI mode

# Ensure the CGI script is executable
chmod +x cgi-bin/deepfake_quiz.cgi

# Start HTTP server on the port provided by Render (or default to 8000)
exec python3 -m http.server "${PORT:-8000}" --cgi


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

# 4) Output result HTML
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
