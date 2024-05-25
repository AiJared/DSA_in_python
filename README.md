# Algorithms in Python

## Introduction to Algorithms

An algorithm is a set of steps taken by a program to perform a task. 

### Algorithmic Thinking

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

This is what is called 'algorithmic thinking'.

## Strategies used in the above example

The strategies used in the above scenario are examples of 'search algorithms'. The strategy
of starting from the beginning and adding one number after the other is called 'linear search'
or 'sequential search' or just 'simple search'.

## Example of an Algorithm (Linear Search)

Linear search is defined by having a list of items with our target items amongst them then we start
to search for it from the beginnig of the list, progress through the list until we either find the
item we are searching for or run out of items.

## What should an Algorithm be

1. Clearly defined problem statement, input and output.
2. The steps in the algorithm need to be in a very specific order
3. The steps also need to be distinct
4. The algorithm should produce a result.
5. The algorithm should complete in a finit amount of time.

## Evaluating an algorithm

An algorithm is evaluated through:
1. Correctness
2. Efficiency.

## 1. Correctness

An algorithm is deemed as correct if everytime we run it against all possible 'input'
data we get an 'output' we expect.

Part of correctness also means that for every possible input the algorithm should
always 'terminate/end'.

If the above two are not met, then the algorithm is not correct.

## 2. Efficiency

Efficiency helps us solve a problem 'faster'.

There are two measures when it comes to evaluating efficiency

1. Time and
2. Space.

'Time complexity' is the measure of how long it takes for a program
to run.

'Space complexity' - deals with the amount of 'memory' taken up on the computer

Good algorithms need to balance between these two to be useful.
For example, if an algorithm is extremely fast but consumes more memory than
you have available then it is not a good algorithm.

## Metric of measuring Time and Space Complexities

1. Running Time

The measure of the amount of time it took for an algorithm to run for a given set
of values. It is used to define time compexity.

There are three ways we can measure how well an algorithm does

a. Best Case Scenario - This is when the algorithm takes less running time to complete the task 
b. Average Case Scenario - Is the average running time an algorithm takes to complete the task.
c. Worst Case Scenario - This is the maximum amount of time an algorithm can take to complete a task.

While going back to the real life scenario of thinking of a number and letting other people guess 
the correct number, we have already seen how Linear Search can be used to achieve it, now let's see how 
another search algorithm can be used to achieve using even less time, that is, while looking at
time complexity.

Meet 'Binary Search'

In this scenario, binary search can be implemented by guessing the number in the 'middle' of the whole list
say 50 if the total number of the items in the whole list is 100 and our target number is 100.
The person would then ask if 50 is the target number then I'll tell him that the number provided is too low.
In this case the person will 'eliminate' all the numbers from 1 to 50 because they are irrelevant. He will then
pick another number in the middle of the remaining list and keep on eliminating untill he reaches to 100 which is 
the target number.

Given that Linear Search requires trying out from the first number one all the way to the target number 100,
it would take a lot of time to reach to the target number than Binary Search which works by guessing a middle
number, then eliminating half of the numbers that are irrelevant to reaching the target number hence reaching
the target number faster.

## Time Complexity

We always want to evaluate how the algorithm performs in terms of the worst case scenario. This means that an 
algorithm that performs best will take less time when working on a larger set of data as compared to the other.
In this case, while liear search might perform best on a smaller set of data than binary search, when we choose
to increase the set of data to say 1000, it will take linear search 1000 tries while binary search just 10 tries.
Increasing further to 10000, linear search will take 10000 tries while binary search will take just 14 tries.
Ploting the performs on the 'Growth Rate graph' of an algorithm will clearly show it.
Different algorithms grow at different rates and by ploting the order of growth rate, we get to see how the algorithm
grows when the number of sets increases.

This brings us to what is known as 'Big O'

'Big O'
This is the theoretical definition of the complexity of an algorithm as a 'function of the size'.

It is simply a 'notation' used to describe complexity. An example of complexity written in terms of Big O looks like

'O(n)'

The O comes from 'Order of magnitude of complexity'. The complexity refers to the 'exercise of measuring the efficiency'.

Complexity is a relative measure, which means that to measure complexity of an algorithm, we need to do it with comparison
to another algorithm.

