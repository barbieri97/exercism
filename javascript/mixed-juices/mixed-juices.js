// @ts-check
//
// The line above enables type checking for this file. Various IDEs interpret
// the @ts-check directive. It will give you helpful autocompletion when
// implementing this exercise.

const time_to_prepare = new Map([
  ['Pure Strawberry Joy', 0.5],
  ['Energizer', 1.5], 
  ['Green Garden', 1.5],
  ['Tropical Island', 3],
  ['All or Nothing', 5]
])

const wedges_per_lemon = new Map([
  ['small', 6],
  ['medium', 8],
  ['large', 10]
])


/**
 * Determines how long it takes to prepare a certain juice.
 *
 * @param {string} name
 * @returns {number} time in minutes
 */
function timeToMixJuice(name) {
  return time_to_prepare.has(name) ? time_to_prepare.get(name) : 2.5
}

/**
 * Calculates the number of limes that need to be cut
 * to reach a certain supply.
 *
 * @param {number} wedgesNeeded
 * @param {string[]} limes
 * @returns {number} number of limes cut
 */
function limesToCut(wedgesNeeded, limes) {
  let wedges = 0
  let count = 0
  while (wedges <= wedgesNeeded && limes.length && wedgesNeeded){
    let tam = limes.shift()
    wedges += wedges_per_lemon.get(tam)
    count ++
  }
  return count
}

/**
 * Determines which juices still need to be prepared after the end of the shift.
 *
 * @param {number} timeLeft
 * @param {string[]} orders
 * @returns {string[]} remaining orders after the time is up
 */
function remainingOrders(timeLeft, orders) {
  var time = 0
  var queue = 0
  while (time < timeLeft){
    let t = orders[queue]
    time += timeToMixJuice(t)
    queue ++
  }
  return orders.slice(queue)
}

export {
  remainingOrders,
  timeToMixJuice,
  limesToCut
}