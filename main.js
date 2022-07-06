const readline = require('readline');
const chalk = require('chalk');

const input = readline.createInterface({ input: process.stdin, output: process.stdout })


input.question('What is your name?', (argument) => {
    console.log(argument)
    input.close()
})

input.on('close', () => {
    input.question('What is your name?', (argument) => {
        console.log(argument)
        input.close()
    })
    process.exit(0)
});