// New data structure!  Queues!!!
// Think of the dreaded lines at roller coaster parks.  It's a first in, first out type situation.
// The first person in line is the first person ride the roller coaster and leave the queue (line)
// When someone joins the queue, where in the line do they join?  At the back (tail)!
// When someone leaves the queue where in line do they leave it from?  The front (head)!
// In our lists, the head will be on the left, and the tail will be on the right
// For example:  node1 (head, remove from here) --- node2 --- node3 --- node4 (tail, add here)

class ListNode {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

class SLLQueue {
    constructor() {
        this.head = null;
        this.tail = null;
    }
    // Use enterQueue(human) to add the given person (node) to the queue (at the tail)
    // Return the added node's value
    // HINTS: Add the new node to the back and assign it the new tail
    // EDGE CASES: What if the list is empty?
    enterQueue(human) {
        
    }
    
    // Use leaveQueue() to remove the first node from the queue
    // Return the removed node's value
    // HINTS: Save the current head, assign new head, cut the connection from the old head
    // EDGE CASES: What if the list is empty?  What if there is only one node in the list?
    leaveQueue() {
        
    }

    // Use front() to return the value of the node at the front of the queue (line)
    // EDGE CASES: What if the list is empty?
    front() {
        
    }

    // Use inLine(human) to search the queue for a node
    // Return true if the node exists in the list, return false if it's not
    inLine(human) {

    }

    // Use isEmpty() to return true if the list is empty, return false if it's not
    isEmpty() {
        
    }

    // Use howMany() to return the number of in the queue
    // EDGE CASES: What if the list is empty?
    howMany() {
        
    }

    // Use compareQueues(queue2) to compare the nodes from two separate queues
    // Return true if the queues have the SAME VALUES in the SAME ORDER return false if not
    // This should be a non-destructive operation (neither queue should change after this runs)
    // HINTS: Try and check both queues in one loop | Think of the conditions that need to be true for the loop to stop
    // EDGE CASE: think of a quick check you can do at the beginning to stop the code from running unnecessarily
    compareQueues(queue2) {
        
    }
    // Again, this is given out of the kindness of my heart to help test (:
    display() {
        if (this.head == null) {
            return null;
        }
        var values = this.head.value;
        var runner = this.head.next;

        while (runner != null) {
            values += " - " + runner.value;
            runner = runner.next;
        }
        return values;
    }
}

// I placed the test console.logs far below.  If you want to create your own, for a little bit
// more of a challenge, go for it!  Or just use mine.  Either way make sure to do whatever your heart 
// tells you, that's what I always do (:



var queue_A = new SLLQueue();
console.log(queue_A.isEmpty())
console.log(queue_A.enterQueue("George"))
console.log(queue_A.isEmpty())
console.log(queue_A.enterQueue("Fred"))
console.log(queue_A.enterQueue("Gertrude"))
console.log(queue_A.enterQueue("Beatrice"))
console.log(queue_A.enterQueue("Frank"))
console.log(queue_A.display())
console.log(queue_A.leaveQueue())
console.log(queue_A.leaveQueue())
console.log(queue_A.display())
console.log(queue_A.inLine("Gertrude"))
console.log(queue_A.inLine("Fred"))
console.log(queue_A.howMany())

var queue_B = new SLLQueue();
console.log(queue_B.enterQueue("Gertrude"))
console.log(queue_B.enterQueue("Beatrice"))
console.log(queue_B.enterQueue("Frank"))
console.log(queue_B.display())
console.log(queue_B.compareQueues(queue_A))
console.log(queue_B.leaveQueue())
console.log(queue_B.compareQueues(queue_A))
