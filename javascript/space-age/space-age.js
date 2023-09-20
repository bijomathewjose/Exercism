//
// This is only a SKELETON file for the 'Space Age' exercise. It's been provided as a
// convenience to get you started writing code faster.
//
const YEARS={
  mercury:0.2408467,
  venus:0.61519726,
  earth:1,
  mars:1.8808158,
  jupiter: 11.862615 ,
  saturn:29.447498,
  uranus: 84.016846,
  neptune:164.79132
}
const YEAR=31557600
export const age = (planet,seconds) =>  Number((seconds/YEAR/YEARS[planet]).toFixed(2))
