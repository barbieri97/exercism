// @ts-check

/**
 * Calculates the sum of the two input arrays.
 *
 * @param {number[]} array1
 * @param {number[]} array2
 * @returns {number} sum of the two arrays
 */
function twoSum(array1, array2) {
  let n1 = array1.reduce((acc, cur) => String(acc) + String(cur))
  let n2 = array2.reduce((acc, cur) => String(acc) + String(cur))
  return Number(n1) + Number(n2)
}

/**
 * Checks whether a number is a palindrome.
 *
 * @param {number} value
 * @returns {boolean}  whether the number is a palindrome or not
 */
function luckyNumber(value) {
  let v = String(value);
  let reverse_str = v.split('').reverse().join('')
  return v === reverse_str
}

/**
 * Determines the error message that should be shown to the user
 * for the given input value.
 *
 * @param {string|null|undefined} input
 * @returns {string} error message
 */
function errorMessage(input) {
  if (input){
    return Number(input) ? '' : "Must be a number besides 0"
  }
  return "Required field"
}

export {
  errorMessage,
  luckyNumber,
  twoSum
}
