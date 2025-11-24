"""Python Data Structures Demonstration

This module demonstrates various Python data structures including
lists, tuples, dictionaries, sets, and their common operations.

Author: Student Project
Course: Python Essentials
"""

# List Operations
def demonstrate_lists():
    """Demonstrate list operations and methods"""
    print("\n=== LIST DEMONSTRATIONS ===")
    
    # Creating lists
    numbers = [5, 2, 8, 1, 9, 3]
    fruits = ['apple', 'banana', 'orange', 'mango']
    
    print(f"Original list: {numbers}")
    
    # Sorting
    numbers_sorted = sorted(numbers)
    print(f"Sorted list: {numbers_sorted}")
    
    # List methods
    numbers.append(10)
    print(f"After append(10): {numbers}")
    
    numbers.insert(0, 99)
    print(f"After insert(0, 99): {numbers}")
    
    # List comprehension
    squares = [x**2 for x in range(1, 6)]
    print(f"Squares using comprehension: {squares}")
    
    return numbers

# Dictionary Operations
def demonstrate_dictionaries():
    """Demonstrate dictionary operations"""
    print("\n=== DICTIONARY DEMONSTRATIONS ===")
    
    # Student records
    students = {
        '001': {'name': 'Alice', 'grade': 85, 'courses': ['Math', 'Physics']},
        '002': {'name': 'Bob', 'grade': 92, 'courses': ['Chemistry', 'Biology']},
        '003': {'name': 'Charlie', 'grade': 78, 'courses': ['Math', 'CS']}
    }
    
    print("Student Records:")
    for student_id, info in students.items():
        print(f"  ID: {student_id}, Name: {info['name']}, Grade: {info['grade']}")
    
    # Dictionary methods
    average_grade = sum(s['grade'] for s in students.values()) / len(students)
    print(f"\nAverage Grade: {average_grade:.2f}")
    
    return students

# Tuple Operations
def demonstrate_tuples():
    """Demonstrate tuple operations (immutable)"""
    print("\n=== TUPLE DEMONSTRATIONS ===")
    
    # Creating tuples
    coordinates = (10, 20, 30)
    person = ('John Doe', 25, 'Engineer')
    
    print(f"Coordinates: {coordinates}")
    print(f"Person info: Name={person[0]}, Age={person[1]}, Job={person[2]}")
    
    # Tuple unpacking
    name, age, job = person
    print(f"Unpacked: {name}, {age}, {job}")
    
    return coordinates

# Set Operations
def demonstrate_sets():
    """Demonstrate set operations"""
    print("\n=== SET DEMONSTRATIONS ===")
    
    set_a = {1, 2, 3, 4, 5}
    set_b = {4, 5, 6, 7, 8}
    
    print(f"Set A: {set_a}")
    print(f"Set B: {set_b}")
    print(f"Union: {set_a | set_b}")
    print(f"Intersection: {set_a & set_b}")
    print(f"Difference (A-B): {set_a - set_b}")
    
    # Removing duplicates from list
    numbers_with_dupes = [1, 2, 2, 3, 4, 4, 5]
    unique_numbers = list(set(numbers_with_dupes))
    print(f"\nOriginal with duplicates: {numbers_with_dupes}")
    print(f"Unique numbers: {unique_numbers}")
    
    return set_a

# String Operations
def demonstrate_strings():
    """Demonstrate string manipulation"""
    print("\n=== STRING DEMONSTRATIONS ===")
    
    text = "Python Programming"
    
    print(f"Original: {text}")
    print(f"Uppercase: {text.upper()}")
    print(f"Reversed: {text[::-1]}")
    print(f"Length: {len(text)}")
    
    # Check palindrome
    def is_palindrome(s):
        s = s.lower().replace(' ', '')
        return s == s[::-1]
    
    test_word = "racecar"
    print(f"\n'{test_word}' is palindrome: {is_palindrome(test_word)}")
    
# Algorithm Demonstrations
def linear_search(arr, target):
    """Linear search implementation"""
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

def bubble_sort(arr):
    """Bubble sort implementation"""
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def demonstrate_algorithms():
    """Demonstrate searching and sorting algorithms"""
    print("\n=== ALGORITHM DEMONSTRATIONS ===")
    
    numbers = [64, 34, 25, 12, 22, 11, 90]
    
    # Search
    target = 25
    index = linear_search(numbers, target)
    print(f"Linear search for {target}: Found at index {index}")
    
    # Sort
    sorted_nums = bubble_sort(numbers)
    print(f"Original: {numbers}")
    print(f"Bubble sorted: {sorted_nums}")

# Main execution
def main():
    """Main function to run all demonstrations"""
    print("\n" + "="*50)
    print("PYTHON DATA STRUCTURES PROJECT")
    print("Demonstrating Core Python Concepts")
    print("="*50)
    
    # Run all demonstrations
    demonstrate_lists()
    demonstrate_dictionaries()
    demonstrate_tuples()
    demonstrate_sets()
    demonstrate_strings()
    demonstrate_algorithms()
    
    print("\n" + "="*50)
    print("All demonstrations completed!")
    print("="*50 + "\n")

if __name__ == "__main__":
    main()
