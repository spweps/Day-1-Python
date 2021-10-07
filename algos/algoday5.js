// Use the generateCoinChange function below to receive a dollar (decimal) amount with change. 
// Covert that value to the number of quarters, dimes, nickels, and pennies it would have.
// It should count the number or quarters first then work it's way down from there
// This can return a string or an object or whatever you'd like

// Example: generateCoinChange(.67) woud return 2 quarters, 1 dime, 1 nickel, 2 pennies
// Example: generateCoinChange(0.77) would return 3 quarters, 2 pennies
// Example: generateCoinChange(2.85) would return 11 quarters, 1 dime
// Example: generateCoinChange(4.57) would return 18 quarters, 1 nickel, 2 pennies

// function generateCoinChange(input) {
//     var quarter = .25;
//     var dime = .1;
//     var nickel = .05;
//     var penny = .01;

//     if (input % quarter != 0){
//         return (input % quarter);
//     }
// }

function generateCoinChange(input) {
    var quarters = Math.floor(input / 0.25); // 0.67 => 2.sddsdsd => 2
    input = input % 0.25; // 0.67 => 0.17
    var dimes = Math.floor(input / 0.1);
    input = input % 0.1;
    var nickels = Math.floor(input / 0.05);
    input = input % 0.05;
    var pennies = Math.floor(input / 0.01);
    return quarters + " quarters, " + dimes + " dimes, " + nickels + " nickels, and " + pennies + " pennies."
}

function generateCoinChange(input) {
    function generateCoinChange(input) {
        change = {'quarters': 0, 'dimes': 0, 'nickels': 0, 'pennies': 0};
        while(input>= .25){
            change['quarters']++;
            input-=.25
        }
        while(input>= .10){
            change['dimes']++;
            input-=.10
        }
        while(input>= .05){
            change['nickels']++;
            input-=.05
        }
        while(input>= .01){
            change['pennies']++;
            input-=.01
        }
    
        return change;
    }
}   
    
function generateCoinChange2(input) {
    change = {'quarters': 0, 'dimes': 0, 'nickels': 0, 'pennies': 0};
    change['pennies'] = (input%.25%.10%.05/.01).toFixed(0);
    input-=change['pennies'].01;
    change['nickels'] = (input%.25%.10/.05).toFixed(0);
    input-=change['nickels'].05;
    change['dimes'] = (input%.25/.10).toFixed(0);
    input-=change['dimes']*.10;
    change['quarters'] = (input/.25).toFixed(0);
    
    return change;
    }

var changeArr = [0.25, 0.10, 0.05, 0.01]
var coinObj = {
    "quarters": 0,
    "dimes" : 0,
    "nickels" : 0,
    "pennies" : 0
}

var totalCoins = [0,0,0,0]
function generateCoinChange(input) {
    input = input%1;
    for (var i = 0; i<changeArr.length; i++){
        if(input/changeArr[i] > 1){
            totalCoins[i] = Math.floor(input/changeArr[i]);
            input -= changeArr[i]*totalCoins[i];
        }
    }
    coinObj.quarters = totalCoins[0]
    coinObj.dimes = totalCoins[1]
    coinObj.nickels = totalCoins[2]
    coinObj.pennies = totalCoins[3]
    return coinObj;
}

console.log(generateCoinChange(.67)) 
console.log(generateCoinChange(0.77))
console.log(generateCoinChange(2.85)) 
console.log(generateCoinChange(4.57))

console.log(generateCoinChange(.67)) 
console.log(generateCoinChange(0.77))
console.log(generateCoinChange(2.85)) 
console.log(generateCoinChange(4.57))

console.log(generateCoinChange(.67)) 
console.log(generateCoinChange(0.77))
console.log(generateCoinChange(2.85)) 
console.log(generateCoinChange(4.57))