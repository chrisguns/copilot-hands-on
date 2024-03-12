
//how it works
//explain the code above line-by-line
// Language: typescript
function isPrime(n) {
    // if n is less than or equal to 1, return false
    if (n <= 1) {
        return false;
    }
    // loop through all numbers from 2 to the square root of n
    for (let i = 2; i <= Math.sqrt(n); i++) {
        // if n is divisible by i, return false
        if (n % i === 0) {
            return false;
        }
    }
    // if n is not divisible by any number from 2 to the square root of n, return true
    return true;
}