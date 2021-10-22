// Back in the day, we had to press numbers which in turn would give us letters and we used that method to text
// It was amazing!  So let's create something that takes us back to that golden age
// If you look at your keypad on your phone there will be letters that are tied to each numbers

// Use telephoneWords() to receive a string of digits and return an array of all the possible letter combinations
// Here are the numbers are the characters they represent:
// 1: _.@ | 2: ABC | 3: DEF | 4: GHI  | 5: JKL | 6: MNO | 7: PQRS | 8: TUV | 9: WXYZ | 0: ' ' (a space)
// For Example: '23' would return ['AD','AE','AF','BD','BE','BF','CD','CE','CF']  (combination of ABC and DEF)
// '10' would return ['_ ', '. ','@ '] (combination of _.@ and ' ')



// HINTS:
// We can use four parameters in our recursive function, input, output, position, and partial
// INPUT would be the digit string passed in, OUTPUT would be an empty array that will eventually hold the combinations,
// POSITION would keep track of where we are in the string, PARTIAL would save the different combinations
// This one should only require one recursive call to telephoneWords

// The object phoneChar is given here to access the characters each number represents
// Remember you can choose an index position of a character in a string!
// For example: phoneChars["23"[0]] resolves into phoneChars[2] because it pulled the first character from "23" and that gives us "ABC"
// Also, phoneChars["23"[1]] resolves into phoneChars[3] because it pulled the 2nd character of "23" and that gives us "DEF"
// You could use that method to select the different key value pairs in the phoneChars object
// A loop could be used to progress further into the string and combine the strings
// Remember when recursive functions are called inside of a loop, it pauses the loop, waits for the recursive call
//   and then continues on

var phoneChars = {
    1: '_.@', 2: 'ABC', 3: 'DEF', 4: 'GHI', 5: 'JKL', 6: 'MNO', 7: 'PQRS', 8: 'TUV', 9: 'WXYZ', 0: ' '
}
function telephoneWords(input, output = [], position = 0, partial = '') {
    
}

results = telephoneWords('2')
console.log(results)
console.log(results.length)
results2 = telephoneWords('23')
console.log(results2)
console.log(results2.length)
results3 = telephoneWords('10')
console.log(results3)
console.log(results3.length)

//Dunavan
function telephoneWords(input, output = [], partial = '') {
    if(!input){
        output.push(partial);
    }
    else {
        for(var i = 0; i < String(phoneChars[input[0]]).length; i++){
            telephoneWords(input.substring(1,input.length),output, partial + `${String(phoneChars[input[0]])[i]}`)
        }
        return output;
    }
}

//Jacob
function telephoneWords(input, output = [], position = 0, partial = '') { // input:2, output:[], pos:0, part:""
    var temp = partial
    for(var i = 0; i<phoneChars[input[position]].length; i++){
        partial = temp
        partial += phoneChars[input[position]][i] // partial = "A"
        console.log(partial)
        if (position+1 == input.length){ // Haven't reached the end of the input yet
            output.push(partial)
        }
        else {
            telephoneWords(input, output, position+1, partial) //pos:1, partial:"A"
            }
        }
        if (position+1 == input.length){
            return output
        }
        return output
}