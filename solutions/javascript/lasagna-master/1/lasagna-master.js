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
export function cookingStatus(remainingTime) {
  if(remainingTime === undefined) return 'You forgot to set the timer.'
  if(remainingTime === 0) return 'Lasagna is done.'
  return 'Not done, please wait.';
}

export function preparationTime(layers, timePerLayer = 2){
  return layers.length*timePerLayer;
}

export function quantities(layers){
  let reqForNoodles = 0;
  let reqForSauce = 0;
  for(let meal of layers){
    if(meal === 'noodles') reqForNoodles += 50;
    if(meal === 'sauce') reqForSauce += 0.2;
  }
  return {noodles: reqForNoodles,
          sauce: reqForSauce}
}

export function addSecretIngredient(friendsList, myList){
  myList.push(friendsList[friendsList.length-1]);
}

export function scaleRecipe(recipe, numOfPortionsReq){
  let obj = {};
  numOfPortionsReq /= 2;
  for(let item in recipe) {
    obj[item] = recipe[item]*numOfPortionsReq;
  }
  console.log(recipe)
  console.log(obj)
  return obj
}