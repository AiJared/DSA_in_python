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

### Overview
1. Arrays
2. Linked Lists
3. What motivates us to build specific kinds of structures and pros and cons of those structures
by eploring four common operations, that is, <b>accessing a value, searching for a value, insearting a value and deleting a value</b>.
4. Circle back to algorithms and implement a <b>sorting algorithm</b>.

## Arrays
It is a common data structure built into nearly every programming langauage. Arrays can be used to represent a collection of values. They can also be used as building blocks to create even more custom data types and structures. In fact in most programming languages a text is repsented by a string type which is just a buch of characters stored in a particular order under an array. 

Before we go any further into array, let's first understand what exactly a data structure is.

A data structure is a way of storing data when programming.

It is the collection of values and the format they are stored in, the relationships between the values in the collection as well as the operations applied on the data stored in the structure.

An array is one of very many data structures. In general, an array is a data structure that stores a collection of values where each value is referenced using an index or a key.

A common analogy of thinking about arrays is that of train cars. Each car has a number and all cars are <b>ordered sequentially</b>. Inside each car there is some data stored in it. While this is a general representation of array, it can differ in some other languages but for the most part all these fundamentals remain the same.

In Swift and Java, arrays are <b>homogenous containers</b>, which means that they can only contain values of the same type. In Python, arrays are <b>heterogeneous structures</b>, they can store mixed kinds of values.

Regardless of the above nuance the fundamental feature of an array is <b>index</b>. This index value is used for every operation on the array, from accessing values, insearting, updating and deleting values.

In Python, the concept of arrays is a bit confusing. The type is mostly refered to by most languages as arrays, in Python it is best represented by the list type in Python. Python has a type called array but we are not going to use it now. While Python calls it a list, it can be used to carry out operations that can be carried out in arrays of other languages.

<b>Please Note that in computer science a list is a completely different data structure from the array and we will see the difference later on, generally though this structure is refered to us a linked list as opposed to just a list</b>.

Alright let's get back to arrays:

An array is a <b>contiguous</b> data structure. This means that an array is stored in blocks or memory that are beside each other without any gaps between them. The advantage of doing this is that retreiving values is very easy.

In a non-contiguous data structure, the structure stores a value as well as reference to where the next value is. To retreive that value, the languange has to follow that reference also called a <b>pointer</b> to the next block of memory. This adds some overhead which increases runtime of some common operations as we will see later.

Remember that arrays can either be homogeneous or heterogeneous, these choices also affects the memory layout of the array. For example in languages like C, Swift or Java where arrays are homogeneous, when an array is created, since the kind of value is already known to the compiler, it can choose a contiguous block of memory that fits the array size and values created. If an array contains integers, assuming that an integer took up space represented by one of the blocks, then for a five item array, the compiler can allocate five blocks of equally sized memory. In Python however, this is not the case, we can put any value in a Python list, there is no restriction. The way this works is a combination of contiguous memory and a pointer as mentioned above. When we create a list in Python, there is no information of what will go into that array which makes it difficult to allocate contiguous memory of equal size. 

There are several advantages to having contiguous memory, since values are stored right next to each other, accessing the values almost happens at contant time. The way Python gets around it, is by allocating contiguous memory and storing in it, not the values we want to store, but a reference or a pointer to a value that is stored somewhere else in the memory. By doing this it can allocate equally sized contiguous memory, since regardless to the size of the value, the size of the pointer referencing to that value is always going to be the same. This incurs an additional cost in that when a value is accessed, we need to follow the pointer to the block of memory where the value is actually stored but Python has ways of dealing with these costs which we will look at later on.

### Operations carried out on an array
Despite of a data structures you are working on, all data structures are expected to carry out four operations at minimum, these are:

1. Access and read values
2. Search for an arbitrary values
3. Insert values at any point into the structure
4. Delete values in the structure.

