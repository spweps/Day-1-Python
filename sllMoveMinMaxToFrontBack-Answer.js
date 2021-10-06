//today we are going to use nodes with numbers as values and take the lowest value and move it
//to the front.  We will also take the highest value and move it to the back.

class ListNode {
    constructor(value) {
      this.value = value;
      this.next = null;
    }
}

class SinglyLinkedList {
    constructor() {
        this.head = null;
        this.tail = null;
    }

    addToFront(value) {
        var new_node = new ListNode(value);

        if (this.head == null) {
            this.head = new_node;
            this.tail = new_node;
        }

        else {
            new_node.next = this.head;
            this.head = new_node;
        }
    }
    addToBack(value) {
        var new_node = new ListNode(value);
        if (this.head == null) {
            this.head = new_node;
            this.tail = new_node;
        }
        else {
            this.tail.next = new_node;
            this.tail = new_node;
        }
    }
    contains(target) {
        var runner = this.head;

        while (runner != null) {
            if (runner.value == target) {
                return true;
            }
            runner = runner.next;
        }
        return false;
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
    removeFront() {
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
    removeBack() {
        if (this.head == null) {
            return null;
        }
        else if (this.head == this.tail) {
            var temp = this.head;
            this.head = null;
            this.tail = null;
            return temp.value;
        }
        let runner = this.head; 
        while (runner != this.tail) { 
            if (runner.next == this.tail) {
                let getEnd = this.tail;
                this.tail = runner; 
                runner.next = null; 
                return getEnd.value; 
            }
            runner = runner.next;  
        }
    }
    // Use moveMinToFront() to find the location of lowest value in the list and move it to the front
    // HINTS:
    // Need to go through the whole list checking their values to find the lowest one 
    // Could have a temp variable that holds the node with the lowest value
    //   -- this will be the node that will need to be moved to the front
    // Could have another variable that stays one behind the node with the lowest value
    //   -- this would be used to keep the connection going with the the node that comes 
    //      after the node with the lowest value
    // Once you find the lowest node, connect the node before it, to the node after it (it being the lowest node)
    // Then attach the lowest node to the head (which is what brings it to the front)
    // After all the connections have been restored crown the lowest node the head!
    moveMinToFront(){
        var min = this.head //this holds node with lowest value
        var runner = this.head //this is the runner
        var walker = this.head //this is going to be one behind min so when we remove it
        //walker will be there to restore the connection to the node that came after the min node
        
        while(runner.next != null){ 
            if(runner.next.value < min.value){ //if the next value of the runner is less than the current min value
                min = runner.next //this sets the new current minimum value
                walker = runner //this puts the walker behind the minimum value so when we sever the connection it will be there to remake the connection
            }            
            runner = runner.next     
        }
        
        if(min == this.head){ //after we go through the whole list, if the minimum value is at the front of the list we don't need to do anything
            console.log("Minimum value is already at the front!")
            return
        } 
        walker.next = min.next //connects the walker, which is behind the minimum value, to what was after the min value
        min.next = this.head //connects the lowest value node to the front of the list
        this.head = min //makes the min node the head
    }
    // Use moveMaxToBack() to find the location of highest value in the list and move it to the back
    // HINTS:
    // Need to go through the whole list checking their values to find the highest one 
    // Could have a temp variable that holds the node with the highest value
    //   -- this will be the node that will need to be moved to the back
    // Could have another variable that stays one behind the node with the highest value
    //   -- this would be used to keep the connection going with the the node that comes 
    //      after the node with the highest value
    // Once you find the highest node, connect the node before it, to the node after it (it being the highest node)
    // Then set the next property to the max node to null since it will be at the end of the list
    // Then set the next property of the runner to the max node since runner should be at the end
    moveMaxToBack(){ 
        var max = this.head
        var runner = this.head
        var walker = this.head
        
        while(runner.next != null){
            if(runner.next.value > max.value){ //if the next value is greater than the current max value
                max = runner.next //set the new max value to the runner's next value
                walker = runner // set the walker to be behind the runner's current position so when we sever the connection it will be there to replace the max node
            }            
            runner = runner.next          
        }
        
        if(max == runner){ //after we go through the whole list, if the max value is at the end of the list we don't need to do anything
            console.log("the max is already at the back!")
            return
        }

        if(max == this.head){ //if the max value is at the front of the list
            this.head = this.head.next //move the max node over to make it the 2nd in the list
        }
        walker.next = max.next //take the walker which is behind the max node, and connect it to the node after the max node
        max.next = null //set the next node of max to be null since it will be at the end of the list
        runner.next = max //runner is currently at the end of the list so this sets max to be after the runner, now putting it at the end
    }
}


var new_sll = new SinglyLinkedList();
new_sll.addToBack(3);
new_sll.addToBack(15);
new_sll.addToBack(11);
new_sll.addToBack(18);
new_sll.addToBack(5);
new_sll.addToBack(1);
new_sll.addToBack(7);
new_sll.addToBack(9);
console.log(new_sll.display());

new_sll.moveMinToFront()
console.log(new_sll.display());

new_sll.moveMaxToBack()
console.log(new_sll.display());
