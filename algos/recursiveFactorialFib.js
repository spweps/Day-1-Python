// Recursion!  It's when a function calls itself over and over until some condition has been met (base case)
// If multiple functions are called they are added, in the order invoked, to the "call stack" 
// The "call stack" is list of functions that have been called but aren't done yet 
// A function is "done" when it returns something.  Then, it's removed from the call stack  
// The call STACK is a "last in first out" structure, remember that??? (:  
//    The last function called is the first to be resolved
// In recursion, a call stack is created when a function calls itself over and over
// A "base case" is needed which is:
//    A condition that will end the recursion by returning something other than the function call
// Each time it calls itself something should be done to the values to eventually meet the base case
// Anything a loop can do, recursion can do as well
// Loops, however, cannot do everything recursion can do.  A good example of this is traversing tree structures

// Here we use the function called sum(num)
// It uses recursion to sum all the values between 1 and the given number
// For example: sum(10) returns 55 | sum(4) returns 10
function sum(num) {
    if (num == 1){
        return 1    
    }
    else {
        return num + sum(num-1);
    }
}
console.log(sum(4));

// Ok onto the challenges for today!

// Use factorial(num) to return the value of all the numbers in a range multiplied by each other
// For example: factorial(5) returns 120 because 5 * 4 * 3 * 2 * 1 = 120
// factorial(6) returns 720 because 6 * 5 * 4 * 3 * 2 * 1 = 720
function factorial(num) {
    
}
console.log(factorial(3))
console.log(factorial(5))
console.log(factorial(6))
console.log(factorial(7))

// A Fibonacci sequence is when each number is the sum of the two preceding ones, starting at 0 and 1
// For example:  0  1  1  2  3  5  8  13  21  34  55  89  144..... 

// Use fibonacci(n) below to receive the nth number in the Fibonacci sequence starting at position 0
// For Example: fibonacci(0) would return 0 | fibonacci(1) returns 1 | fibonacci(2) returns 1 
// fibonacci(3) returns 2 | fibonacci(4) returns 3 | fibonacci(5) returns 5 | fibonacci(6) returns 8 etc....
// HINTS: Think of where in the Fibonacci sequence the recursion would start creating the stack and start resolving it
// Might have to use fibonacci(n) more than once.  One for the 1st number, another for the number it's adding to 
// Depending on your code, don't make n very high or it might make your computer think for a looooong time

function fibonacci(n) {
    
}
console.log(fibonacci(4));
console.log(fibonacci(9));


function factorial(num) {
    if (num < 1){
        return "Number entered as an argument must be a positive number."
    }
    if(num == 1){
        return 1;
    }
    return num * factorial(num-1);
}

console.log(factorial(5));

function fibonacci(position) {
    if(position < 0) {
        return "Number entered as an argument must be greater than or equal to 0.";
    }
    if(position == 0) {
        return 0;
    }
    if(position == 1) {
        return 1;
    }
    return fibonacci(position-1) + fibonacci(position-2);
}

console.log(fibonacci(9));