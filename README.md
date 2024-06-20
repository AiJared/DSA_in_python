# Algorithms in Python

## Introduction to Algorithms

An algorithm is a set of steps taken by a program to perform a task. 

### Algorithmic Thinking

In a real life senario we can use the game of **thinking about a number** and
letting someone try to *predict* the number we are thinking about, for example,
the number can be between 1 and 10, both 1 and 10 included. The steps that they
would take to get the correct number might vary from person to person because 
some might use steps that would get them to the correct answer quicker than others.

Some might start guesing the numbers from the *beginning* 1 for example, and progress by adding 1 until
they get the correct number while some might start from a number in the *middle* say 5 then
determine how close they are to the correct number delete *half the numbers* from the middle that are either less than or more than the correct number, adjust there thinking by repeating the same steps until they get the correct number.

The one which will take *fewer* steps to the get to the correct answer is the *winner* as it is
the **most effective strategy**.

This is what is called **algorithmic thinking**.

## Strategies used in the above example

The strategies used in the above scenario are examples of **search algorithms**. The strategy
of starting from the beginning and adding one number after the other is called **linear search**
or **sequential search** or just **simple search**.

### Example of an Algorithm (Linear Search)

Linear search is defined by having a list of items with our target items amongst them then we start
to search for it from the *beginning* of the list, progress through the list until we either find the
item we are searching for or run out of items.

## What should an Algorithm be

1. Clearly defined problem statement, input and output.
2. The steps in the algorithm need to be in a very **specific** order
3. The steps also need to be **distinct**.
4. The algorithm should produce a **result**.
5. The algorithm should complete in a **finit amount of time**.

## Evaluating an algorithm

An algorithm is evaluated through:
1. Correctness
2. Efficiency.

### 1. Correctness

An algorithm is deemed as correct if everytime we run it against all possible 'input'
data we get an 'output' we *expect*.

Part of correctness also means that for every possible input the algorithm should
always *terminate/end*.

If the above two are not met, then the algorithm is not correct.

## 2. Efficiency

Efficiency helps us solve a problem *faster*.

There are two measures when it comes to evaluating efficiency

1. Time and
2. Space.

**Time complexity** is the measure of how long it takes for a program
to run.

**Space complexity** - deals with the amount of *memory* taken up on the computer

Good algorithms need to balance between these two to be useful.
For example, if an algorithm is extremely fast but consumes more memory than
you have available then it is not a good algorithm.

## Metric of measuring Time and Space Complexities

### 1. Running Time

The measure of the *amount of time* it took for an algorithm to run for a given set
of values. It is used to define time compexity.

There are three ways we can measure how well an algorithm does

a. **Best Case Scenario** - This is when the algorithm takes *less running time* to complete the task. 
b. **Average Case Scenario** - Is the *average running time* an algorithm takes to complete the task.
c. **Worst Case Scenario** - This is the *maximum amount of time* an algorithm can take to complete a task.

While going back to the real life scenario of thinking of a number and letting other people guess 
the correct number, we have already seen how Linear Search can be used to achieve it, now let's see how 
another search algorithm can be used to achieve using even less time, that is, while looking at
time complexity.

Meet **Binary Search**

In this scenario, binary search can be implemented by guessing the number in the *middle* of the whole list
say 50 if the total number of the items in the whole list is 100 and our target number is 100.
The person would then ask if 50 is the target number then I'll tell him that the number provided is too low.
In this case the person will *eliminate* all the numbers from 1 to 50 because they are irrelevant. He will then
pick another number in the middle of the remaining list and keep on eliminating untill he reaches to 100 which is 
the target number.

Given that Linear Search requires trying out from the first number one all the way to the target number 100,
it would take a lot of time to reach to the target number than Binary Search which works by guessing a middle
number, then eliminating half of the numbers that are irrelevant to reaching the target number hence reaching
the target number faster.

## Time Complexity

We always want to evaluate how the algorithm performs in terms of the *worst case scenario*. This means that an 
algorithm that performs best will take less time when working on a larger set of data as compared to the other.
In this case, while liear search might perform best on a smaller set of data than binary search, when we choose
to increase the set of data to say 1000, it will take linear search 1000 tries while binary search just 10 tries.
Increasing further to 10000, linear search will take 10000 tries while binary search will take just 14 tries.
Ploting the performance on the **Growth Rate graph** of an algorithm will clearly show it.
Different algorithms grow at different rates and by ploting the order of growth rate, we get to see how the algorithm
grows when the number of sets increases.

This brings us to what is known as **Big O**

### Big O
This is the theoretical definition of the **complexity** of an algorithm as a *function of the size*.

It is simply a **notation** used to describe complexity. An example of complexity written in terms of Big O looks like

**O(n)**.

The O comes from **Order of magnitude of complexity**. The complexity refers to the **exercise of measuring the efficiency**.

Complexity is a relative measure, which means that to measure complexity of an algorithm, we need to do it with comparison to another algorithm.

With that in mind, Big O is a usefull notation for understanding both time and space complexities but only when
comparing among algorithms that **solve the same problem**.

The last bit **(n)** is the **function of the size**. This means that Big O measures complexity as the *input size increases*.

Big O can also be referred to as the **Upper Bound** of the algorithm. This means that Big O also measures how the algorithm performs in the worst case scenario.

Now these Big O notation variables for time compexity looks different in our two search algorithms that we have looked into so far, 
that is, Linear Search and Binary Search respectively as shown below.

For Linear Search it is just **O(n)**

For Binary Search it is **O(log n)** - more on this later.

## Common Complexities 

Each step in an algorithm has its own time and space complexity, in linear search for example there are multiple steps,start at the
beginning of the list and compare the current value to the target value, if our current value is the same as our target value then
we are done, if it's not, we will move on the next value and repeat step two. Step two is very important because there can be a situation
where we reach the end of the list and not get our target value. When at step two, we are reading the value to make a comparison in the
list. Reading a value is a **single operation** and if we were to plot it on a graph of **Runtime per operations** against **n**, it would be a 
**strait line** that takes **constat time** regardless of n. Since it takes the same amount of time in any given case, we say that the runtime is
a **constant time**.

