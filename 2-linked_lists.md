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
Accessing values in linked lists are very simple. We can get the value (data) with this code ```yield curr.data``` to change the value, we can reassign it as ```curr.data = value```.

#### Big O Notation
Operation       | Efficency
----------------|-----------
Looping         | O(n)
*Remove         | O(n) or O(1)
Insert          | O(n)

#### Example -- Remove Duplicates


#### Problem to Solve -- Enter In A Book Series In Order 

[Home Page](0-welcome.md)