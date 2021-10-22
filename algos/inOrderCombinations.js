// Use inOrderCombinations() to receive a string and return an array holding all the combinations of strings 
//     that could be made in the order they are given
// The order of the string combinations in the output array doesn't matter
// For Example:
// input string of "ab" returns ["ab", "a", "b", ""] (4 items in array)
// "abc" returns ["abc", "ab", "ac", "a", "bc", "b", "c", ""] (8 items)
// "sup" returns ["sup", "su", "sp", "s", "up", "u", "p", ""] (8 items)
// "junk" returns ["junk","jun","juk","ju","jnk","jn","jk","j","unk","un","uk","u","nk","n","k",""] (16 items)
// 
// The number of results follow this equation: 2^n | Where n is the number of letters of the string passed in
// For Example: If there are 3 letters it will return 2^3 (8) results or 4 letters 2^4 (16)
// Every character will appear the same amount of times in the output
// Test with at least 4 characters in input

// HINTS:
// For your parameters, you might want to have an input, empty output array, a position tracker, and a partial variable
//    INPUT receives the string, OUTPUT would be an empty array that would eventually be populated with the 
//    different string combinations, POSITION would track the current index positions (letters) of the string, 
//    and PARTIAL would hold the string values that are not equal to the full/main string passed in
// You might want to have two functions, one that gets the full string, and another that gets the partial strings
// Base case could be when the length of the string equals the current index position you're on in the string

function inOrderCombinations(input, output=[], position=0, partial='') {
    if(input.length == position){
        output.push(partial);
    }
    else{
        inOrderCombinations(input, output, position+1, partial + input[position]);
        inOrderCombinations(input, output, position+1, partial);
    }
    return output;
    
}
console.log(inOrderCombinations("ab"));
console.log(inOrderCombinations("abc"));
console.log(inOrderCombinations("sup"));
console.log(inOrderCombinations("junk"));
