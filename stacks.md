# Stacks

## What is a stack?

A stack is a data structure that is a list of items. The items are added to the stack in the order they are added, and the last item added is the first item to be removed. We call this a LIFO (last in, first out) data structure.


## Dynamic Arrays

Before we talk about stacks, we need to first have a quick review on dynamic arrays. This tutorial won't go into detail on how a dynamic array works, but only a high level review. 

If you recall, there are two attributes for a dynamic array: `capacity` and `size`. Capacity says how much data the dynamic array can currently hold, and size says how much data is actually in the array. In an array, all data slots are of the same size, which means we can look up data by index using the equation ` address = array_address + (index * data_size)`. This means we can look up data by index in O(1). 

Dynamic arrays also maintain "contiguous memory". This means all the data in the array needs to be next to each other. There can be no gaps. This means if we delete (or insert) something at index 0, we then have to move everything down an index in order to fill that gap. This means deletion is an O(n) operation. However, if you delete the data at the end of the dynamic array, there is nothing else that needs to be shifted, and thus inserting and deleting at the end is an O(1) operation

We can use the `size` attribute to keep track of the last index, which means we can easily add and remove data at the end. The stack takes advantage of this.


## How does a stack work?

A stack is a dynamic array with simple rules: you can only insert and remove at the end. Inserting is called pushing, and removing is called popping. When we pop, we also get the data. While this may sound simple, a stack is an incredibly powerful tool.

## Performance

Since we can insert and delete at the end of a dynamic array in O(1) performance, that gives a stack a performance of O(1). This is as fast as it gets. 

## Where is a stack used?

Although a stack is incredibly fast, it may seem useless at first. Why would we want a dynamic array when we can only access the data at the very end? There are many uses for a stack. It isn't good for everything, but what it is good at it is VERY good at. 

One common use for a stack is to keep track of history. Have you ever used ctrl + z to undo a change in a text editor? If yes (which it probably is) then you've interacted with a stack. In a text editor, every change is pushed into a stack. Then when you hit the undo button, it just pops the end off the stack and undoes that change. It is an O(1) operation. The stack is an incredible way of tracknig history.

Have you ever had a function call itself? Letting it do that forever will result in an error called `stack overflow`. Your function callback is tracked in a stack, and when you recurse down a function too many times, that stick fills up and then overflows. That's right. Even your Python interpreter is using the stack data structure.

## How to do it in Python3

In Python3 we can create a dynamic array by initializing a list:

```python
stack = []

```

We can push using the `.append()` method, and we can pop using the `.pop()` method:

```python

stack = []
stack.append(1) # The push
value = stack.pop() # The pop

```

This pop will remove the value at the end, and will add it to the `value` variable.

## Example problem

Let's say we need to reverse a string. We can do this quite elegantly using a dynamic array. We first loop through the string and add each letter to the stack:

```python
string = "Berries and cream"
all_letters_stack = []

for character in string:
    all_letters_stack.append(character)

```

Notice how, in Python, we push to a stack using the append method. So in this code snipit, we put push character in the all_letters_stack. If we print the all_letters_stack, we see this: ` ['B', 'e', 'r', 'r', 'i', 'e', 's', ' ', 'a', 'n', 'd', ' ', 'c', 'r', 'e', 'a', 'm']`.

Now we need to reverse the order. To do this, we can simply pop all the items out of the stack, and add those to a new string. We can do this like this:

```python
reversed_string = ""

while len(all_letters_stack) > 0:
    reversed_string += all_letters_stack.pop()


```

So while there are still items in the all_letters_stack, we pop one out and append it to reversed_string. Since pop removes the last item in the stack, we reverse the order. When we print out reversed_string we see `maerc dna seirreB` which is the reverse of the original string `Berries and cream`. We have successfully reversed the string.

Here is the full code, put inside a function called "reverse_string()"

```python

def reverse_string(string):
    all_letters_stack = []

    for character in string:
        all_letters_stack.append(character)

    
    reversed_string = ""

    while len(all_letters_stack) > 0:
        reversed_string += all_letters_stack.pop()

    return reversed_string


```

## Practice problem

Now it's time for you to do it yourself with this practice problem. The problem you need to solve is this: make a function that can verify every quote had an close quote. Make sure to use a stack

I have already created `stack_problem.py` for you  [here](./practice_problems/problems/stack_problem.py). This file has an empty function, as well as already written tests. Please note these tests are not exhaustive, and you may need to write additional tests.

There is also a example solution [here](`./practice_problems/solutions/stack_example_soludtion.py`). There are many different ways to solve a Software Engineering problem, and this is the way I personally chose to. This means your code may look different, but still work. Nonetheless, feel free to use my solution for additional insight or if you get stuck and need some help

## Conclusion

Like all data structures, the stack isn't the right tool most of the time. However, when it is the right tool, it
is incredibly elegant and incredibly efficient. Thus, it is an incredibly powerful tool to keep in your tool belt.


Here is a link to the next lesson about [sets](./sets.md)