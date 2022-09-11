/* Graphical view of MathProportion
 x1     y1
---- = ----
 x2     y2 */

function MathProportion(MATH_LIST) {
    let _search_i; 
    for(let i = 0; i < MATH_LIST.length; i++) { if(MATH_LIST[i] == 'x' ) { _search_i = i } }
    if (_search_i === 3) { return (MATH_LIST[1]*MATH_LIST[2])/MATH_LIST[0] }
    else if (_search_i === 2) { return (MATH_LIST[0]*MATH_LIST[3])/MATH_LIST[1] }
    else if (_search_i === 1) { return (MATH_LIST[0]*MATH_LIST[3])/MATH_LIST[2] }
    else if(_search_i === 0) { return (MATH_LIST[1]*MATH_LIST[2])/MATH_LIST[3] }
}

const input = async (LABEL) => {
    const readline = require('readline');
    const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
    const prompt = (query) => new Promise((resolve) => rl.question(query, resolve));
    let _user = await prompt(LABEL)
    rl.close()
    return _user
}



const client = () => {
console.log(
    MathProportion([1,2,3,'x'])
)
}

client()