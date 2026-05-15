// @ts-check

/**
 * Calculates the sum of the two input arrays.
 *
 * @param {number[]} array1
 * @param {number[]} array2
 * @returns {number} sum of the two arrays
 */
export function twoSum(array1, array2) {
  let num1 = 0;
  let i = 0;
  while(i<array1.length){
    num1 = num1*10 + array1[i]%10;
    i++;
  }
  let num2 = 0;
  i = 0;
  while(i<array2.length){
    num2 = num2*10 + array2[i]%10;
    i++;
  }
  console.log(num1);
  console.log(num2);
  return num1+num2;
}

/**
 * Checks whether a number is a palindrome.
 *
 * @param {number} value
 * @returns {boolean} whether the number is a palindrome or not
 */
export function luckyNumber(value) {
  let str = String(value);
  let i = 0, j = str.length - 1;
  while(i<j) if(str.charAt(i++) != str.charAt(j--)) return false;
  return true;
}

/**
 * Determines the error message that should be shown to the user
 * for the given input value.
 *
 * @param {string|null|undefined} input
 * @returns {string} error message
 */
export function errorMessage(input) {
  if(input === null || input === undefined || input == '') return 'Required field';
  if(Number.isNaN(Number(input))|| Number(input) === 0) return 'Must be a number besides 0';
  return '';
}
