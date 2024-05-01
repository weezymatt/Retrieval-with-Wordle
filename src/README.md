# Source Code
All files with the ```.py``` extension can be run in the terminal. Below you will see a brief description of which code to run. Each file asks the user for input about which word they would like to choose.

1. Benchmark v1 tests the naive implementation. You may run this code but it originally used to test the grade of the system.
   ```bash
   python3 benchmark_inv_index_v1.py
   ```
   
2. Benchmark v2 tests the default system and returns either the evaluation of the system or the solutions for a single letter.
   ```bash
   python3 benchmark_inv_index_v2.py
   ```
4. The main file allows you to play Wordle programmatically in the terminal and to debug the system. This is a fine option but we do recommend the player to instead go to [New York Times](https://www.nytimes.com/games/wordle/index.html) to play.
   ```bash
   python3 main.py
   ```
5. The improved implementation allows you to choose one word, all words, or random words to test against. We recommend choosing the one word option because the computational overhead is high running the model. Refer back to the main ```README.md``` for detailed information.
   ```bash
   python3 test_model_oneword.py
   ```
