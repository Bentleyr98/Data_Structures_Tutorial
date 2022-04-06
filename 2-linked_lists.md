## II. Linked List
#### Introduction
Linked lists are very similiar to lists and arrays, with the exception that they are linked. Hence they are called linked lists.

#### Structure
I've always looked at linked lists like trains. Each train car has a connecting piece to the next and previous train cars. Like those train cars, each node has on one end a pointer pointing to the previous car called prev, and on the other side another pointer pointing to the next car called next. It keeps the entire list ordered and connected to each other.
One of the other distinguishing features of this structure (similiar to a train) is that there is a head and a tail to each linked list. The head shows where it starts and the tail shows the end.

![](DLLGfG.png)

#### Inserting
When it comes down to it, a linked list is still essentially a list. To insert, we will still need to loop through the list, unless we insert at the head or tail. Because a linked list is structured, the head and tail are predefined positions that we maintain. This would make inserting at those specified places instaneous. 

To insert in the list, there are certain steps to accomplish. 
First, we must create a new node. Second, we need to start attaching it 
![](DLLInsertGfG.png)

#### Removing


#### Accessing Values
Accessing values in linked lists are very simple. We can get the value (data) with this code to change the value.
```python
yield curr.data
``` 
We can also reassign the value with this code.
```python 
curr.data = value
```

#### Big O Notation
Operation       | Efficency
----------------|-----------
Looping         | O(n)
*Remove         | O(n) or O(1)
Insert          | O(n)

#### Example -- Remove Duplicates
Here we have an example of removing duplicates from a linked list.

```python




```


#### Problem to Solve -- Enter In A Book Series In Order 
We have a challenge for you. For this problem, you will be tasked with reordering this linked list of books so that the books are in order for the series.

Here is your [starting code](2-books.py)

Once finished, compare your answer to this [solution](2-books_solution.py).
Remember, there's more then one way to solve a problem in programming. 


### Next Data Structure
You've finished this part of the tutorial! We do have one more data structure to teach.
Please head on back to the [welcome page](0-welcome.md) to start the last one.