// Time to interleave!  See instructions below

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
    enterQueue(human) {
        var new_node = new ListNode(human);

        if (this.head == null) {
            this.head = new_node;
            this.tail = new_node;
        }
        else {
            this.tail.next = new_node;
            this.tail = new_node;
        }
        return human;
    }
    leaveQueue() {
        if (this.head == null) {
            return null;
        }
        else if (this.head == this.tail) {
            var temp = this.head;
            this.head = null;
            this.tail = null;
            return temp.value;
        }

        var temp = this.head
        this.head = this.head.next
        temp.next = null 

        return temp.value
    }

    front() {
        if (this.head == null) {
            return null;
        }
        return this.head.value
    }
    inLine(human) {
        var runner = this.head;

        while (runner != null) {

            if (runner.value == human) {
                return true;
            }

            runner = runner.next;
        }

        return false;

    }
    isEmpty() {
        if (this.head == null && this.tail == null){
            return true;
        }
        else {
            return false;
        }
    }
    howMany() {
        if (this.isEmpty()){
            return 0;
        }
        var size = 1;
        var runner = this.head;
        while (runner.next != null) {
            runner = runner.next;
            size++;
        }
        return size;
    }
    compareQueues(queue2) {
        if (this.howMany() != queue2.howMany()) {
            return false;
        }
        var queue2Runner = queue2.head;
        var runner = this.head;
        while (queue2Runner != null && runner != null){
            if (queue2Runner.value != runner.value){
                return false;
            }
            queue2Runner = queue2Runner.next;
            runner = runner.next;
        }
        return true;
    }
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

    // Use interleaveQueue() below to alternate the first half of the queue's values with second half 
    // For example: (1,2,3,4,5) would become (1,4,2,5,3) and (6,5,4,3,2,1) would become (6,3,5,2,4,3)
    // Step by Step Example:
    // Original queue:   1 -- 2 -- 3 -- 4 -- 5 -- 6 
    // Splits in half:   1 -- 2 -- 3   |  4 -- 5  -- 6
    // Interleaves one side with the other:   1 -- 4 -- 2 -- 5 -- 3 -- 6

    // Another example
    // Original queue:   George -- Fred -- Gertrude -- Beatrice -- Frank 
    // Splits in half:   George -- Fred -- Gertrude   |   Beatrice -- Frank 
    // Interleaves one side with the other:   George -- Beatrice -- Fred -- Frank -- Gertrude
    
    // HINTS (one way to do it): 
    // Remember you've already created methods that add/remove/count/display the nodes from the queue, use them! (:
    // If really lost, here's the psuedo code on how this could be done:
    // Half the nodes could leave the original queue and enter a temporary one
    //      That way half the nodes could be in one queue and the other half in another one
    // Then have the 1st node leave the front of the temp queue and enter the back 
    // Follow that with the 1st node from the other queue and keep alternating until they are interleaved

    interleaveQueue(){
        
    }
}

var queue = new SLLQueue();
console.log(queue.enterQueue("George"))
console.log(queue.enterQueue("Fred"))
console.log(queue.enterQueue("Gertrude"))
console.log(queue.enterQueue("Beatrice"))
console.log(queue.enterQueue("Frank"))
console.log(queue.display())
console.log(queue.interleaveQueue())

var queue2 = new SLLQueue();
console.log(queue2.enterQueue(1))
console.log(queue2.enterQueue(2))
console.log(queue2.enterQueue(3))
console.log(queue2.enterQueue(4))
console.log(queue2.enterQueue(5))
console.log(queue2.enterQueue(6))
console.log(queue2.display())
console.log(queue2.interleaveQueue())


interleaveQueue(){
    var half = Math.ceil(this.howMany()/2);
    var backRunner = this.head;
    var counter = 0;
    while(counter < half){
        backRunner = backRunner.next;
        counter++;
    }
    var runner = this.head;
    var newQueue = new SLLQueue();
    counter = 0;
    while(counter < half){
        newQueue.enterQueue(runner.value);
        runner = runner.next;
        if(backRunner!=null){
            newQueue.enterQueue(backRunner.value);
            backRunner = backRunner.next;
        }
        counter++;
    }
    this.head = newQueue.head;
    this.tail = newQueue.tail;
    return this;
}