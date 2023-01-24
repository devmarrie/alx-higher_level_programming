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

