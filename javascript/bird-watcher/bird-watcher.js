// @ts-check
//
// The line above enables type checking for this file. Various IDEs interpret
// the @ts-check directive. It will give you helpful autocompletion when
// implementing this exercise.

/**
 * Calculates the total bird count.
 *
 * @param {number[]} birdsPerDay
 * @returns {number} total bird count
 */
export function totalBirdCount(birdsPerDay) {
  let sum=0
  for(let i=0;i<birdsPerDay.length;i++){
    sum+=birdsPerDay[i];
  }
  return sum
  throw new Error('Please implement the totalBirdCount function');
}

/**
 * Calculates the total number of birds seen in a specific week.
 *
 * @param {number[]} birdsPerDay
 * @param {number} week
 * @returns {number} birds counted in the given week
 */
export function birdsInWeek(birdsPerDay, week) {
  return totalBirdCount(birdsPerDay.slice((week-1)*7,week*7))
  throw new Error('Please implement the birdsInWeek function');
}

/**
 * Fixes the counting mistake by increasing the bird count
 * by one for every second day.
 *
 * @param {number[]} birdsPerDay
 * @returns {number[]} corrected bird count data
 */
export function fixBirdCountLog(birdsPerDay) {
  for(let i=0;i<birdsPerDay.length;i+=2)
          birdsPerDay[i]=birdsPerDay[i]+1
  return birdsPerDay
  throw new Error('Please implement the fixBirdCountLog function');
}
