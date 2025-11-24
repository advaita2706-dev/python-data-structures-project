# Python Data Structures Project

Hey! This is my Python project for the Python Essentials course. Basically spent a good amount of time working through different data structures and algorithms to really understand how they work in Python.

## What's This About?

So for this project, I wanted to create something that shows I actually understand Python's core data structures - lists, tuples, dictionaries, sets, etc. Also threw in some algorithm implementations because they're pretty fun once you get the hang of them.

The idea was to build practical examples that demonstrate how these concepts work in real scenarios, not just theory stuff.

## Main Features

There are basically 4 main parts to this project:

### 1. Data Structure Implementations
- **List Operations**: sorting, searching, manipulation
- **Dictionary Management**: student records, grade tracking
- **Set Operations**: finding unique elements, set math
- **Tuple Usage**: immutable data storage

### 2. Algorithm Examples
- **Searching**: linear search, binary search
- **Sorting**: bubble sort, selection sort (implemented from scratch)
- **String manipulation**: reversing, palindrome checking

### 3. Practical Applications
- Student grade management system
- Contact book using dictionaries
- Inventory management with lists
- Data analysis with basic statistics

### 4. File Operations
- Reading/writing text files
- CSV data handling
- JSON data processing

## Tech Stack

- Python 3.x (obviously lol)
- No external libraries - just core Python
- Standard library modules only

## How to Run

1. Clone this repo
   ```bash
   git clone https://github.com/advaita2706-dev/python-data-structures-project.git
   cd python-data-structures-project
   ```

2. Run any of the Python files
   ```bash
   python data_structures_demo.py
   python algorithms_demo.py
   python student_management.py
   ```

3. Each file has example usage and output

## Project Structure

```
python-data-structures-project/
├── data_structures_demo.py    # Main data structures examples
├── algorithms_demo.py          # Algorithm implementations
├── student_management.py       # Practical application example
├── file_operations.py          # File I/O examples
├── utils.py                    # Helper functions
├── README.md
└── requirements.txt
```

## What I Learned

Honestly, understanding how Python handles mutable vs immutable data types was tricky at first. Took me a while to figure out why modifying a list inside a function affected the original list but integers didn't.

Also learned a ton about:
- List comprehensions (they're actually super useful once you get them)
- Dictionary methods and when to use them
- Time complexity - realized bubble sort is way slower than Python's built-in sort()
- File handling - had some issues with file paths initially

## Challenges Faced

- Debugging the binary search took longer than expected (kept getting index errors)
- Understanding Python's pass-by-reference vs pass-by-value behavior
- Making the code readable and well-documented
- Time management (should've started earlier tbh)

## Testing

Tested each module with different inputs to make sure they work properly. Test coverage is probably around 70-75% - didn't have time to write comprehensive unit tests but manually tested all the main functions.

## Future Improvements

If I had more time, I'd:
- Add more complex data structures (stacks, queues, linked lists)
- Implement more sorting algorithms
- Add unit tests using pytest
- Create a GUI using tkinter
- Add exception handling everywhere
- Better documentation with docstrings

## References

- Python official documentation
- Course lecture notes
- Stack Overflow (for debugging specific issues)

---

**Note**: This project was created for educational purposes as part of the Python Essentials course at VIT Bhopal.
