## II. Queue
#### Introduction
Queues are a great way to keep order. We use queues, when we are in checkout lines, a waitlist, etc. They are in our everyday life. Because it's so orderly, this saves us time and space trying to find whatever should be next, but is buried somewhere else in the array.
#### Structure
Queues look like lists, they are also arrays. We can declare a queue like we would a list/queue.
```queue = []```
How queues work is that they remove one at the top (left side) of the list, and add at the back (right side) as directed.
#### Inserting
To insert in a queue, we are simply appending to the back of the list (that's how queues work, remember?). We can do this with this code ```queue.append(item)``` it's a very simple and straightforward way to work with this array.
#### Removing
Removing an item from an array is also really simple. We can treat it just like we would a list. By using ```queue.pop(0)``` this will take off the first item of our list. We can also remove other items from our list or queue by using indexing. In life, it would be like a person in the middle of a line got tired of waiting, so she/he left the line. That would be exiting a queue.
#### Looping through Lists (Arrays)
We can loop through our list/queues fairly easy by using a for loop.
#### Big O Notation
Big O Notation is looking at the worst case scenario that allows us to evaluate how effecient our algorthim is.

Big O for looping is O(n). 
Big O for removing is O().
Big O for inserting is O().
#### Example -- Checkout Line
Here is an example problem showing how we can insert into a queue by adding customers to a checkout line.

```

```

#### Problem to Solve -- Expired Food
We have a challenge for you. For this problem, you will be searching through an abstract pantry to find and remove expired food. Some of it is still good today and should be used, others have gone too far.

Here is your starting code
```

```