In Big O notation, it would be represented as **O(1)** which is read as constant time. This means that reading values in a list is a *constant time operation*.

Now let's look at it with respect to Binary Search Algorithm

While playing the game, we noticed that with every turn we were able to discard half of the data but there is another pattern that we did not explore. Let's assume that the number of values is 10 and our target item is at 10, the number of tries we would make to reach our target value would be 4. If we double our n to 20 and our target value at 20, we would make 5 tries and if then double n to 40 and our target value at 40 we would make 6 tries. So from this we have noticed that everytime we *double the number of values*, the *number of tries increases by 1*.
There is a mathematical pattern to this problem called the *logarithm of n* **(log n)**. Binary search works the same as logarithms. For example, given that our target value is 16 at a list of 16 values, using binary search we would start in the middle 8, then to 12 then to 14 then 15 then finally 16 which is 5 tries or **log2 of 16 + 1**. In general for a given value of n, the number of tries it takes to get the worst case scenario is
**log2 of n + 1**. And this pattern is a logarithmic pattern, we then can say that the runtime of such alorithms is **logarithmic runtime**. Plotting it on a graph of n against Tries, the graph is a **curve** and in Big O notation it is represented as **O(log n)** or even sometimes as **O(ln n)** and it is read as **logarithmic time**.

The graph, as n grows really large the number of tries grows slowly and eventually flattens out. Since the line in the graph of a logarithmic runtime is below the linear search line, you might often here algorithms with logarithmic runtimes called **sublinear**.

Sublinear runtimes are preferred to linear because they are more efficient but in practice, linear search has it's own advantages as well.

In Linear Search Algorithm, the number of operations required to get the target given a list n is the same as the total number of the list n if the target is the last item in the list. When the result in worst case scenario is almost the number of n, we say that the algorithm runs in 'Linear Time'. This is represented as O(n) also read as **linear time**.

The next Common Complexity you will come across is when an algorithm runs in **Quadratic Time**. Quadratic means an operation is raised to the **second power** or something is squared.

Let's say you and your friend are playing a **tower defence game**. To start it off you are going to draw a map of a terrain, the map will be of a grid and you'll pick a *random number* to determine how large this grid is going to be, let's say **n = 4**. Next you need to come with the list of coordinates so that you place towers, enemies and other things. So how exactly can this be done, let's say you choose to start horizontally, you will have coordinates
((1,1), (1,2), (1,3), (1,4)) then you grow up verticall ((2,1), (2,2), (2,3), (2,4)), then((3,1), (3,2), (3,3), (3,4)) then finally the last one ((4,1), (4,2), (4,3), (4,4)). Notice a pattern here, for the range of values from 1 to n, for each value in that range, we create a point by combining that value with the range of values from 1 to n again. Doing this way for the range of values from 1 to n we create an n number of values and we end up with 16 points which is also n^2 or n*n. This is an algorithm with quadratic runtime because for any given value of n we carry out n^2 number of operations. In English, this is a **4 * 4 Grid**. In Big O notation we would write this as **O(n^2)** or say that this is an algorithm with a **Quadratic Runtime**. Many search algoritms have a worst
case quadratic runtime.

You may also encounter **Cubic Runtime** as you work with different algorithms.

In such an algorithm for a given number of n, the algorithm executes *n^3 number of operations*. These aren't as common as the quadratic algorithms though. Plotting quadratic and cubic runtimes on a graph of n against tries would look **computationally expensive** because for any small changes in n there are pretty significant 
changes in the number of operations that we need to carry out.

The next worst case runtime we are going to look at is **Quasilinear Runtime**.

It is easier to understand by starting with its Big O notation which is written as **O(n log n)**. Remember that with O(log n) we saw that while n grew, there was only a small change in the number of tries while in the quasilinear runtime, what we are saying is that for every value of n, we are going to execute a log n number of
operations hence a runtime of *n times log n*. When you plot it in a graph, you will notice that the quasilinear runtime lies somewhere between a linear runtime and a quadratic runtime. So where would we expect to find a quasilinear runtime in practical use? Well **Sorting Algorithms** is definately one place you will see it.
**Merge Sort** for example is a sorting algorithm that has a worst case scenario of O(n log n). Here is an example, let's say we start of with a list of values that looks like this [8,4,5,1,3,2,6,7], merge sort starts by splitting the list down the middle like this [8,4,5,1] and [3,2,6,7], it then takes each sublist and cuts it down the
middle again like this [8,4] [5,1] [3,2] [6,7], it keeps doing this until we end up with just a list of a single number [8] [4] [5] [1] [3] [2] [6] [7]. When we are down to single numbers we can do one sort operation and merge the sublists back in the opposite direction. The first part of merge sort cuts those lists into sublists with half
the numbers. Then we carry out comparison operations so that we can sort those values and if you look at each step of the algorithm, we are carrying out an *n number of comparison operations* and thus brings the worst case runtime of this algorithm to O(n log n) or **Quasilinear Runtime**.

The runtimes we have looked at here are called **Polynomial Runtimes**. An algorithm is considered to have a polynomial runtime if for a given value of n, its worst case value is in the form of **O(n^k)** where k just means some value such as k = 2 (for quadratic runtime) k = 3 for a cubic runtime etc.

Algorithms with an upper bound or a runtime with a Big O value that is Polynomial, are considerd efficient algorithms and likely to used in practise.

Next let's look at algorithms that are considered to be inefficient. These algorithms are called **Exponential Algorithms**.

