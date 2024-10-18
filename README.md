# Hurdle-Jumping-Algorithms-in-Python
In this repository, we explore several solutions to navigate hurdles using Python's Turtle graphics. Each file demonstrates a different scenario with varying obstacles and methods for solving the challenges.

# Files Overview
> **1. hurdle1.py**
- **Description:** Basic hurdle jumping solution using a combination of manual steps, for loops, and while loops.
- **Techniques Used:**
  - Defined functions for right turns and jumping.
  - Three different methods to clear a fixed number of hurdles (manual steps, loops, and while loops).
  
> **2. hurdle2.py**
- **Description:** Hurdle jumping where the goal is not known, and the program will continue until the goal is reached.
- **Techniques Used:**
  - The while not at_goal() loop ensures the turtle continues jumping until it reaches the finish line.
  - A simple jump function is used to bypass each hurdle.
  
> **3. hurdle3.py**
- **Description:** The turtle will only jump if a wall is detected in front. If no wall is present, it will simply move forward.
- **Techniques Used:**
  - Conditional checking for obstacles using if wall_in_front().
  - Jumping is triggered only when there's a wall in front, making the turtle movement more efficient.

> **4. hurdle4.py**
- **Description:** More complex hurdles where the turtle must navigate around walls by checking if there's a wall on the right or front.
- **Techniques Used:**
  - Defined jump function to handle complex obstacles by checking for walls on the right side.
  - Uses a while loop and multiple checks to intelligently navigate around walls.

# Code Breakdown
**Key Functions**
  - turn_right(): A helper function to perform a right turn by using three left turns.
  - jump(): The main function to guide the turtle over the hurdles.
  - while not at_goal(): This loop ensures the turtle continues until the goal is reached.

**Conditionals:**
  - if wall_in_front(): Checks if a wall is directly in front of the turtle.
  - while wall_on_right(): Checks if there is a wall on the right side.