#### 1. Accessing values
Let's look at how these structures are implemented on arrays to some detail starting with access.

Elements in an array are identifies using a value known as an <b>index</b>. We use this index to access and read values in an array. Most programming languages follow a zero based numbering system when it comes to indexing an array. All this means is that the first index value is zero and not one. Generally speaking when an array is declared a base amount of contiguous memory is allocated as the array is stored. Computers refer to memory through the use of an <b>address</b>. 

Instead of keeping the reference to all the memory allocated for an array, the array only has to store the address of the first location. Because the memory is contiguous, using the base address, the array can calculate the address of any value by using the index position of that value as an offset.

Let's take a look at an example:

Let's say we want to create an array of integers and each integer takes a certain amount of space in memory which we will call <b>M</b>. Let's also assume we know how many elements we are going to create so the size of the array is some number of elements we call <b>N</b>. The total amount of space we need to allocate is <b>N * M</b>. If the array keeps track of the location where the first element is held, let's say <b>M0</b>, then it has all the information it need to find the locations of all the other values in the memory. 

When accessing a value in an array we use the index. To get the value of the array we use the 0 index, to get the second we use the index value 1 and so on.

Given that the array knows how much storage is need for each element, it can get the address of any element by starting off with the address of the first element and adding to that the index value value times the amount of storage per element. For example, to access the second value, we can start by M0, then to that add M times the index value 1 giving us M1 as the location in memory for the second address. This is simplified model but that is how more or less it works. It is only possible because of a contiguous memory locations with no gaps property.

#### 2. Searching
While arrays are fast at accessing values, they are pretty bad at searching. Taking an array as it is, the best way we can do is use linear search as a worst case linear runtime.

To search for an item in a list we can use one of two methods.

1. searching using an in operator
checks if a list contains an item. The in operator actually calls a contains method that is defined in a list type
which runs in a linear search operation.

2. In addition to this we can use a for loop to iterate over the list manually and
perform a comparison operation. This is more or less the implementation of linear search

If the array is sorted however, we can use binary search but because sort operations incur costs of there own languages usually stay away from sorting a list  and running binary search since for smaller arrays, linear search on its own may be faster.

#### 3. Inserting and Deleting values in an array
a. <b>Inserting</b>

In general most array implementations support three types of insert operations.

i. True insert

This makes use of an index value where we can insert an element anywhere in a list. This operation has a linear runtime.

Given this list [5, 1, 3, 2, 6]

Imagine if you had to insert an element 4 at the first position of the above list. 4 would take the first index value 0, 5 would move to the second position 1, 1 to index 2 and so forth until the last element 6 moves to index 5 making the new list to be [4, 5, 1, 3, 2, 6]. In a worst case screnario, inserting at the 0 position of an array, every single item in the array has to shifted forward and we know that any operation that involves iterating through every single item is a linear runtime.

ii. Appending

Though technically an insert operation that adds an item to an array, it doesn't incure runtime cost because it simply adds the item at the end. We can simply say that this is constant time operation but it also depends on the language implementation of the array.

To highlight why that matters, let's consider how lists in Python work. In Python when we create a list, the list doesn't know anything about the size of the list and how many items we are going to store.

Creating an empty list in Python gives it a space of one element by default but the list returns a length of 0 because it does not contain a value yet. This means that the list does not use memory allocation as an indication of it's size. An example list "numbers" demonstrates this in the file <b>arrays.py</b>. Okay so this list numbers currently has space for one element, now let's use
append method to insert a number at the end of the list.

Now the memory allocation and the size of the list are the same since the list
contains one element. Now when we try to add another element using the same append
method, first we should keep in mind that the list had only one space for one element
which was taken by 2, so here, it would have to allocate another space for our second
item and thereby the size of the list. It does this by calling list resize operation.

