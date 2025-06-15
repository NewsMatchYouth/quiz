#!/bin/bash
# deepfake_quiz.cgi — CGI wrapper for the C++ quiz binary

echo "Content-Type: text/plain; charset=UTF-8"
echo ""

DIR=$(dirname "$0")
exec "$DIR"/deepfake_quiz.bin