With these runtimes, as the number of n increases slightly, their number of tries increases exponentially. These algorithms are far too computationally expensive to use.
An exponential runtime is an algorithm with a Big O value of some number raised to the nth power 'O(X^n)'. Imagine that you want to break into a locker that has a padlock on it assuming that you forgot it's code, this lock takes a 2 digit code and the digit for code ranges from 0 to 9. You start by setting the dials to 00 and then while leaving
the first dial to 0, you set the second dial to 1 then try again, if it does not work you change it to 2 and try again. You'll keep on doing it and if you still haven't succeeded  with the second then you go back to the first dial, change it to 1 and start working with the second dial again. The range of values you will have to go trough is from 00 to 99 which is 100 values. This can be generalized to 10^2 since there are 10 values on each dial raised to 2 dials. Searching trough each individual value until you reach to the correct one is a strategy known as **Brute Force**. Brute force algorithms have exponential runtimes. Here there are 2 dials so n = 2 and each has 10 values so then we can generalize this algorithm as *10 ^ n* where n is the number of dials. The reason why this algorithm is so inefficient is because with just one more dial on the lock, the number of operations increases siginificantly. With 3 dials, the number of combinations in the worst case scenario where the correct code is the last digit in the range is 10 ^ 3 or 1000 values. With an increase in the number of n the number of operations increases exponentially to a point where it becomes unsolvable in a realistic amount of time.

The next class of Exponential Algorithms is best highlighted by a popular problem known as the **Traveling Salesman**.

The problem statement goes like this; given a list of cities and the distance between each pair of cities, what is the shortest distance possible that travels each city and returns to the origin city?

Now assuming that we have 3 cities A B and C, we have 6 possible routes, that is, A-B-C,A-C-B, B-A-C, B-C-A, C-A-B, C-B-A. From those 6 routes, we can determmine the shortest. If we increase them to 4 cities we jump to 24 combinations. The mathematical explanation that defines this is called a **Factorial** and it is denoted as **n!**. Factorials are basically n(n-1)(n-2)...(2)(1), that is n times n - 1 repeated until you reach one. For example the factorial of 3, 3!, is 3 * 2 * 1 = 6 which is the number of combinations we came up with for 3 cities, while the factorial of 4, 4!, is 4 * 3 * 2 * 1 = 24 which is number of combinations we came up with for 4 cities. 

In solving the travelling salesman problem, the most efficient algorithm will have a **factorial/combinatorial runtime**. On low values of n algorithms of a factorial runtime may be used with larger values like 200! it would take longer than humans have been alive to solve the problem.

Plotting the runtime on a graph, an algorithm that solves a problem with a factorial runtime has a worst case of **O(n!)**. Studying exponential runtimes like this one are usefull for two reasons
1. In studying how to make those algorithms efficient, we develope strategies that are usefull across the board and can be potentially used to make even existing algorithms efficient.
2. It is important to be aware of problems that take a long time to solve, knowing right a way that a problem can take longer than realistic amount of time to solve, helps you focus on other aspects of the problem.

## How to Determine the Worst Case Complexities of Different Algorithms

Even though an algorithm has its own upper bound, each of its step has its own worst case complexity. 

Let's bring up the Binary Search algorithm again; assuming that the list is sorted, the first step is to determine the middle of the list, in general this is going to be a *constant time operation*. Many programming languages hold on to information about the size of the list so don't have to walk through the list to actually know the size. Now if we didn't have information about the size of the list, we would have to manually count through each item of the list until the end and this is a linear time operation but realistically this is a **Big O of 1 O(1)** or
a **Constant Time**. Step two is to compare the element in the middle position to the target element. We can also assume that in most mordern programming languages this is a constant time operation because the documentation for the language tells us that it is. Step three is our success case and the algorithm ends, this is our best case and so far we have only incurred two  constant time operations. So we can therefore say that the best case for Binary Search Algorithm is a **Constant Time**. Remember that the best case is not a usefull metric so step four if we
don't match is splitting the list into sublists, assuming the worst case scenario, the algorithm will keep splitting into sublists until a single value element list is reached with a value that we are searching for. The runtime for this step is **logarithmic** since we are discarding half the values each time. So in this algorithms there are couple steps which are constant time and one step which is logarithmic overall.

When evaluating the runtime for an algorithm, we say that the algorithm has as its upper bound, the same runtime as the least efficient step in the algorithm. With the Binary Search Algorithm this means that it doesn't matter how fast we make the other steps because they are already as fast as they can be. In the worst case scenario, the splitting down to the single element list is what will impact the overall runing time of the algorithm. This is why we say that the runtime of the algorithm in the worst case is **O(log n)/logarithmic Runtime**. 

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

Linked lists often comes in three forms:

i. <b>A Singly Linked List</b> - Where each node stores a reference to the next node in the list or

ii. <b>A Doubly Linked List</b> - Where each node stores a reference to both the node before and after.

iii. <b>Circular Linked List</b> - Where the last element points back to the first element.

### i. Singly Linked List
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

We have seen how those operations work on singly linked lists well, we have even talked about how they would work on doubly linked list but not looked at any implementations. Now let's see take a look at doubly linked lists and see how those operations are carried out in doubly linked list.

### ii. Doubly linked Lists

The nodes of a doubly linked list contain a data element and two links pointing to the next and previous node in the sequence. This makes operations suh as traversals, insertions and deletions more efficient because they can be done from and in both directions. We can easily traverse in forward and backward direction using the next and previous pointers respectively.

#### Representing a Doubly Linked List in Python

The representation of a doubly linked list in Python is different from the one we have seen above in a singly linked list. Check out the file <b>doubly_linked_list.py</b> to its representation.

#### Traversing in a Doubly Linked List in Python

Traversing a doubly linked list in Python is simple. You can start from the head of the list and iterate through each node while outputing its data.

To see how it is implemented, check out the file doubly_linked_list.py.

#### Insert Operation

Inserting a new node here is same as inserting new node in a singly linked list though it needs an extra operation that maintains the link of the previous node. There are four different ways of inserting a node in a doubly linked list.

i. At the beginnig of the list
ii. After a certain specified node
iii. Before a certain specified node
iv. At the end of the list

