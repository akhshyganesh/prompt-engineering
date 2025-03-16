Here are some JavaScript examples showcasing AI-assisted programming and debugging using prompt engineering:

---

### 1️⃣ **Code Generation: Generate a Function Based on a Prompt**
#### **Prompt:**  
*"Write a JavaScript function that checks if a given number is prime."*

#### **Generated Code:**
```js
function isPrime(num) {
    if (num < 2) return false;
    for (let i = 2; i <= Math.sqrt(num); i++) {
        if (num % i === 0) return false;
    }
    return true;
}

// Example usage
console.log(isPrime(7)); // true
console.log(isPrime(10)); // false
```

---

### 2️⃣ **Bug Fixing: Debugging a Broken Function**
#### **Prompt:**  
*"Fix the bug in the following JavaScript function that is supposed to reverse a string but doesn't work correctly."*

#### **Buggy Code:**
```js
function reverseString(str) {
    return str.split("").reverse;
}

console.log(reverseString("hello")); // TypeError: reverse is not a function
```

#### **Fixed Code:**
```js
function reverseString(str) {
    return str.split("").reverse().join("");
}

console.log(reverseString("hello")); // "olleh"
```

🔹 **Correction:** Added `()` after `.reverse` and used `.join("")` to convert the array back into a string.

---

### 3️⃣ **Logic Explanation: Understanding JavaScript Closures**
#### **Prompt:**  
*"Explain how closures work in JavaScript with an example."*

#### **Generated Explanation & Code:**
```js
function outerFunction(outerVariable) {
    return function innerFunction(innerVariable) {
        console.log(`Outer: ${outerVariable}, Inner: ${innerVariable}`);
    };
}

const closureExample = outerFunction("Hello");
closureExample("World"); // Output: Outer: Hello, Inner: World
```
🔹 **Explanation:**  
- The `innerFunction` has access to `outerVariable` even after `outerFunction` has finished execution.  
- This is due to JavaScript’s closure mechanism, which retains access to the outer function’s variables.

---

### 4️⃣ **Code Refactoring: Improve Performance**
#### **Prompt:**  
*"Optimize the following JavaScript function that finds the sum of an array."*

#### **Original Code (Inefficient Looping):**
```js
function sumArray(arr) {
    let sum = 0;
    for (let i = 0; i < arr.length; i++) {
        sum += arr[i];
    }
    return sum;
}
```

#### **Optimized Code (Using `reduce`):**
```js
const sumArray = (arr) => arr.reduce((acc, num) => acc + num, 0);

console.log(sumArray([1, 2, 3, 4])); // 10
```
🔹 **Improvement:** Used `.reduce()` for cleaner, more efficient iteration.

---

### 5️⃣ **Auto-Generating Unit Tests**
#### **Prompt:**  
*"Write Jest unit tests for the `isPrime` function."*

#### **Generated Jest Test Cases:**
```js
const isPrime = require('./isPrime');

test('checks if 7 is prime', () => {
    expect(isPrime(7)).toBe(true);
});

test('checks if 10 is not prime', () => {
    expect(isPrime(10)).toBe(false);
});

test('checks edge case for 1', () => {
    expect(isPrime(1)).toBe(false);
});
```
🔹 **Benefit:** AI can generate test cases automatically, saving time.

---

Would you like more advanced AI-assisted debugging examples, such as working with APIs or performance profiling? 🚀