With that in mind, Big O is a usefull notation for understanding both time and space complexities but only when
comparing among algorithms that solve the same problem.

The last bit '(n)' is the 'function of the size'. This means that Big O measures complexity as the 'input size increases'.

Big O can also be referred to as the 'Upper Bound' of the algorithm. This means that Big O also measures how the algorithm
performs in the worst case scenario.

Now these Big O notation variables for time compexity looks different in our two search algorithms that we have looked into so far, 
that is, Linear Search and Binary Search respectively as shown below.
For Linear Search it is just 'O(n)'
For Binary Search it is 'O(log n)' - more on this later.

## Common Complexities 

Each step in an algorithm has its own time and space complexity,in linear search for example there are multiple steps,start at the
beginning of the list and compare the current value to the target value, if our current value is the same as our target value then
we are done, if it's not, we will move on the next value and repeat step two. Step two is very important because there can be a situation
where we reach the end of the list and not get our target value. When at step two, we are reading the value to make a comparison in the
list. Reading a value is a single operation and if we were to plot it on a graph of 'Runtime per operations' against 'n', it would be a 
strait line that takes constat time regardless of n. Since it takes the same amount of time in any given case, we say that the runtime is
a 'constant time'.
In Big O notation, it would be represented as 'O(1)' which is read as 'constant time'. This means that reading values in a list is a constant
time operation.

Now let's look at it with respect to Binary Search Algorithm

While playing the game, we noticed that with every turn we were able to discard half of the data but there is another pattern that we did not
explore. Let's assume that the number of values is 10 and our target item is at 10, the number of tries we would make to reach our target value
would be 4. If we double our n to 20 and our target value at 20, we would make 5 tries and if then double n to 40 and our target value at 40 we
would make 6 tries. So from this we have noticed that everytime we double the number of values, the number of tries increases by 1.
There is a mathematical pattern to this problem called the 'logarithm of n' (log n). Binary search works the same as logarithms. For example,
given that our target value is 16 at a list of 16 values, using binary search we would start in the middle 8, then to 12 then to 14 then 15 then
finally 16 which is 5 tries or 'log2 of 16 + 1'. In general for a given value of n, the number of tries it takes to get the worst case scenario is
'log2 of n + 1'. And this pattern is a logarithmic pattern, we then can say that the runtime of such alorithms is 'logarithmic runtime'. Plotting
it on a graph of n against Tries, the graph is a curve and in Big O notation it is represented as 'O(log n)' or even sometimes as 'O(ln n)' and it
is read as 'logarithmic time'.

The graph, as n grows really large the number of tries grows slowly and eventually flattens out. Since the line in the graph of a logarithmic runtime
is below the linear search line, you might often here algorithms with logarithmic runtimes called 'sublinear'.

Sublinear runtimes are preferred to linear because they are more efficient but in practice, linear search has it's own advantages as well.

In Linear Search Algorithm, the number of operations required to get the target given a list n is the same as the total number of the list n if the 
target is the last item in the list. When the result in worst case scenario is almost the number of n, we say that the algorithm runs in 'Linear Time'.
This is represented as O(n) also read as 'linear time'.

The next Common Complexity you will come across is when an algorithm runs in 'Quadratic Time'. Quadratic means an operation is raised to the second power
or something is squared.

Let's say you and your friend are playing a 'tower defence game'. To start it off you are going to draw a map of a terrain, the map will be of a grid and
you'll pick a random number to determine how large this grid is going to be, let's say n = 4. Next you need to come with the list of coordinates so that you
place towers, enemies and other things. So how exactly can this be done, let's say you choose to start horizontally, you will have coordinates
((1,1), (1,2), (1,3), (1,4)) the you grow up verticall ((2,1), (2,2), (2,3), (2,4)), then((3,1), (3,2), (3,3), (3,4)) then finally the last one
((4,1), (4,2), (4,3), (4,4)). Notice a pattern here, for the range of values from 1 to n, for each value in that range, we create a point by combining that 
value with the range of values from 1 to n again. Doing this way for the range of values from 1 to n we create an n number of values and we end up with 16 points
which is also n^2 or n*n. This is an algorithm with quadratic runtime because for any given value of n we carry out n^2 number of operations. In English, this
is a 4 * 4 Grid. In Big O notation we would write this as O(n^2) or say that this is an algorithm with a 'Quadratic Runtime'. Many search algoritms have a worst
case quadratic runtime.

