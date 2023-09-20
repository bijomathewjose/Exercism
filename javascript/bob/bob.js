//
// This is only a SKELETON file for the 'Bob' exercise. It's been provided as a
// convenience to get you started writing code faster.
//
function isCaps(message) {
  return message.match(/[A-Z]/) && message===message.toUpperCase()
}
export const hey = (message) => {
    const trimmedMessage = message.trim(), isQuestion = trimmedMessage.endsWith('?'), isEmpty = trimmedMessage.length === 0
    if (isEmpty) return "Fine. Be that way!";
    if (isCaps(trimmedMessage)) return isQuestion ? "Calm down, I know what I'm doing!" : 'Whoa, chill out!';
    if (isQuestion) return 'Sure.';
    return 'Whatever.';
};
