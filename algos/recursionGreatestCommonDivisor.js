// Greatest Common Divisor
// Use recursiveGreatestCommonDivisor(num1, num2) below to receive two numbers and recursively determine 
// the greatest common divisor (the largest number that can evenly be divided into both)
// For example: recursiveGreatestCommonDivisor(5,10) would return 5 because it is the highest number that can be
// divided evenly into 5 and 10.
// HINT:  
// Thanks to Euclid (ancient Greek Mathmetician), we know the following:
// if num1 === num2, that number is the greatest common divisor
// if num1 > num2, we can calculate num1-num2 and that will get you to or closer to the GCD
// if num2 > num1, we can calculate num2-num1 and that will get you to or closer to the GCD
// For example: if we had num1=5 and num2=10 | num2 > num1 so we do 10-5 which gives us 5 which is the GCD

function recursiveGreatestCommonDivisor(num1,num2){
    
}
console.log(recursiveGreatestCommonDivisor(5,10)); // 5
console.log(recursiveGreatestCommonDivisor(50,180)); // 10
console.log(recursiveGreatestCommonDivisor(7,35)); // 7
console.log(recursiveGreatestCommonDivisor(65,95)); // 5


// Bonus: Try and rewrite it in a way that will be able to avoid stack overflow when num1=123456 & num2=987654
// HINT: I had the remainder of the food at Mod Pizza.  There wasn't any left (:

function recursiveGreatestCommonDivisor2(num1,num2){
    
}

console.log(recursiveGreatestCommonDivisor2(123456,987654))



//Dunavan
function recursiveGreatestCommonDivisor(num1, num2){
    if(num1 == num2){
        return num1;
    }
    if(num1 > num2) {
        return recursiveGreatestCommonDivisor(num2, num1-num2);
    }
    return recursiveGreatestCommonDivisor(num1, num2-num1);
}

console.log(recursiveGreatestCommonDivisor(5,10)); // 5
console.log(recursiveGreatestCommonDivisor(50,180)); // 10
console.log(recursiveGreatestCommonDivisor(7,35)); // 7
console.log(recursiveGreatestCommonDivisor(65,95)); // 5

function recursiveGreatestCommonDivisor2(num1,num2){
    if(num1%num2==0){
        return num2;
    }
    if(num1 > num2){
        return recursiveGreatestCommonDivisor2(num2, num1%num2);
    }
    return recursiveGreatestCommonDivisor2(num1, num2%num1);
}

console.log(recursiveGreatestCommonDivisor2(123456,987654))


//Jacob
function recursiveGreatestCommonDivisor(num1,num2){
    if (num1 == 0 || num2 == 0){
        return ("No common denominator")
    }
    if (num1 == num2){ 
        return num1
    }
    if (num1 > num2){
        return recursiveGreatestCommonDivisor(num1 - num2, num2)
    }
    if (num2 > num1){
        return recursiveGreatestCommonDivisor(num2 - num1, num1)
    }
}
function recursiveGreatestCommonDivisor2(num1,num2){
    if (num1 == 0){
        return num2
    }
    if (num2 == 0){
        return num1
    }
    if (num1 == num2){ 
        return num1
    }
    if (num1 > num2){
        return recursiveGreatestCommonDivisor2(num1%num2, num2)
    }
    if (num2 > num1){
        return recursiveGreatestCommonDivisor2(num2%num1, num1)
    }
}