<b>i. Inserting at the beginnig</b>

Let's start by inserting at the beginnig of the list, it is quit simple and below are the steps.

- Create a new node with the given data
- Set the <b>next</b> pointer of the new node to point to the current head if it exists.
- Set the <previous> pointer of the new node to None because it is our new head now.
- If the list has data, update the <b>previous</b> pointer of the current head to point to the new node.
- Update the head of the list to point to the new node.

Check the file doubly_linked_list.py to see how this is implemented.

<b>ii. Inserting after a certain specified node</b>

A node can also be inserted after a given node in a doubly linked list. Below are the steps of inserting a node after a given node in a doubly linked list.

- Create a new node with the given data
- Set the <b>next</b> pointer of the new node to point to the next node of the given node.
- Set the <b>previous</b> pointer of the new node to given node.
- If the node of the given node id not None, update the <b>previous</b> pointer if that node to point to the new node.
- Update the <b>next</b> pointer of the given node to point to the new node.

Check out the implementation in Python in the file doubly_linked_list.py.

<b>iii. Insert before a certain specified node</b>

As we have done with inserting after a specified node, we can insert before a specified node as well. Below are the steps of inserting a node before a given specified node.

- Create a new node with the given data

- Set the next pointer of the new node to point to the given node.

- Set the previous pointer of the new node to point to the previous node of the given node

- If the previous node of the given node is not None, update the next pointer of that node to point to the new node.

- Update the previous pointer of the given node to point to the new node.

Check out it is implemented in Python in the file doubly_linked_list.py

<b>iv Inserting at the end</b>

As it is possible to insert a node at the beginning of the list, it is also possible to insert at the end of the list in Python. Below are the steps of inserting a node at the end of a doubly linked list.

- Create a new node with the given data
- If the list is empty, that is, head is None, then make the new node the head of the list.
- If not, traverse the list to find the last node.
- Set the next pointer of the last node to point to the new node.
- Optionally, update the ead of the list to point to the new node if it's the first node in the list.

Check the implement in Python in the file doubly_linked_list.py

#### Delete Operation

We've seen how to add nodes in a doubly linked list and we have learned that it can be done in four different ways. Deleting a node in a doubly linked list generally involves modifying the next and the previous pointers of nodes. Deletion can be done in the three ways:

- At the beginnig of the list
- At the end of the list
- At a given position in the list

And by list here I mean doubly linked list.

<b>1. Deletion at the beginning</b>

Below are the steps involved in deleting a node at the beginnig of a doubly linked list in Python.

- Check if the list is empty, that is, head is None. If it is empty, then there is nothing to delete.
- If the list has only one node, set the head to None to delete the node.
- Otherwise update the head to point to the next node.
- Set the previous pointer of the new node to None
- Optionally, free the memory allocated to the deleted node.

Check the implementation in Python in the file doubly_linked_list.py

<b>ii. Delete at a given position</b>

To delete a node at a given position in a doubly linked list in Python, you need to follow these steps:

- Check if the list is empty, that is, head is None, and if empty then there is nothing to delete
- If the position is less than 0, print an error message indicating that it's an invalid position.
- Traverse the list to find the node at the given position
- Update the next pointer of the previous node to skip the node to be deleted.
- Update the previous pointer of the next node to point to the previous node of the node to be deleted.
- Optionally, free the memory allocated to the deleted node.

Check out its implementation in the file doubly_linked_list.py

<b>iii. Delete at the end</b>

Well it is also possible to delete a node at the end of the doubly linked list in Python using the steps below.

- Check if the list is empty, that is, head is None. If it is empty, there is nothing to delete.
- If the list has only one node, set the head to None to delete the node.
- Traverse the list to find the last node.
- Set the next pointer of the second-to-last node to None.
- Optionally, free the memory allocated to the deleted node.

Check out the implementation in Python in the file doubly_linked_list.py

### iii. Circular Linked Lists

It is a variation of the standard linked list whereby in a standard linked list, the last node points to null, showing the end of the list. However, in a circular linked list, the last element points back to the first element, forming a loop.

Circular linked lists can be singly linked list or doubly linked list, meaning each node may have one or two pointers respectively. They can be used in various scenarios, such as representing circular buffers, round-robin scheduling algorithms and as an alternative to linear linked lists when operations involve wrapping around from the end to the beginning of the list.

Check out the representation of a circular linked list in the file circular_linked_list.py.

Now let's take a look at operations that can be carried out on a circular list.

#### Traversal of a Circular Linked List in Python

Traversing a circular linked list involves visiting each node of the list starting from the head node and continuing until the head node is encountered again.

Check out its implementation in Python in the file circular_linked_list.py.

The <b>Time Complexity</b> in our implementation is <b>O(N)</b> where N is the number of nodes in the list.

The <b>Auxiliary Space</b> is <b>O(1)</b>.

#### Insertion in a Circular Linked List

Nodes can be inserted in a circular list just as they can be inserted in a standard linked list and a doubly linked list as shown above. Just like in the doubly linked list, nodes can be inserted at different positions in the list. let's take a look at how nodes can be inserted at different positions in a circular list starting with at the head.

<b>1. Inserting a Node at the Beginning</b>

Follow the following steps to inset a node at the beginnig of a circular linked list.

- Create a new node with the given data
- If the list is empty, make the new node the head and point it to itself.
- Otherwise, set the next pointer of the new node to point to the current head.
- Update the head to point to the new node.
- Update the pointer of the last node to point to the new head, this helps maintain the circular structure.

Check out the implementation in Python in the file circular_linked_list.py

The <b>Time Complexity</b> of our implementation is <b>O(1)</b>.

The <b>Auxiliary Space</b> of our implementation is <b>O(1)</b>.

<b>ii. Inserting a Node at a Particular Position</b>

A node can also be inserted at a particular position in a circular linked list which we famously call the <b>index position</b>.

