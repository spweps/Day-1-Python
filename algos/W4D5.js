//today we will be finding the min and max node and second to last

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
    moveMinToFront(){
        var min = this.head 
        var runner = this.head 
        var walker = this.head 
        
        while(runner.next != null){ 
            if(runner.next.value < min.value){ 
                min = runner.next 
                walker = runner 
            }            
            runner = runner.next     
        }
        
        if(min == this.head){ 
            console.log("Minimum value is already at the front!")
            return
        } 
        walker.next = min.next 
        min.next = this.head 
        this.head = min 
    }
    moveMaxToBack(){ 
        var max = this.head
        var runner = this.head
        var walker = this.head
        
        while(runner.next != null){
            if(runner.next.value > max.value){
                max = runner.next 
                walker = runner 
            }            
            runner = runner.next          
        }
        
        if(max == runner){ 
            console.log("the max is already at the back!")
            return
        }

        if(max == this.head){ 
            this.head = this.head.next 
        }
        walker.next = max.next 
        max.next = null 
        runner.next = max 
    }
    appendValue(loc,value){
        var node = new ListNode(value)

        var runner = this.head
        var counter = 1;
        while(counter < loc){              
            runner = runner.next
            counter++
        }
        node.next = runner.next   
        runner.next = node   
    }
    prependValue(loc,value){
        var node = new ListNode(value)

        if(loc == 1){
            node.next = this.head;
            this.head = node;
            return
        }
        var runner = this.head
        var counter = 1;
        while(counter < loc-1){            
            runner = runner.next
            counter++
        }           
        node.next = runner.next  
        runner.next = node    
    }
    
    // Use findMinNode() to find the node in the linked list with the lowest value
    // Return the node ITSELF, not its value
    // If you find two or more nodes tied for that value, return the first one you find
    findMinNode(){
        var min = this.head
        var runner = this.head

        while(runner.next !-=null){
            if(runner.next.value < min.value){
                min = runner.next
            }
            runner = runner.next
        }
        return min

    }

    // Use findMaxNode() to find the node in the linked list with the highest value
    // Return the node ITSELF, not its value
    // if you find two or more nodes tied for that value, return the first one you find
    findMaxNode(){
        
    }

    // Use secondToLast() to return the VALUE of the second-to-last node in the linked list
    // HINTS: You could do this with or without a tail.  Choose whichever (:
    // Edge Case: What should you do if the list has less than two nodes?
    secondToLast(){
        
    }
}


var new_sll = new SinglyLinkedList();
new_sll.addToBack(52);
new_sll.addToBack(32);
new_sll.addToBack(88);
new_sll.addToBack(12);
new_sll.addToBack(18);
new_sll.addToBack(22);
new_sll.addToBack(32);
console.log(new_sll.display());

console.log(new_sll.findMinNode())
console.log(new_sll.findMaxNode())
console.log(new_sll.secondToLast())



findMinNode(){ //52, 32, 88, 12, 18, 22, 32
    if (this.head == null){
        return "Are you the Green Knight? Because you've got no head!"
    }
    if (this.head.next == null){
        return "Only one node!"
    }
    var runner = this.head.next;
    var minValue = this.head.value;
    var minNode = this.head;
    while(runner != null){
        if (runner.value < minValue){
            minValue = runner.value
            minNode = runner;
        }
        runner = runner.next;
    }
    return minNode;
}

findMaxNode(){
    if (this.head == null){
        return "Are you the Green Knight? Because you've got no head!"
    }
    if (this.head.next == null){
        return "Only one node!"
    }
    var runner = this.head.next;
    var maxValue = this.head.value;
    var maxNode = this.head;
    while(runner != null){
        if (runner.value > maxValue){
            maxValue = runner.value
            maxNode = runner;
        }
        runner = runner.next;
    }
    return maxNode;
}

secondToLast(){  //52, 32, 88, 12, 18, 22, 32
    if (this.head == null){
        return "Are you the Green Knight? Because you've got no head!"
    }
    if (this.head.next == null){
        return "Only one node!"
    }
    var runner = this.head;
    while(runner.next != this.tail){
        runner = runner.next
    }
    return runner.value
}


findMinNode(){
    if(this.head == null) {
        return "The list is currently empty. There is no smallest node.";
    }
    if(this.head.next == null) {
        return this.head;
    }
    var runner = this.head;
    var minNode = this.head;
    while(runner.next != null){
        if(runner.next.value < minNode.value){
            minNode = runner.next;
        }
        runner = runner.next;
    }
    return minNode;
}
findMaxNode(){
    if(this.head == null) {
        return "The list is currently empty. There is no largest node.";
    }
    if(this.head.next == null) {
        return this.head;
    }
    var runner = this.head;
    var maxNode = this.head;
    while(runner.next != null){
        if(runner.next.value > maxNode.value){
            maxNode = runner.next;
        }
        runner = runner.next;
    }
    return maxNode;
}
secondToLast(){
    if(this.head == null) {
        return "The list is currently empty. There are no nodes.";
    }
    if(this.head.next == null) {
        return "There is only one node. There is no second to last node.";
    }
    var runner = this.head;
    while(runner.next.next != null){
        runner = runner.next;
    }
    return runner.value;
}


class ListNode {
constructor(value) {
    this.value = value;
    this.next = null;
}
}


var new_sll = new SinglyLinkedList();
new_sll.addToBack(52);
new_sll.addToBack(32);
new_sll.addToBack(88);
new_sll.addToBack(12);
new_sll.addToBack(18);
new_sll.addToBack(22);
new_sll.addToBack(32);
console.log(new_sll.display());

console.log(new_sll.findMinNode())
console.log(new_sll.findMaxNode())
console.log(new_sll.secondToLast())