You may also encounter 'Cubic Runtime' as you work with different algorithms.

In such an algorithm for a given number of n, the algorithm executes n^3 number of operations. These aren't as common as the quadratic algorithms though. Plotting
quadratic and cubic runtimes on a graph of n against tries would look 'computationally expensive' because for any small changes in n there are pretty significant 
changes in the number of operations that we need to carry out.

The next worst case runtime we are going to look at is 'Quasilinear Runtime'.

It is easier to understand by starting with its Big O notation which is written as 'O(n log n)'. Remember that with O(log n) we saw that while n grew, there was only
a small change in the number of tries while in the quasilinear runtime, what we are saying is that for every value of n, we are going to execute a log n number of
operations hence a runtime of 'n times log n'. When you plot it in a graph, you will notice that the quasilinear runtime lies somewhere between a linear runtime and a
quadratic runtime. So where would we expect to find a quasilinear runtime in practical use? Well 'Sorting Algorithms' is definately one place you will see it.
'Merge Sort' for example is a sorting algorithm that has a worst case scenario of O(n log n). Here is an example, let's say we start of with a list of values that looks
like this [8,4,5,1,3,2,6,7], merge sort starts by splitting the list down the middle like this [8,4,5,1] and [3,2,6,7], it then takes each sublist and cuts it down the
middle again like this [8,4] [5,1] [3,2] [6,7], it keeps doing this until we end up with just a list of a single number [8] [4] [5] [1] [3] [2] [6] [7]. When we are down
to single numbers we can do one sort operation and merge the sublists back in the opposite direction. The first part of merge sort cuts those lists into sublists with half
the numbers. Then we carry out comparison operations so that we can sort those values and if you look at each step of the algorithm, we are carrying out an n number of
comparison operations and thus brings the worst case runtime of this algorithm to O(n log n) or 'Quasilinear Runtime'.

The runtimes we have looked at here are called 'Polynomial Runtimes'. An algorithm is considered to have a polynomial runtime if for a given value of n, its worst case value
is in the form of O(n^k) where k just means some value such as k = 2 (for quadratic runtime) k = 3 for a cubic runtime etc.

Algorithms with an upper bound or a runtime with a Big O value that is Polynomial, are considerd efficient algorithms and likely to used in practise.

Next let's look at algorithms that are considered to be inefficient. These algorithms are called 'Exponential Algorithms'.

With these runtimes, as the number of n increases slightly, their number of tries increases exponentially. These algorithms are far too computationally expensive to use.
An exponential runtime is an algorithm with a Big O value of some number raised to the nth power 'O(X^n)'. Imagine that you want to break into a locker that has a padlock on
it assuming that you forgot it's code, this lock takes a 2 digit code and the digit for code ranges from 0 to 9. You start by setting the dials to 00 and then while leaving
the first dial to 0, you set the second dial to 1 then try again, if it does not work you change it to 2 and try again. You'll keep on doing it and if you still haven't succeeded 
with the second then you go back to the first dial, change it to 1 and start working with the second dial again. The range of values you will have to go trough is from 00 to 99
which is 100 values. This can be generalized to 10^2 since there are 10 values on each dial raised to 2 dials. Searching trough each individual value until you reach to the correct
one is a strategy known as 'Brute Force'. Brute force algorithms have exponential runtimes. Here there are 2 dials so n = 2 and each has 10 values so then we can generalize this
algorithm as '10 ^ n' where n is the number of dials. The reason why this algorithm is so inefficient is because with just one more dial on the lock, the number of operations
increases siginificantly. With 3 dials, the number of combinations in the worst case scenario where the correct code is the last digit in the range is 10 ^ 3 or 1000 values. With
an increase in the number of n the number of operations increases exponentially to a point where it becomes unsolvable in a realistic amount of time.

The next class of Exponential Algorithms is best highlighted by a popular problem known as the 'Traveling Salesman'.

