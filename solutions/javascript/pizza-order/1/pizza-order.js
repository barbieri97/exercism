/// <reference path="./global.d.ts" />
//
// @ts-check


  // Preços das diferentes pizzas e dos extras
  let prices = {
    'Margherita': 7,
    'Caprese': 9,
    'Formaggio': 10,
    'ExtraSauce': 1,
    'ExtraToppings': 2
  }

/**
 * Determine the prize of the pizza given the pizza and optional extras
 *
 * @param {Pizza} pizza name of the pizza to be made
 * @param {Extra[]} extras list of extras
 *
 * @returns {number} the price of the pizza
 */
export function pizzaPrice(pizza, ...extras) {
  // declaração da variavel que recebe o valor da pizza
  let finalPrice = 0

  // Atribui o valor base da pizza
  finalPrice += prices[pizza]

  // add o valor dos extras
  for (let x of extras) {
    finalPrice += prices[x]
  }
  return finalPrice

}

/**
 * Calculate the prize of the total order, given individual orders
 *
 * @param {PizzaOrder[]} pizzaOrders a list of pizza orders
 * @returns {number} the price of the total order
 */
export function orderPrice(pizzaOrders) {
  // declara variavél que vai receber o valor final do pedido
  let finalPrice = 0

  // add o valor de cada pizza ao valor final
  for (let x of pizzaOrders) {
    finalPrice += prices[x.pizza]

    for (let y of x.extras) {
      finalPrice += prices[y]
    }

  }
  return finalPrice
}

