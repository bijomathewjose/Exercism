//
// This is only a SKELETON file for the 'RNA Transcription' exercise. It's been provided as a
// convenience to get you started writing code faster.
//
const STRANDS={G:'C',C:'G',T:'A',A:'U'}
export const toRna = (DNA) => {
  return Array.from(DNA).map(item=>STRANDS[item]).join('')
};