The problem statement goes like this; given a list of cities and the distance between each pair of cities, what is the shortest distance possible that travels each city and returns
to the origin city?

Now assuming that we have 3 cities A B and C, we have 6 possible routes, that is, A-B-C,A-C-B, B-A-C, B-C-A, C-A-B, C-B-A. From those 6 routes, we can determmine the shortest. If we
increase them to 4 cities we jump to 24 combinations. The mathematical explanation that defines this is called a 'Factorial' and it is written by 'n!'. Factorials are basically
n(n-1)(n-2)...(2)(1), that is n times n - 1 repeated until you reach one. For example the factorial of 3, 3!, is 3 * 2 * 1 = 6 which is the number of combinations we came up with for
3 cities, while the factorial of 4, 4!, is 4 * 3 * 2 * 1 = 24 which is number of combinations we came up with for 4 cities. 

In solving the travelling salesman problem, the most efficient algorithm will have a 'factorial/combinatorial runtime'. On low values of n algorithms of a factorial runtime may be used
with larger values like 200! it would take longer than humans have been alive to solve the problem.

Plotting the runtime on a graph, an algorithm that solves a problem with a factorial runtime has a worst case of O(n!). Studying exponential runtimes like this one are usefull for two reasons
1. In studying how to make those algorithms efficient, we develope strategies that are usefull across the board and can be potentially used to make even existing algorithms efficient.
2. It is important to be aware of problems that take a long time to solve, knowing right a way that a problem can take longer than realistic amount of time to solve, helps you focus on 
other aspects of the problem.

## How to Determine the Worst Case Complexities of Different Algorithms

Even though an algorithm has its own upper bound, each of its step has its own worst case complexity. 

Let's bring up the Binary Search algorithm again; assuming that the list is sorted, the first step is to determine the middle of the list, in general this is going to be a constant time
operation. Many programming languages hold on to information about the size of the list so don't have to walk through the list to actually know the size. Now if we didn't have information
about the size of the list, we would have to manually count through each item of the list until the end and this is a linear time operation but realistically this is a Big O of 1 'O(1)' or
a 'Constant Time'. Step two is to compare the element in the middle position to the target element. We can also assume that in most mordern programming languages this is a constant time
operation because the documentation for the language tells us that it is. Step three is our success case and the algorithm ends, this is our best case and so far we have only incurred two 
constant time operations. So we can therefore say that the best case for Binary Search Algorithm is a 'Constant Time'. Remember that the best case is not a usefull metric so step four if we
don't match is splitting the list into sublists, assuming the worst case scenario, the algorithm will keep splitting into sublists until a single is
reached with a value that we are searching for. The runtime for this step is 'logarithmic' since we are discarding half the values each time. So in this algorithms there are couple steps which
are constant time and one step which is logarithmic overall.

When evaluating the runtime for an algorithm, we say that the algorithm has as its upper bound, the same runtime as the list efficient step in the algorithm. With the Binary Search Algorithm
this means that it doesn't matter how fast we make the other steps because they are already as fast as they can be. In the worst case scenario, the splitting down to the single element list
is what will impact the overall runing time of the algorithm. This is why we say that the runtime of the algorithm in the worst case is O(log n)/logarithmic Runtime. 

### Binary Search Algorithm using Recursion
Binary search algorithm can also be recursive just like the one created in the <b>recursive_binary_search.py</b> file. This version of binary search algorithm implementents recursion whereby it is a function that calls itself. Let's try to use a real life example to explain this; Let's say that you have a book that contains answers to multiplication problems, you open up the book to solve your problem. In the book, the answer to your problem says "add 10 to the answer of problem 52". Okay you look at problem 52 and there it says "add 12 to the answer of problem 85". And finally when you go to problem 85, instead of redirecting you to somewhere else it tells you 10. So you go back to problem 52 and add 12 to 10 from problem 85, then you go back to the original problem where it says to add 10 to problem 52 so you add 10 to 22 and get 32 to end up with your finall answer. That is an example of <b>recursion</b>. The value of your answer needed a lookup in a book which required another lookup in the same book which required another lookup in the same book. The recursive binary search function works in a similar manner.

