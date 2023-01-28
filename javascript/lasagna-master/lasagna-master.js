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
export function cookingStatus(time=-1){
  if(time===-1)
    return 'You forgot to set the timer.'
  if(time===0)
    return 'Lasagna is done.';
  return 'Not done, please wait.';
}
export function preparationTime(layers,timePerLayer=2){
  return layers.length*timePerLayer
}

export function quantities(layers){
  const recipe={noodles:0,sauce:0}
  for(let value of layers){
    if(value=='noodles') recipe[value]+=50;
    if(value==='sauce') recipe[value]+=0.2;
  }
  return recipe
}
export function addSecretIngredient(friendsList,myList){
  myList.push(friendsList[friendsList.length -1])
}

export function scaleRecipe(recipe,no_of_portion){
  const scaled={}
  for(let i in recipe)
      scaled[i]=recipe[i]/2*no_of_portion
  return scaled
}