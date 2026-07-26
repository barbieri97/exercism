export const COLORS: Array<string> = [
  'black',
  'brown',
  'red',
  'orange',
  'yellow',
  'green',
  'blue',
  'violet',
  'grey',
  'white',
  ]


export function decodedValue(colors: Array<string>):number {

  let textNumbers: Array<string> =  colors.slice(0,2).map(x => {
    return String(COLORS.indexOf(x))
  })

  return Number(textNumbers.join(""))
}  