List resizing is quit interesting. Python doesn't resize the list just to accomodate the elements we want to add, instead in this case, it would allocate four blocks of memory to increase the size to a total of contiguous blocks of memory. It does this so that it does not have to add a memory everytime we add an element but at very specific points. The growth pattern of the list type in Python is <b>0,4,8,16,25,35,46...</b>. This means that as the list size approaches these specific values resize is called again. This may signify that append method has non-constant space complexity but it turns out that some operations don't increase space and others do. When you average all of them out, append operation takes constant space. We say that it has <b>Ammortized Constant Space Complexity</b>. 

This also happens with insert operations. If we had a four element array, we would have four elements and four memory allocations. An insert operation at that point, doesn't matter where it happens on the list, but at that point it would triger a reset. Inserting is still expensive though because after the resize, every element need to shifted over 1.

The last insert operation supported by most programming languages is the ability to add one list to another. In Python this is called an extend as demostrated in the arrays.py file.

iii. Extend
Extend takes another list to add, it effectively makes a series of append calls of each of the elements in the new list until all of them have been appended to the new list.

This operation has a runtime of <b>O(k)</b> where k represents the number of elements in the list that we are adding to our evisting list.

iv. Delete
Delete operation is similar to insert in that when an a delete operation occurs, the list needs to maintain correct index values. So where insert shifts every element to the right, delete operation shifts every element to the left. Just like insert as well, if we delete the first element in the list every single elememt in the list need to be shifted to the left.

Delete operations have an upper bound of <b>O(n)</b> also known as linear runtime.

## Linked List

Here we will work on building data structures. Before we get into linked lists, let me first explain why building data structures instead of just using those that come built into our languages is important. Each data structure solves a particular problem, on the basics of arrays above, we have looked at the common operations carried out and their costs. We found out that arrays are particularly good at accessing as reading values happends in constant time. But arrays are pretty bad at inserting and deleting, both of which run in linear time.

Linked lists on the other hand are somewhat better at this, although there are some caviets. If we are trying to solve a problem that involves more inserts and deletes that accessing, a linked list can be a more better tool than an array.

So what is a linked list?

A <b>linked list</b> is a linear data structure where each element in the list is contained in a separate object called a <b>node</b>. 

A node models two pieces of information; an individual item of the data we want to store, and a reference to the next node in the list. The first node in the linked list is called the <b>head</b> of the list and the last node of the list is called the <b>tail</b> of the list. The heads and the tail node are special because the list only maintans a reference to the head although in some implementations it keeps a reference to the tail as well.

Every node other than the tail, points to the next node in the list but tail doesn't point to anything, this is basically how we know the end of the list.

Nodes are what are called <b>self referential objects</b>. The definition of a node includes a link to another node. Self referential here means that definition of a node includes the node itself. 

Linked lists often comes in two forms:

i. <b>A Singly Linked List</b> - Where each node stores a reference to the next node in the list or

ii. <b>A Doubly Linked List</b> - Where each node stores a reference to both the node before and after.

Nodes are the building blocks for a list. The concept behind nodes is demonstrated in Python in the file 'linked_list.py", please check it out to learn more about it practically.

### Operations carried out on a linked list
As at this moment we can create an empty linked list but that's it. Next let's define a method to add data to our list.

#### Adding data to a linked list
There are three ways we can add data to our list. We can add node at the head of the list, meaning that the most recent node we created would be the head and the first node we created would be the tail or we can flip that around, the most recent node would be the tail and the first node would be the head.

One of the advantages of linked lists is that inserting data is more efficient that with arrays. This is true if we are inserting at the head or at the tail. Technically this isn't an insert, you would often here the method refered to <b>add</b>, <b>prepend</b> if the data is added to the head or <b>append</b> if the data is added to the tail. A true insert is when you can add data at any point in the list which is our third way of adding data and we will circle back to that later.

If we wanted to insert at the tail, then the list need a reference to the tail node otherwise we would have to start to the head and walk down the list to find the tail. Since our list only keeps a reference to the head we are going to add a new item to the head of the list.