Below are the steps followed to insert a node at a particular index position in a circular linked list.

- Create a new node with given data.
- Traverse the list to find the node at the desired position (index - 1)
- Update the next pointer of the new node to point to the next node of the current node
- Update the next pointer of the current node to point to the new node.

Check out its implementation in the file circular_linked_list.py

The <b>Time Complexity</b> of our implementation is <b>O(N)</b>, where N is the number of nodes in the list.

The <b>Auxiliary Space</b> of our implementation is <b>O(1)</b>.

<b>Inserting a node at the end</b>

It is also possible to insert a node at the end of a circular linked list. Below are the steps of inserting a node at the end of the list

- Create a new node with the given data.
- If the list is empty, make the new node the head and point it to itself.
- Otherwise, traverse the list to find the last node.
- Set the next pointer of the last node to point to the new node.
- Set the next pointer of the new node to point back to the head( to maintain the circular structure).

The <b>Time Complexity</b> is <b>O(N)</b> where N is the number of nodes in the linked list.

The <b>Auxiliary Space</b> is <b>O(1)</b>.

#### Deletion in Circular Linked List

Well we have looked at inserting nodes in a circular linked list. We have seen that a node can be inserted at the beginning, at a specific position and at the end.

Let's now look at how we can delete a node from a circular linked list. Much like inserting, deleting a node can also be done at different positions of the list.

<b>i. Deletion at the beginning of the circular linked list</b>

The head of a circular linked list can be deleted. This operation would then make the next node that the head points to as the new head and the last node of the list would have to point back to this new head.

To delete the head of the list, follow the steps below.

