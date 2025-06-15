// deepfake_quiz.cpp
#include <iostream>
#include <vector>
#include <string>

struct Question {
    std::string path;  // 画像への相対パス
    int answer;        // 0 = Real, 1 = Fake
};

int main() {
    // --- 問題設定（5問） ---
    std::vector<Question> qs = {
        {"../quiz/static/face1.jpg", 1},
        {"../quiz/static/face2.jpg", 0},
        {"../quiz/static/face3.jpg", 1},
        {"../quiz/static/face4.jpg", 0},
        {"../quiz/static/face5.jpg", 1}
    };

    int score = 0;
    std::cout << "Deepfake Detection Quiz\n";
    std::cout << "For each image, enter 0 for Real or 1 for Fake.\n\n";

    for (size_t i = 0; i < qs.size(); ++i) {
        std::cout << "Question " << (i + 1) << ": Please open the image at `"
                  << qs[i].path << "` in a separate window.\n";
        std::cout << "Your answer (0=Real, 1=Fake): ";

        int choice;
        if (!(std::cin >> choice)) {
            std::cout << "Invalid input. Exiting.\n";
            return 1;
        }

        if (choice == qs[i].answer) {
            std::cout << "Correct!\n\n";
            ++score;
        } else {
            std::string correct_str = (qs[i].answer == 0 ? "Real" : "Fake");
            std::cout << "Incorrect. The correct answer is " << correct_str << ".\n\n";
        }
    }

    std::cout << "Your final score: " << score << " out of " 
              << qs.size() << ".\n";
    return 0;
}