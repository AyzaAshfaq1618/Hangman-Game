# Hangman-Game
A simple text-based hangman game in Python with 5 words and 6 wrong guess limit

A simple text-based hangman game implemented in Python where players guess a word one letter at a time.

 ## Game Overview

- **Word Bank**: 5 predefined words (apple, house, music, ocean, happy)
- **Maximum Wrong Guesses**: 6 incorrect attempts allowed
- **Interface**: Console-based text interface
- **Input**: Single letter guesses only

##  How to Play

1. The game randomly selects one word from the 5 predefined words
2. You see the word as underscores: `_ _ _ _ _` (length matches the secret word)
3. Enter one letter at a time to guess
4. **Correct guesses** reveal all instances of that letter in the word
5. **Wrong guesses** increase your mistake counter (max 6)
6. **Win** by revealing the complete word before reaching 6 wrong guesses
7. **Lose** if you make 6 incorrect guesses

##  Installation & Setup

### Prerequisites
- Python 3.x installed on your system

### Running the Game
1. Download the `hangman.py` file
2. Open terminal/command prompt
3. Navigate to the file location
4. Run the command:
   ```bash
   python hangman.py
   ```

## Game Rules & Features

- **Single Letter Input**: Only accepts one alphabetic character at a time
- **Case Insensitive**: 'A' and 'a' are treated the same (converted to uppercase)
- **Duplicate Prevention**: Already guessed letters don't count as wrong attempts
- **Input Validation**: Rejects numbers, symbols, or multiple characters
- **Progress Tracking**: Shows current word state, wrong guess count, and all guessed letters
- **Clear Feedback**: Tells you if your guess was correct or wrong

## Sample Gameplay

```
Welcome to Hangman!
Guess the word one letter at a time.
You can make 6 wrong guesses.

Word: _ _ _ _ _
Wrong guesses: 0/6
Guessed letters: 

Enter a letter: A
Good guess! A is in the word.

Word: A _ _ _ _
Wrong guesses: 0/6
Guessed letters: A

Enter a letter: E
 Wrong guess! E is not in the word.

Word: A _ _ _ _
Wrong guesses: 1/6
Guessed letters: A, E

Enter a letter: P
Good guess! P is in the word.

Word: A P P _ _
Wrong guesses: 1/6
Guessed letters: A, E, P
```

##  Technical Implementation

### Technologies Used
- **Language**: Python 3.x
- **Libraries**: `random` (standard library)
- **No external dependencies required**

### Key Programming Concepts Used
- **Random selection** using `random.choice()`
- **While loops** for main game flow
- **If-else conditions** for game logic and validation
- **String manipulation** and list operations
- **Input validation** and error handling
- **List comprehension** for word display

### Code Structure
```
├── Word list definition (5 words)
├── Random word selection and setup
├── Game state initialization
├── Main game loop with:
    ├── Display current progress
    ├── Get and validate user input
    ├── Check guess against secret word
    ├── Update game state
    ├── Check win/lose conditions
```

##  Game Features

- ✅ **Input Validation**: Ensures only single letters are accepted
- ✅ **Duplicate Detection**: Prevents counting repeated guesses as wrong
- ✅ **Case Handling**: Converts all input to uppercase for consistency
- ✅ **Progress Display**: Shows word progress, wrong guess count, and guessed letters
- ✅ **Clear Win/Lose Conditions**: Game ends appropriately with clear messages
- ✅ **Error Handling**: Handles invalid input gracefully

##  Game Statistics

- **Total Words Available**: 5
- **Average Word Length**: 5 letters
- **Maximum Attempts**: 6 wrong guesses
- **Input Method**: Single letter console input
- **Display Format**: Spaced underscore format (`_ _ _ _ _`)

##  Future Enhancements

- [ ] Add more words to increase variety
- [ ] Implement difficulty levels (word length based)
- [ ] Add ASCII hangman drawing for visual feedback
- [ ] Include word categories (animals, colors, etc.)
- [ ] Add scoring system based on remaining attempts
- [ ] Implement play again functionality
- [ ] Add hints feature
- [ ] Create word list file for easy expansion

## 🤝 Contributing

Feel free to fork this project and submit improvements! Some areas for contribution:
- Expanding the word list
- Adding new features
- Improving user interface
- Code optimization

## 📄 Code Structure Details

The game follows a clear structure:
1. **Setup Phase**: Import libraries, define word list, select random word
2. **Initialization**: Set up game variables and counters
3. **Game Loop**: Handle input, process guesses, update display, check conditions
4. **End Game**: Display win/lose message with the secret word

## 👨‍💻 Author

**Your Name**
- GitHub: AyzaAshfaq1618

## 📝 License

This project is open source and available under the MIT License.

---

⭐ **Perfect for Python beginners learning loops, conditionals, and string manipulation!** ⭐
