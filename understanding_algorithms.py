# Understaning Algorithms
"""
An algorithm is a set of steps taken by a program to perform a task. 
"""

#Algorithmic Thinking
"""
In a real life senario we can use the game of thinking about a number and
letting someone try to predict the number we are thinking about, for example,
the number can be between 1 and 10, both 1 and 10 included. The steps that they
would take to get the correct number might vary from person to person because 
some might use steps that would get them to the correct answer quicker than others.

Some might start guesing the numbers from the beginning 1 and progress by adding 1 until
they get the correct number while some might start from a number in the middle say 5 then
determine how close they are to the correct number and adjust there thinking.

The one which will take fewer steps to the get to the correct answer is the winner as it is
the most effective strategy.

That is what is called algorithmic thinking.
"""

# Strategies used in the above example
"""
The strategies used in the above scenario are examples of search algorithms. The strategy
of starting from the beginning and adding one number after the other is called linear search
or sequential search or just simple search.
"""

# Example of an Algorithm (Linear Search)
"""
Linear search is defined by having a list of items with our target items amongst them then we start
to search for it from the beginnig of the list, progress through the list until we either find the
item we are searching for or run out of items.
"""

# What should an Algorithm be
"""
1. Clearly defined problem statement, input and output.
2. The steps in the algorith need to be in a very specific order
3. The steps also need to be distinct
4. The algorithm should produce a result.
5. The algorithm should complete in a finit amount of time.
"""

# Evaluating an algorithm
"""
An algorithm is evaluated through:
1. Correctness
2. Efficiency.
"""

# 1. Correctness
"""
An algorithm is deemed as correct if everytime we run it against all possible input
data we get an output we expect.

Part of correctness also means that for every possible input the algorithm should
always terminate/end.

If the above two are not met, then the algorithm is not correct.
"""

# 2. Efficiency
"""
Efficiency helps us solve a problem faster.

There are two measures when it comes to evaluating efficiency

1. Time and
2. Space.

Time complexity is the measure of how long it takes for a program
to run.

Space complexity - deals with the amount of memory taken up on the computer

Good algorithms need to measure between these two to be useful.
For example, if an algorithm is extremely fast but consumes more memoru than
you have available then it is not a good algorithm.

"""

# Metric of measuring Time and Space Complexities
"""
1. Running Time

The measure of the amount of time it took for an algorithm to run for a given set
of values. It is used to define time compexity.

The are three ways we can measure how well an algorithm does

a. Best Case Scenario - Happens when the algorithm takes less running time to complete the task 
b. Average Case Scenario - Is the average running time an algorithm takes to complete the task.
c. Worst Case Scenario - This is the maximum amount of time an algorithm can take to complete a task.

While going back to the real life scenario of thinking of a number and letting other people guess 
the correct number, we have already seen how Linear Search can be used to achieve, now let's see how
how another search algorithm can be used to achieve using even less time, that is, while looking at
time complexity.

Meet Binary Search

In the scenario, binary search can be implemented by guessing the number in the middle of the whole list
say 50 if the total number of the items in the whole list is 100 and our target number is 100.
The person would then ask if 50 is the target number then I'll tell him that the number provided is too low.
In this case the person will eliminate all the numbers from 1 to 50 because they are irrelevant. He will then
pick another number and keep on eliminating untill he reaches to 100 which is the target number.

Given that Linear Search requires trying out from the first number one all the way to the target number 100,
it would take a lot of time to reach to the target number than Binary Search which works by guessing a middle
number, then eliminating half of the numbers that are irrelevant to reaching the target number hence reaching
the target number faster.
"""

# Time Complexity
"""
We always want to evaluate how the algorithm performs in terms of the worst case scenario. This means that an 
algorithm that performs best will take less time when working on a larger set of data as compared to the other.
In this case, while liear search might perform best on a smaller set of data than binary search, when we choose
to increase the set of data to say 1000, it will take linear search 1000 tries while binary search just 10 tries.
Increasing further to 10000, linear search will take 10000 tries while binary search will take just 14 tries.
Ploting the performs on the Growth Rate graph of an algorithm will clearly show it.
Different algorithms grow at different rates and by ploting the order of growth rate, we get to see how the algorithm
grows when the number of sets increases.

This brings us to what is known as Big O

Big O
This is the theoretical definition of the complexity of an algorithm as a function of the size.

It is simply a notation used to describe complexity. An example of complexity written in terms of Big O looks like

O(n)

The O comes from "Order of magnitude of complexity." The complexity refers to the exercise of measuring the efficiency.

Complexity is a relative measure, which means that to measure complexity of an algorithm, we need to do it with comparison
to another algorithm.

With that in mind, Big O is a usefull notation for understanding both time and space complexities but only when
comparing among algorithms that solve the same problem.

The last bit (n) is the function of the size. This means that Big O meausers complexity as the input size increases.

Big O can also be referred to as the "Upper Bound" of the algorithm. This means that Big O also measures how the algorithm
performs in the worst case scenario.

Now these Big O notation variables for time compexity looks different in our two search algorithms that we have looked into so far, that is, Linear
Search and Binary Search respectively as shown below.
For Linear Search it is just "O(n)"
For Binary Search it is "O(log n)" - more on this later.

"""