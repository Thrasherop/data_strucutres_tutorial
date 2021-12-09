# What is a set?

A set is a dynamic array data structure that holds unique and non-repeated data. It does this by using the data itself as the index. This allows a set to have O(1) lookup by value (we will discuss this later). While it may sound like a downside, the non-repeated aspect of sets are actually a feature that allow it to be really handy for many algorithms, which we will show later. 

## What is hashing?

A set uses the data itself as the index of a dynamic array. For example, if we want to insert the integer 3 into a set, we will take that and put it into index `3`. Then if we put 4 in the array, we put it into the index `4`. Now if we want to check if there is a 3 in this set, or we want to access 3, we can simply look at index 3 and see if there is data there.

There is a problem here: how do we store non-integer values such as strings in a set? This is where hashing comes into play. The breakfast food "hashed browns" are just potatoes that have been cut up and scrambled. Computer hashing is similar: it cuts up and scrambles the inputted data. There are many different uses of computer hashing, the most common being password storage. However, hashes are also used in sets.

The built in python function `hash()` takes in a variable of any type, and hashes it. The return is an integer which corrosponds to that variable. Note that hash will always be the same for that program runtime, but it may be different on different machines or in different runtimes.  For example, if I run:

```python
print(hash("hello"))
print(hash("hello"))
print(hash("hello"))
``` 
I get an output of 
```python
-1417392563139104318
-1417392563139104318
-1417392563139104318
```

But if I run this program once again I get an output of:
```python
7685339043008787875
7685339043008787875
7685339043008787875
```

It's also important that not all hashing algorithms work like this, but the `hash()` function does behave this way. 

As you can see, we can use the string as a numerical index. We can then store the string at that index. That number, however, is really big. If we need to store just 100 items, it doesn't make sense to make an array of size  7.6 quintillion. To resolve this, we can pass this number through a simple equation to make the size smaller: `index = hash % array_size`. So if we have an array of size 10, we will run `7685339043008787875 % 10`. This gives us an output of 5, thus we can put this string into index 5.

## Conflict handling

We have yet another problem: what do we do when two pieces of data, when passed through the `hash()` function AND through our `index = hash % array_size` equation, share the same index? We can't store two pieces of data in the same index can we? Technically no, but practically we can. What we can do is store a memory address in that location, and have this memory address corrospond to a different set. 

For example, let's say we need to put float `6.874` and string `hello world` into a set named `berries`. Let's assume that, when passed through our function and equation, they both yield the index `4`. We can create another set (or any data structure) named `cream`, and put the address of `cream` into index 4 in `berries`. Finally, we put `6.874` and `hello world` inside of `cream`. Thus, we can essentially store multiple values into the same index in `berries`.


## Performance of a set

All of this fancy hashing allows us to run a quick hash() call, and then know exactly where to look for data in a set. This means we have O(1) performance. No matter how many millions of pieces of data are in a set, the amount of time it takes to check for 1 piece of data stays the same.

## Uniqueness

In a set, you cannot put duplicate data. This seems like it would be a limiting factor, but as I will show in the example question, it is actually an intended and handy feature of a set. Essentially, you cannot put integer `4` into a set twice. It's as simple as that. 

## Set's in python

Python has the set data structure built directly into the language. There are two ways to create a set. The first is by using curly braces like so:

```python
set1 = {}

```

The other way is by using the built in `set()` function:

```python
set2 = set()
```

You can then add and remove items to a set using the `.add()` and `.remove()` methods respectively. See below:

```python

my_set = set()

my_set.add(1)
my_set.add(1)
my_set.add(2)
my_set.add(3)

print(my_set)

my_set.remove(1)

print(my_set)

```

This code will print the following: 
```python
{1, 2, 3}
{2, 3}
```
Notice that how, even though we added `1` twice, it was only put into the set once, and that it didn't throw any errors. In other words, the second `my_set.add(1)` failed silently. Again, this may seem like a bug, but it is an intended feature, as we will see below.

## Example question

Here is the problem: Given a list of numbers, which numbers in this list add up to 8. There should be no duplicates. With a set, you can do this in O(n).

For this problem, I plan to solve it by initializing a set, and putting all the numbers into it. Next, I'll loop through the set. For every number, I'll subtract it from 8. This subtraction will give me a target number, or the number I need in order to complete the pair (remember a pair needs to add up to 8). Finally, I check if the target number is in the set (remember, this is an O(1) operation). If it is, that means we have successfully found a pair, and so I print the targetNum and the num out to console.

```python

# Initialize a set
mySet = set(numbers)

for num in mySet:

    targetNum = 8 - num

    if targetNum in mySet and targetNum > num:

        print(targetNum, num)

```

Notice how the if statement has that second clause of `and targetNum > num`. This prevents duplicates from being printed by only printing when the bigger number of the pair has been found. For example, if there is a 3 and 4 in the list, it wont print `3 4` and `4 3`. It will only print the `3 4`. 

## Practice problem

Here is the task:  Find if a Python list has any duplicates. This should be done in O(n) using a set. 

Like with the stack lesson, there is a premade file [here](./practice_problems/problems/set_problem.py). Additionally, there is a sample solution [here](./practice_problems/solutions/set_example_solution.py) if you get stuck or you want to see how I did it. 

## Conclusion

The set is a really clever data structure that can come in handy when creating an algorithm. Similar to the stack, and similar to all data structures, it isn't right for all tasks. When you use it properly, however, it can improve the performance of your program exponentially.

