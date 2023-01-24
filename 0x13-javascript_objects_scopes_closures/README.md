## Advanced Javascript
>In JavaScript, module.exports is a way to expose specific objects or values from a module for use in other parts of your application. It is used in the CommonJS module system, which is the default module system used in Node.js.

```
const add = (a, b) => a + b;
const subtract = (a, b) => a - b;

module.exports = {
  add,
  subtract
};
```

>These functions can now be imported and used in another file:

```
const math = require('./math');
console.log(math.add(2, 3)); // 5
console.log(math.subtract(5, 2)); // 3
```


>The reduce() function in JavaScript is a higher-order function that takes an array and reduces it to a single value by applying a callback function to each element in the array. The callback function takes two arguments: an accumulator (which accumulates the value returned by the callback function) and the current value of the array.

```
let numbers = [1, 2, 3, 4, 5];
let sum = numbers.reduce(function(accumulator, currentValue) {
  return accumulator + currentValue;
}, 0);
console.log(sum); // Output: 15
```

>You can also use arrow function instead of callback function.


```
let sum = numbers.reduce((acc, cur) => acc + cur, 0);
console.log(sum); // Output: 15
```

>The reduce() function is a powerful tool that can be used to perform a variety of operations on arrays, such as finding the average, concatenating strings, or counting occurrences of items.

```
let reversedList = list.reduce((acc, cur) => [cur, ...acc], []);
console.log(reversedList); // Output: [5, 4, 3, 2, 1]
```

