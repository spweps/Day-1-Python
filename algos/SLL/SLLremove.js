// Today we will be removing the front and back nodes of the SLL using the functions found at the bottom

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

    // Use removeFront() to remove the head of the linked list and return its value
    // HINTS: 
    // this needs to be in a certain order, what would happen if you set this.head's value to null first?
    // or what would happen if you only set the new head and that's it?  
    // this.head's value needs to change
    // The connection between the old head and new head needs to be severed
    // If you get done early try and handle the edge cases if the linked list only has one or zero nodes

    removeFront() {
        //create me!
    }

    // Use removeBack() to remove the tail of the linked list and return its value
    // HINTS: 
    // Think about how can we get to the end of the list and how can we tell which one is the 2nd to last?
    // This needs to be in a certain order as well
    // Save the value of the old tail so you can return it  
    // A new tail should be marked
    // The connection between the old tail and new tail needs to be severed
    // If you get done early try and handle the edge cases if the linked list only has one or zero nodes

    removeBack() {
        //create me!
    }
}

var new_sll = new SinglyLinkedList();
new_sll.addToBack("Disneyland");
new_sll.addToBack("Las Vegas");
new_sll.addToBack("Mount Rushmore");
new_sll.addToBack("Times Square");
console.log(new_sll.display());

console.log(new_sll.removeFront())
console.log(new_sll.display());

console.log(new_sll.removeBack())
console.log(new_sll.display());



//from class below

removeFront() {
    if(this.head == null){
        return "That doesn't look like anything to me";
    }

    var temp = this.head;
    this.head = this.head.next; // {value: "Disneyland", next: { value: "Golden Gate Bridge", next: ...}
    return temp;
}

removeBack() {
    var runner = this.head;
    
    
    if(this.head == null){
        return "That doesn't look like anything to me";
    }
    
    if (this.head.next == null){ // { value: "Disneyland", next: null}
        console.log("This is the only node! And now it's gone!")
        var temp = this.head;
        this.head = null;
        return temp;
    }

    while (runner != null) { // Keeps going further into nodes until it hits the last one
        if(runner.next.next == null){
            console.log("The line below me is the runner!");
            console.log(runner);
            var temp = runner;
            runner.next = null; // { value: "Mount Rushmore", next: { value: "Times Square", next: null } }
            break;
        }
        runner = runner.next;
    }
    return temp;
}



removeFromFront() {
    if(this.head == null){
        return "The list is already empty.";
    }
    var val = this.head.value;
    if(this.head.next == null){
        this.head = null;
        this.tail = null;
    }
    else {
        this.head = this.head.next;
    }
    return val;
}
removeFromBack() {
    if(this.head == null){
        return "The list is already empty.";
    }
    var val = this.tail.value;
    if(this.head.next == null){
        this.head = null;
        this.tail = null;
        return val;
    }
    var runner = this.head;
    while(runner.next.next != null){
        runner=runner.next;
    }
    this.tail = runner;
    runner.next = null;
    return val;
}



removeFront() {
    var temp = this.head;
    this.head = this.head.next;
    return temp;
}

// Use removeBack() to remove the tail of the linked list and return its value
// HINTS:
// Think about how can we get to the end of the list and how can we tell which one is the 2nd to last?
// This needs to be in a certain order as well
// Save the value of the old tail so you can return it
// A new tail should be marked
// The connection between the old tail and new tail needs to be severed
// If you get done early try and handle the edge cases if the linked list only has one or zero nodes

removeBack() {
    if (this.head == null) {
        return "empty list"
    } 
    else {
        var runner = this.head;
        var oldTail = this.tail;
        while (runner.next != null) {
            if (runner.next == this.tail) {
                var temp = runner;
                runner.next = null;
            } 
            else if(runner.next == null){
                this.head = null
                this.tail = null
                return "you've emptied the list"
            }
            else {
                runner = runner.next;
            }
        }
        this.tail = temp;
        return oldTail;
        // console.log("New Tail = " + this.tail.value);
    }
}
}