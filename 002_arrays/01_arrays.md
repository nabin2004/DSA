---
title: Arrays in Python
short_title: Arrays
description: All about Arrays
thumbnail: ../logo.svg
---

:::{toc}
:context: section
:::



Arrays are the starting point of data structures for a reason. They are simple, predictable, and brutally honest about performance. If something is slow with arrays, it is usually slow everywhere else too.

This chapter exists to build intuition. Not tricks. Not shortcuts. By the end, you should be able to look at any array operation and immediately reason about its cost.

If you skip this and jump ahead, it will catch up with you later.

## What an Array Really Is

An array is a collection of elements stored in contiguous memory locations.

That single sentence explains almost everything important about arrays.

Because elements are stored next to each other in memory:

* Accessing an element by index is fast
* Traversing the array is straightforward
* Inserting or deleting elements can be expensive

In low-level languages like C or C++, arrays have a fixed size. Once created, the size cannot change.

Python does not expose raw arrays by default. Instead, it gives you lists, which behave like dynamic arrays. The rules are the same. Python just hides the resizing work.

## Why Arrays Matter

Arrays show up everywhere, even when you do not see them.

They are used to:

* Store input data
* Build strings
* Implement stacks and queues
* Represent matrices and grids
* Act as building blocks for more complex data structures

If you understand arrays well, many other topics feel less intimidating.

## Indexing and Memory

Array indexing is the superpower here.

When you write arr[i], the program does not loop or search. It calculates the memory address directly using a formula.

That is why access time is constant.

This is also why arrays need contiguous memory. Without it, direct address calculation would not work.

## Operations and Their Cost

Do not memorize time complexities. Understand why they happen.

* [ ] Access by index
  Constant time because the memory location is directly computed

* [ ] Update by index
  Constant time for the same reason as access

* [ ] Traversal
  Linear time because every element must be visited

* [ ] Insertion
  At the end is usually constant time in Python lists
  At the beginning or middle is linear time due to shifting

* [ ] Deletion
  Linear time in most cases because elements must be shifted

If this feels abstract, draw boxes on paper and simulate shifting.

## Python Lists as Dynamic Arrays

Python lists automatically resize when they run out of space.

To make this efficient, Python allocates extra memory in advance. Most append operations are fast, but occasional resizes cost more.

This is why append is amortized constant time, not guaranteed constant time.

You do not need to memorize this term. Just remember that Python trades memory for speed.

## One-Dimensional vs Two-Dimensional Arrays

A one-dimensional array is a simple list of values.

A two-dimensional array is a list of lists.

There is no real matrix structure in Python lists. It is just nesting.

This leads to common mistakes:

* Accidentally sharing inner lists
* Confusing rows and columns
* Incorrect indexing order

Most 2D problems are logic problems, not syntax problems.

## Arrays vs Lists

In interviews, this distinction is often tested conceptually.

* Arrays use contiguous memory and fixed size
* Python lists are dynamic and resizable
* Arrays are memory efficient
* Lists are flexible and easier to work with

You should be able to explain when each choice makes sense.

## Practice Checklist

Do not rush these. Write them from scratch.

* [ ] Find the largest element in an array
* [ ] Count occurrences of a given element
* [ ] Remove duplicates while preserving order
* [ ] Reverse an array in place

## Real Problem Context

Arrays and lists are rarely the final answer. They are the tool you use on the way to the answer.

They appear in:

* Sliding window problems
* Two pointer techniques
* Prefix sum optimizations
* Dynamic programming tables
* Graph and tree representations

If arrays feel solid, problem solving becomes calmer.

That is the goal.