- Check if the list is empty. If it is empty then there is nothing to delete.
- If the list is has only one node, set the head to None to delete the node.
- Otherwise, find the last node of the list(the node whose next pointer points to the head).
- Update the next pointer of the last node to point to the second node (head's next).
- Update the head to point to the second node.
- Optionally, free the memory allocated to the deleted node.

Check the implementation in Python in the file circular_linked_list.py.

The <b>Time Complexity</b> of deleting at the beginning of a circular linked list is <b>O(1)</b>.

The <b>Auxiliary Space</b> is <b>O(1)</b>

<b>ii. Deleting at a particular position in Circular Linked List</b>

You see just as it is possible to insert a node at a particular position in a circular linked list, deleting the same way can also be done. Use the steps below to delete a node at a particular position of a circular linked list.

- Check if the list is empty. If it is empty, then there is nothing to delete.
- If the position is 0, it means deleting the head node. In this case, update the next pointer of the last node to point to the second node and update the head.
- Traverse the list to find the node at the desired position (index - 1)
- Update the next pointer of the current node to skip the node to be deleted (pointing to the next node of the node to be deleted).
- Optionally, free the memory allocated to the deleted node.

The <b>Time Complexity</b> is <b>O(N)</b> where N is the number of nodes in the linked list.

The <b>Auxiliary Space</b> is <b>O(1)</b>.

<b>iii. Deleting at the end of a Circular Linked List</b>

Just like inserting a node at the end of the circular linked list, it is also possible to delete a node at the end of that very same list. So to delete at the end of the list, you need to follow the steps below.

- Check if the list is empty. If it is empty then there is nothing to delete.
- If the list has only one node, set the node to None to delete the node.
- Otherwise, find the last node of the list(the node whose next pointer points to the head)
- Update the next pointer of the last node to point to the second node (head's next).
- Update the head to point to the second node.
- Optionally, free the memory allocated to the deleted node.

Check out its implementation in the file circular_linked_list.py

The <b>Time Complexity</b> is <b>O(N)</b>.

The <b>Auxiliary Space</b>is <b>O(1)</b>.

## Merge Sort Algorithm
Let's take a look at how merge sort works conceptually by using arrays.

Let's start with an unsorted array [8 4 5 1 3 2 6 7]. The goal is to end up with an array sorted in ascending order.

Merge sort works like binary search but splitting up the problem into subproblems but it takes the process one step further.

On the first pass we are going to split the problem into two smaller arrays [8 4 5 1] [3 2 6 7]. On the next pass we are going to split them into further evenly sized arrays [8 4] [5 1] [3 2] [6 7]. We are going to keep doing this until we are down to single element arrays [8] [4] [5] [1] [3] [2] [6] [7].

After that the merge sort algorithm is going to work backwards, repeatedly merging those elements and sorting them at the same time. Since we start at the bottom, by merging two single element arrays, you only need to make a single comparison to sort the resulting merged array [4 8] [1 5] [2 3] [6 7]. By starting with smaller arrays that are sorted as it grows, merge sort has to make fewer sort operations than when it started at the end [1 4 5 8] [2 3 6 7] -> [1 2 3 4 5 6 7 8]. 

Solving a problem like this by recursively breaking down the problem into small subparts until it is easily solved it's an algorithmic strategy called <b>divide and conquer</b> 

Checkout the code in the file "merge_sort.py" to learn how the merge sort algorithm is implemented practically.

### The cost of running merge sort
If we go back to the top level, that is the merge sort function in the code, what is the runtime does the runtime look like and what about it's space complexity, how does the memory usage grow as the algorithm runs?

To answer those questions let's look at the individual steps starting with the <b>split function</b>. Here all we are doing is finding the midpoint of the list and splitting the list here. This seems like constant time operation but remember that the split function isn't called once, it is called as many times as we need it to, to go from initial list down to the single element list. This is a pattern we've seen a couple times now and we know that this runs in a <b>logarithmic runtime</b>.

Now the next step is the <b>merge operation</b>. Remember that we have broken the list down to a single element list so we need to merge the elements back while sorting them. For a list of size <b>n</b> we will always have to make n number of merge operations to get back from a single element list to a list of sorted elements. This makes the overall runtime O(n log n) because in the n number of merge steps multiplied by log n number of merge splits.

There is a caviet in the split operation part of the merge sort algorithm we have implemented in our code. If you take a look at the split function, you will notice that we are carrying out slice operation on our list. If you go and check at the Python documentation, you will notice that a slice operation is not a constant time operation, infact it is has a runtime of <b>O(k)</b> where k represents the slice size. This means that the implementation of slice in the split function we created does not run in logarithmic time but in O(k log n) time, that is, k times logarithmic time because there is a slice operation for each split.

This means that our implementation is much more expensive so that makes or overall top merge sort function runtime not O(n log n) but O(kn log n) which is again much more expensive.

To fix it, we would need to remove the slicing operation. In the introduction to algorithms part we looked at two implementations of binary search, a recursive one and an iterative one. In the recursive one we used list slicing with every recursion call, we achieved a similar result using an iterative call without using list slicing. Over there we declared two variables to keep track of starting and ending positions in the list. We could rewrite merge sort to do the same. <b> Do it as an exercise</b>.

Although our implementation is a bit more expensive the overall runtimes of merge sort are as follows:

i. merge step - linear time, that is, O(n)

ii. split step - logarithmic time, that is, O(log n) and

iii. Overall - O(n log n) 

and that is how merge sort actually works.

Now let's take a look at it's <b>Space Complexity</b>

The merge sort algorithm takes <b>linear space</b>. Let me explain. If we start splitting our list from the beginning until we reach to a single item list, each of these new lists takes a certain amount of space say, n for the whole list, n/2 for the second list etc. This might seem that the sum of all this space is the additional space needed for merge sort but that's not actually the case. In reality there are two factors that make a difference.

i. Not every single one of this sublists are created simultaneously.

At step two we create two n/2 sublists. When we move to the next step however, we don't hold on to n/2 and then 4 n/4 sublists for the next split, instead after the 4 n/4 sublists are created, the n/2 are deleted from the memory because there is no reason to hold unto them any longer.

ii. Our code doesn't execute every part simultaneously.

Think of it this way, when we pass our code to the top merge sort function, our implementation calls split which returns the <b>left half</b> and the <b>right half</b>. The next line of code then calls merge sort on the left half again. This runs the merge sort function again with a new list. In that second run of the function split is run again we get a send left and right half and then again like before we call merge sort on the current left half. What this means is that code walks down the left path all the way down first until the initial left half is sorted and merged back into one array. Then it is going to walk the right path all the way down and sort that until it we are back to that first split with 2 n/2 sized sublists.

Esentially we don't run all these paths of codes at once so the algorithm does not need additional space for sublists infact it is the very last step that matters. In the last step, the two sublists are merged back while being sorted until the last list with sorted values is returned. That sorted list has an equal number of items as the original unsorted list. And because this is a new list, it means that at most the additional space the algorithm will require at a given time is n. Yes at different points in the algorithm we require log n amount of space but log n is smaller than n and so we consider merge sort to have a <b>Linear Space Complexity</b> because that is the overall factor.

A true implementation of merge sort runs in quasilinear or log linear time, that is n times log n.

In our implementation of merge sort, we implemented a problem, if we go to the split operation, the bottleneck here, like list slicing, is splitting the linked list at the midpoint. Going back to our implementation "in the file linked_list_merge_sort", we can see that we use the node at index method, which finds the node we want by traversing the list. This means that every split operation incurs a O(k) cost where k here is the midpoint of the list effectively n/2 because we have to walk down the list counting up the index until we get to that node. Given that overall splits take logarithmic time, our split function just like the one we wrote earlier, incurs a cost of O(k log n).

# Sorting and Searching Algorithms

## Sorting Algorithms

Suppose we have a list of names, this list might be huge,like hundred thousand names of people and we need to lookup a specific name. Let us assume that there isn't an existing function to perform the task or if it exists, it doesn't suit our purpose well. For unsorted list, our option may be to use <b>linear search</b>. As you saw in the introduction to algorithms, with linear search you have to go through all the list every single time while not doing anything to narrow down the search each time. If you are searching down a huge list this might take a lot of time which might not be available most of the time.

That might be the reason why another search algorithm might be efficient for the task, <b>binary search</b>. It is efficient because it as we discusses earlier it works by letting us get rid or half of the list each time it searches for our target value from the middle of the list. However, it does this by requiring that the list of values be sorted so we need to sort the list first.

So let's look at sorting algorithms. To start off we will look at sorting numbers first as it is a bit easier than sorting strings then we will look at sorting strings later.

### Bogo Sort

This sorting algorithm randomizes the order of the values in the list repeatedly until it is sorted.

It is a very inefficient algorithm because it has to make attempts randomizing the order of values in the list over and over and again until when the list is sorted. For this reason, the number of attempts it can take varries and it can surprisingly take a lot of attempts for it to sort values of just a small list. This means that it does not make any progress towards sorting the items in each attempt it makes. Given a huge list, bogo sort would not be very helpful.

Check out the implementation of bogo sort in the file "bogo_sort.py".

### Selection Sort

It is still a slow sorting algorithm but at least each pass brings us closer to completion. Our implementation of selection sort is going to use use two arrays, an unsorted array and a sorted one. The sorted list starts out empty but we will be moving values from the unsorted list to the sorted list one at a time.

With each pass, we will look through the unsorted array, take the smallest value and move it to the sorted array. We will start by the first value in the array and mark it as the minimum value, then move to the next value in the array and mark it as minimum again, we will keep on doing that until we reach the end of the array and at that point we will have known what the minimum value of all the values in the unsorted array is and take it. Now here is the part that makes selection sort better than bogo sort, after noting the minimum value in the unsorted list, we then move it to the end of the sorted list. So that value won't be part of the unsorted list so we won't need to look for it anymore.

We will repeat the above steps again with the remaining values in the unsorted list, pick the minimum value and move it again to the end of the sorted list. We will keep on doing that untill there are no values in the unsorted array and we have sorted all values in the sorted array. 

Check the implementation of selection sort in the file "selection_sort.py".

Now there is no doubt that selection sort works way better than bogo sort but in our implementation we have used smaller arrays, however in real life, you would mostly be handling lists with hundreds of thousands of values or even millions. Well dealing with that kind of array can take a lot of time.

You can assess the time it takes for the selection sort to run a given list by using the command <b>time python selection_sort.py 5.txt</b>.

The next sorting algorithms rely on <b>recursion</b>, which is the ability of a function to call itself. But let us first begin by understanding how recursive functions work.

<b>Recursive Functions</b>

Let's suppose we need to write a function that adds together all the numbers in an array. Normally, we'd probably use a loop for this sought of operation. We can create a function that takes in numbers, inside the function declare a variable total assign zero to it. The loop over the numbers as we add them to total until we reach the end of the list then at the end return the total. It works perfectly.

But we can do it using recursion as demonstrated in the file <b>recursion.py</b>. But note that recursion is not the most efficient way to add a list of numbers. But this is a good problem to use to demonstrate recursion because it is so simple. The example code that demonstrates recursion is going to make the use of Python <b>slicing</b>. Remember that a slice is a way to get a series of values from a list.

### Quick Sort

We've seen bogo sort which doesn't make any progress in sorting items towards each pass. We've also seen selection sort which moves one value over to a sorted array on each pass so that it has fewer items to compare each time.

<b>Quick sort</b> speeds up the process further but reducing the number of comparisons it makes. This algorithm relies on recursion. To implement it, we'll write a recursive function as demonstrated in the file <b>quicksort.py</b>

Now here is how the algorithm works. Suppose we load the numbers from our 8.txt file onto a list [4,6,3,2,9,7,3,5]. How do we divide it? It would probably be smart to have quick sort function divide the list in a way that brings it closer to being sorted. So we will pick an item from the list, say the first item 4. We will call this value we have picked the <b>pivot</b>. 

We will then break the list into two set of sublists. The first sublist will contain items that are smaller than the pivot, that is, [3,2,2] and the second set will contain items that are greater than the pivot, that is [6,9,7,5] respectively. These two sublists are not sorted but what if they were, we could just join the sublists with our pivot and end up with a sorted list, so how do we sort the sublists?

The sublists are sorted by calling a quick sort recursively on them. This implements the <b>divide and conquer technique</b>.

So for our first sublist, we pick the first item as the pivot again in this case [3]. We then break the list into sublists, one with everything less than the pivot and one with everything greater than the pivot as [2, 3] and []. Notice that there is a value that is equal to the sublist that get's put in the less than sublist. Also note that there are no values in the greater than sublist and that is okay. We still have one sublist that still has more than one element long so we call our quick sort on that too. We can clearlly see that it is already sorted but the computer does not know that so it will call it anyway. It picks the first element [2] as the pivot, there are no elements less than the pivot and only one element greater than the pivot [3]. That's it for the recursive case, we finally hit the base case for our quick sort function. It will be called both on the the list with no elements and the list with one element but both of the pivot [2] and the element greater than it [3] will be returned as they are [2, 3] because there is nothing to sort. So now at the level of the call stack above this, the returned sorted lists are used in the place of the unsorted sublist that is lest than the pivot and the unsorted sublist that is greater than the pivot. They are then joined together into one sorted list [2, 3, 3]. Remember that the empty list get's discarded then at the level of the call stack above that, the returned sorted lists are used in the place of the unsorted lists there, again, they were already sorted but the quick sort method was called on them anyway. The sublists are joined together into one sorted list. At the call stack level above that, the returned sorted list is used in place of the unsorted list that is less than the pivot. So now that is less than or equal to the pivot [4] is sorted.

Now we call quick sort on the sublist that is greater than the pivot [4] and the process repeats for that sublit. We pick the first element [6] as the first pivot and split the remaining elements into sublists that are less than and greater than the pivot as [5] and [9, 7] respectively. We then call quick sort function onto those elements recursively until they are sorted. Eventually your sorted sublist is returned on the first quick sort function call. We combine the sublists that are less than or equal to the pivot,[2,3,3], the pivot itself, [2,3,3,4] and for the sublist that is greater than the pivot [2,3,3,4,5,6,7,9] into a single list and because we recursively sorted the list, the whole list is sorted. So that is how the quick sort function is going to work. Take a look at how it is implemented in the code in the file <b>quicksort.py</b>.

From the implementation of quick sort we can clearly see that it is faster than the previous sorting algorithms we have used so far in this section. It is way better and faster than bogo sort and selection selection sort algorithms.

### Merge Sort

Now we have already looked at merge sort algorithm in fact in details before but since we are understanding sorting algorithms let's look at it one more time shall we?

Now both merge sort and quick sort are recursive algorithms. The difference comes in how they actually work, quick sort works by taking a pivot value then splitting the rest of the list based on values that are less than the pivot and those that are greater than the pivot. Merge sort on the other hand merge sort works by splitting the list into halves recursively then sorts the halves as it merges them back.

In the file <b>mergesort.py</b> I have made another merge sort algorithm that I would recommend that you check it out because you might find it to be easier to understand than the previous one in the file <b>merge_sort.py</b> file.

Now comparing the time all the sorting algorithms we have looked at here using the command <b>time python algorithm.py list.txt</b> whereby algorithm is the file of the algorithm running and list.txt is the list of values being sorted, proves that selection sort is the slowest algorithm despite it being the easiest to understand. Quick sort is a bit faster than merge sort but merge sort is still good.

## Big O Notation

Developers who need to implement their own algorithms often need to choose an algorithm for every problem they need to solve and they often need to discuss their problems with other developers. It might prove to be time consuming trying to explain all these algorithms in the level of detail we have looked at here. That's why <b>Big O Notation</b> was created. It is a way of explaining how an algorithm performs as the dataset it's working on increases over time.

Big O notation allows you to compare runtimes of different algorithms so that you best choose the algorithm to use. The algorithm we have looked at here have different Big O Notations so let's take a look at them.

### Big O Notation of Selection Sort
Remember that the <b>n</b> in Big O notation refers to the number of elements you are working on. With selection sort you need to check each element in the list to see if it's the lowest so you can move it over to the sorted list. So that's n operations. Suppose you using selection sort on a list of five items [8, 5, 1, 4, 7], so n = 5. Here you need to loop over all the items in the list as you look for the lowest item. For our case there are five and you have to make five comparisons to move each one so it is more like five times five operations or more intuitively it is n time n operations (n^2). But you might think to yourself that half of that entire list is missing because we are testing one less item each time so runtime might be O(1/2 n^2) right? Well it is true we are not doing full n times n operations but remember in Big O notations, when the values of n gets really big, constants like 1/2 gets insignificant and so we discard them. The Big O runtime of selection sort is widely recognized as being O(n^2).

### Big O Notation of Quick Sort and Merge Sort

Quick sort requires one operation for each element in the list it's sorting. It needs to select one element as the pivot and then it needs to divide the list into elements that are smaller than the list and the elements that are greater than the list. So that's n operations. That means, you have a list of 8 items, [3, 2, 3, 4, 6, 9, 7, 5], then n = 8, which also means 8 operations. But ofcourse, the list is not sorted by just splitting it around the pivot ones. You have to repeat those operations several times. In the best case, you'll pick a pivot that is right in the middle of the list so you are diving the list exactly in half then you keep dividing until you have a list with the length of one. The number of times you need to divide n in half until you reach 1 is expressed as <b>log n</b>. So you need to repeat n sorting operations log n times. That leaves us with the best case runtime of quick sort as <b>O(n log n)</b>. That is the best case, now what about the worst case? Well if you pick the wrong pivot, you won't be diving the list into half. If you pick a really bad pivot the next recursive call to quick will only reduce the length of the list by 1. Since our quick sort only picks the first item as the pivot, we can make it pick the worst possible pivot repeatedly, simply by giving it a list that is sorted in reverse order. If we pick the worst possible pivot everytime we'll have to split the list once for every item in the list and then do n sorting operations. This gives it a runtime of O(n^2) which is similar to selection sort. 

So which should we consider when trying to decide whether to use quick sort, best case or worst case? Well as long as your implementations just picks the first item as the pivot, turns out that on average quick sort performs closer to the best case. Many quick sort implementations accomplish this by picking pivots at random on each recursive loop.
Random pivots sometimes give you the best case, sometime give you the worst case but it all averages out over multiple calls of the quick sort function. 

Now remember that at best case quick sort has a runtime of O(n log n) but in its worst case, the runtime is <b>O(n^2)</b> and yet out in the real world, quick sort is more commonly used than merge sort. Now why is that if quick sort's worst case runtime can sometimes be worse than merge sort? This is ones of those situations where Big O Notation doesn't tell you the whole story.

You see Big O Notation:

- Tells you number of times an operation is performed
- Doesn't describe duration of operation
- A usefull tool for quickly describing how the run time of an algorithm increases as the data set it's operating on gets really, really big.

## Searching Algorithms

### Linear Search

Having talked about sorting algorithms, I think the foundation has been layed to talk about searching algorithms. If you need to search through an unsorted list, binary search isn't an option because you have no idea which half of the list has what you are looking for, your only idea is start from the beginning and compare each item in the list with the real value one at a time until you find the value you are looking for. This kind algorithm as we have talked about it in the beginning is called linear search or sequential search as the search proceeds in a straight line or sequence.

Suppose we are searching for a name in a list of names, even though linear search is innefficient, searching for just one name will happend so fast that we won't be able to tell anything useful about the algorithm's runtime. Assuming that we have a list of 100 unrelated names and we want to search for a name using linear search algorithm, check out the code in the file <b>linearsearch.py</b> for demonstration.

Now linear search works for a smaller list well as demonstrated with searching 100 names in a list of hundred thousand names but what if we are working with a bigger list of names let's say millions of them? Well Linear search would perform really poorly and given that in reall world, we work with huge lists, linear search might be inefficient. Searching such from search a huge dataset we would need to use a different algorithm, in this case, <b>binary search</b>.

### Binary Search

In the example we have implemented using linear search above, we have seen that searching for a smaller list of names is working well but realistically speaking the real implementation of search algorithms would mean a huge list of names that linear search might perform poorly.

Here is where binary search comes in handy, however to implement binary search, our list would need to be sorted first.

We need to load our unsorted list from a file, sort it, then write the sorted names back to a new file. We will quick sort to achieve this.

So we created another quick sort algorithm specifically for sorting strings. The code for the quick sort function is just the same as the one we used to sort numbers, the only difference is at the top where we load strings from a file instead of numbers. Then we used the algorithm to sort the unsorted list of 500 names to another sorted list but remember these names are in text files, the first file being <b>unsorted.txt</b> and the sorted being <b>sorted.txt</b>. The quick sort for strings code is in the file <b>quicksort_strings.py</b> so please make sure to check it out.

Now that we have a sorted list of names, we can use binary search upon it. Let's see if it can speed up the search of hundred names from the whole list. The code for implementing this is in the file <b>binarysearch.py</b> so make sure to check it out.

## Big O Notations of Linear Search and Binary Search

Based on the previous implementation of both linear search and binary search algorithms when searching a list of 100 names among 500 names, came with different runtimes. We have tested linear search on unsorted list while binary search required us to sort the list first so we did so.

Running the two search algorithms while testing for time it took both of them to search the names using the linux command <b>time linearsearch.py names/unsorted.txt</b> and <b>time binarysearch.py names/sorted.txt</b> proved that binary search runs faster than linear search.

So having seen that practically, let's understand their Big O Notations then.

The Big O runtime for linear search is O(n) also know as linear time.

The Big O runtime of binary search is O(log n).

Now that is just an introduction to algorithms and data structures, there is more to it than just those few algorithms and data structures we have looked at. We will look at more in a few. 