### Recursion and Space Complexity
A <b>recursive function</b> is the one that calls itself. A good example is the recursive binary search we created. The <b>recursive_binary_search</b> function called itself inside the body of the function. When writing a recursive function you always need a "stopping condition" and typically we always start the body of the recursive function with a stopping condition. It's common to call the stopping condition a <b>base case</b>.

In the recursive binary search function we created, we had two stopping conditions
1. What the function should return if the list is empty.
2. If the value at the midpoint is the same as the target, then we'll return True.

With the above two stopping conditions, we have covered all the possible paths of logic through the search algorithm, you can either find the value or you don't.

Once you have the base cases, the rest of the implementation of the recursive function is to call the function on smaller <b>sublists</b> until we hit one these base cases.

The number of times a recursive function calls itself is called a <b>Recursive Depth</b>.

The way we implemented binary search the first time is called an <b>iterative solution</b>. The word iterative means the solution was implemented using a loop structure of some kind.

A recursive solution on the other hand is the one that involves a set of stopping conditions and a function calling itself.

## Space Complexity
Space complexity is a measure of how much working storage or extra storage is needed as a particular algorithm grows.

Like time compexity, space complexity is also measured using worst case scenario using Big O notation. Let's take a look at an example.

Going back to our iterative implementation of binary search (in the file binary_search.py), let's take a look at what happens to our memory as n grows large. Let's say that we start off with a list of 10 elements. Inspecting the code we see that our solution relies heavily on two variables, that is, <b>first = 0</b> and <b>last = len(list) - 1</b>. First points to the start of the list and last points to the end.

When we eliminate a set of values we don't actually create a sublist, instead we just redefine first and last, as in the code, that is, <b>first = midpoint + 1</b> and/or <b>last = midpoint - 1</b> to point to a different section of the list. Since the algorithm only considers the values of first and last when determining the midpoint, by redefining first and last as the algorithm proceeds we can find the solution using just the original list. This means that for every value of n, the space complexity of the iterative version of binary search is constant or the iterative version of binary search takes <b>constant space</b>. Remember that we would write this as <b>O(1)</b>.

This may seem confusing because as n grows we need more memory to account for that larger list size, while this is true, that storage is not what space complexity cares about measuring, we care about the addition storage need as the algorithm runs as it tries to find the solution.

If we assume something simple, say that for a given size of a list represented by a value n, it takes N amount of space to store it then for the iterative version of binary search, regardless of how large the list is, at the start middle and the end of the algorithm process the amount of storage required does not get larger than N and this is why we consider it to run in constant space.

In the recursive version of binary search we don't use variables to keep track of which potion of the list we are working with, instead we create new list everytime with a subset of values or sublists with every recursive function call.

Let's assume we have a list of size n and in a worst case scenario the target value is the last in the list. Calling a recursive implementation of binary search on this list and target would lead to a scenario like this: The function will call itself and create a new list that goes from the midpoint to the end of the list, since we are discarding half of the list, the size of the sublist is <b>n / 2</b>. The function will keep calling itself, creating a new sublist that is half the size of the current list until it arrives at a single element list and a stopping condition.

Now because of the pattern that we have seen above, the runtime of a binary search is logarithmic. In fact the space complexity of the recursive version of binary search is the same. If we start off with a memory of size N that mactches the size of the list, on each function call of recursive binary search we need to allocate additional memory of N / 2, N / 4 and so on until we have a sublist that is either empty or contains a single value. Because of this we say that the recursive version of the binary search runs in logarithmic time with a O(log n). Now there is an important caviet here, this totally depends on the language. This is due to <b>Tail Optimization</b>, let me explain; if you think of a function as having a head and a tail, if the recursive function call is the last line of the function as it is in our recursive_binary_search function, we call this <b> Tail Recursion</b> since it is the last part of the function that call itself. Swift for example uses a trick to reduce the amount of space and therefore computing overhead to keep track of these recursive calls is called <b>Tail Call Optimization</b> or <b>Tail Call Elimination</b>

Python does not implement tail call optimization, so the recursive version of binary search takes logarithmic space. If we had to choose between the two implementations, given that time compexities of both are the same, we should definately go with the iterative implementation in Python since it runs in <b>constant space</b>.

# Data Structures in Python

## Introduction to Data Structures