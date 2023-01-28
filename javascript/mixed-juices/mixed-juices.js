// @ts-check
//
// The line above enables type checking for this file. Various IDEs interpret
// the @ts-check directive. It will give you helpful autocompletion when
// implementing this exercise.

/**
 * Determines how long it takes to prepare a certain juice.
 *
 * @param {string} name
 * @returns {number} time in minutes
 */
export function timeToMixJuice(name) {
  switch (name) {
    case 'Pure Strawberry Joy': return 0.5;
      break;
    case 'Energizer': return 1.5;
      break;
    case 'Green Garden': return 1.5;
      break;
    case 'Tropical Island': return 3;
      break;
    case 'All or Nothing': return 5;
      break;
    default: return 2.5;
  }
  throw new Error('Please implement the timeToMixJuice function');
}

/**
 * Calculates the number of limes that need to be cut
 * to reach a certain supply.
 *
 * @param {number} wedgesNeeded
 * @param {string[]} limes
 * @returns {number} number of limes cut
 */
export function limesToCut(wedgesNeeded, limes) {
  let wedges_obtained = 0, limes_cut = 0
  while (wedges_obtained < wedgesNeeded && limes_cut < limes.length) {
    switch (limes[limes_cut]) {
      case 'small': wedges_obtained += 6;
        break;
      case 'medium': wedges_obtained += 8;
        break;
      case 'large': wedges_obtained += 10;
        break;
      default: break;
    }
    limes_cut++
  }
  return limes_cut
}

/**
 * Determines which juices still need to be prepared after the end of the shift.
 *
 * @param {number} timeLeft
 * @param {string[]} orders
 * @returns {string[]} remaining orders after the time is up
 */
export function remainingOrders(timeLeft, orders) {
  while (orders.length > 0 && timeLeft > 0) {
    timeLeft -= timeToMixJuice(orders[0]);
    orders.shift()
  }
  return orders
  throw new Error('Please implement the remainingOrders function');
}
