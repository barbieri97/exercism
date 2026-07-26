/// <reference path="./global.d.ts" />
// @ts-check

/**
 * Implement the functions needed to solve the exercise here.
 * Do not forget to export them so they are available for the
 * tests. Here an example of the syntax as reminder:
 *
 * export function yourFunction(...) {
 *   ...
 * }
 */

/**
 * 
 * @param {Number} timer 
 * @returns {String}
 */
function cookingStatus(timer) {
    if (timer > 0){
    return 'Not done, please wait.'
    }else if (timer === 0){
        return 'Lasagna is done.'
    } else {
        return 'You forgot to set the timer.'
    }
}
/**
 * 
 * @param {Array} layers 
 * @param {Number} time 
 * @returns {Number}
 */
function preparationTime(layers, time=2){
    return layers.length * time

}
/**
 * 
 * @param {Array} layers 
 * @return {Object}
 */
function quantities(layers) {
    let noodles = 0
    let sauce = 0
    for (let item of layers){
        if (item === 'noodles'){
            noodles += 50
        } else if (item === 'sauce') {
            sauce += 0.2
        }
    }
    return {noodles:noodles, sauce:sauce}
}

/**
 * 
 * @param {Array} friendsList 
 * @param {Array} myList
 * @returns
 */
function addSecretIngredient(friendsList, myList){
    myList.push(friendsList[friendsList.length -1])
    return
}
/**
 * 
 * @param {Object} recipe 
 * @param {Number} amount 
 * @returns {Object}
 */
function scaleRecipe(recipe, amount){
    let mult = amount /2
    let newRecipe = {}
    for (let item in recipe){
        newRecipe[item] = recipe[item] * mult
    }
    return newRecipe
}


export {
    cookingStatus,
    preparationTime,
    quantities,
    addSecretIngredient,
    scaleRecipe
}
