// const { exec } = require("child_process");
const API = `https://exercism.org/api/v2/tracks/javascript/exercises`
const TOKEN = 'f5bac98a-d58e-4c75-88b2-a288c04091b5'

// const main = `exercism download --exercise=${x} --track=${track}`

const arr = ['hello-world', 'guidos-gorgeous-lasagna', 'ghost-gobble-arcade-game', 'currency-exchange', 'meltdown-mitigation', 'black-jack', 'little-sisters-essay', 'little-sisters-vocab', 'card-games', 'chaitanas-colossal-coaster', 'making-the-grade', 'tisbury-treasure-hunt', 'inventory-management', 'locomotive-engineer', 'cater-waiter', 'ellens-alien-game', 'reverse-string', 'resistor-color', 'two-fer', 'leap', 'resistor-color-duo', 'pangram', 'isogram', 'grains', 'hamming', 'bob', 'rna-transcription', 'armstrong-numbers', 'etl', 'darts', 'raindrops', 'sum-of-multiples', 'anagram', 'difference-of-squares', 'flatten-array', 'perfect-numbers', 'gigasecond', 'isbn-verifier', 'space-age', 'collatz-conjecture', 'secret-handshake', 'wordy', 'triangle', 'house', 'rotational-cipher', 'binary-search', 'list-ops', 'acronym', 'pig-latin', 'protein-translation', 'square-root', 'scrabble-score', 'atbash-cipher', 'resistor-color-trio', 'word-count', 'proverb', 'yacht', 'robot-name', 'nth-prime', 'twelve-days', 'matching-brackets', 'palindrome-product', 'diffie-hellman']

// console.log(arr.length)

// arr.forEach(async (i) => {
//     await new Promise((resolve, reject) => {
//         exec(`exercism  download--exercise = ${i} --track =python`, (err, outs, errs) => {
//             outs;
//             resolve();
//         });
//     });
// });
const exec = require('child_process').exec;
// const names = ['name1', 'name2', 'name3'];

const runCommand = (name) => {
    return new Promise((resolve, reject) => {
        exec(`exercism download --exercise=${name} --track=python`, (error, stdout, stderr) => {
            if (error) {
                reject(error);
            }
            resolve(stdout);
        });
    });
}

const runCommands = async (names) => {
    for (const name of names) {
        try {
            const result = await runCommand(name);
            console.log(result);
        } catch (error) {
            console.error(error);
        }
    }
}

runCommands(arr);