Check out the implementation of <b>prepend</b> method whereby we add new data at the head changing the head and making the first node a tail at the file linked_list.py. 

So far we've only implemented a single method which functions much like the append method on an array except it adds it to the start of the linked list. Like append, this happens in constant time.

#### Searching through linked list
For the search operation, we are going to define a method that takes a value to search for and returns either the node containing the value if the value is found or None if it isn't.

Check out the implementation of search operation in the file linked_list.py.

#### Inserts and Deletes at Specific Points
Inserting on a linked list is quit interesting. Unlike in arrays where the index number of existing items needs to be shifted, with linked list we just need to change the references to next on a few nodes and we are good to go.

Since each node points to the next one, by swaping out these references we can insert a node at any point in the list at constant time. Much like binary search there is a catch, to find the node at that position you want to insert, you need to traverse the list and get to that point. 

We just implemented a search algorithm for the linked list type and we know that this runs in linear time. So while actually inserting is a fast, finding the position to insert is not. Let's see what this looks like in a code in the file linked_list.py but first let's understand something.

Imagine you have a linked list of 5 items, that is, [5]->[1]->[3]->[2]->[6] and we want to insert a node at position3. To insert a node at position 3 we need to modify the nodes at position 2 and 3. Node 2's next node attribute is going to point to the new node and the new node's next node attribute is going to point at node 3. In this way an insert operation is a constant time operation. We don't need to shift the whole list, we just need to modify a few references. In a doubly linked list, we can use node 3 to carry out both of these operations. Node 3 in a doubly linked list will have a reference to node 2 and we can use this reference to modify all the unnecessary links. Than a singly list though which is what we have in this example, if we kept decreasing position until we are at zero, we arrive at node 3, we can then set the new node's next attribute to point to node 3 but we have no way of getting a reference to node 2 which we also need. For this reason, it is just easier to decrease positions to just 1 when it equals 1 and stop at node 2.

Even though we can insert a new node without having the shift the rest, ultimately adding to either the head or the tail if you have a reference is much more efficient.

Removing nodes

Much like insert, removing a node is quite fast and it occurs in constant time. But to actually get to the node we need to remove, we need to traverse the entire list in our worst case. So in the worst case, this takes a linear time. Let us add this operation to our data structure in the file linked_list.py.

There are two ways we can define the remove method.

1. where we provide a key to remove as an argument and

2. where we provide an index.

In the former, the key refers to the data the node stores, so in order to remove that node we would need to search for the data that matches that key. In our code we will implement that first method.

## Merge Sort Algorithm
Let's take a look at how merge sort works conceptually by using arrays.

Let's start with an unsorted array [8 4 5 1 3 2 6 7]. The goal is to end up with an array sorted in ascending order.

Merge sort works like binary search but splitting up the problem into subproblems but it takes the process one step further.

On the first pass we are going to split the problem into two smaller arrays [8 4 5 1] [3 2 6 7]. On the next pass we are going to split them into further evenly sized arrays [8 4] [5 1] [3 2] [6 7]. We are going to keep doing this until we are down to single element arrays [8] [4] [5] [1] [3] [2] [6] [7].

After that the merge sort algorithm is going to work backwards, repeatedly merging those elements and sorting them at the same time. Since we start at the bottom, by merging two single element arrays, you only need to make a single comparison to sort the resulting merged array [4 8] [1 5] [2 3] [6 7]. By starting with smaller arrays that are sorted as it grows, merge sort has to make fewer sort operations than when it started at the end [1 4 5 8] [2 3 6 7] -> [1 2 3 4 5 6 7 8]. 

Solving a problem like this by recursively breaking down the problem into small subparts until it is easily solved it's an algorithmic strategy called <b>divide and conquer</b> 

Checkout the code in the file "merge_sort.py" to learn how the merge sort algorithm is implemented practically.