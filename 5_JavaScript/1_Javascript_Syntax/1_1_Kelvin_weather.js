//Variable is temperature constant Kelvin
const kelvin=0;
//Celsius
const celsius=kelvin-273;

//fehrenheit
let fahrenheit=celsius *(9/5) + 32;
console.log("Fahrenheit: "+fahrenheit);

// round down fahrenheit
fahrenheit = Math.floor(fahrenheit);

console.log(`The temperature is ${fahrenheit} degrees Fahrenheit.`);

// Convert to Newton
let newton = celsius * (33 / 100);
 
// Round down
newton = Math.floor(newton);
 
console.log(`The temperature is ${newton} degrees Newton.`);
