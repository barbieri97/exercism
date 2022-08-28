// @ts-check

/**
 * Implement the classes etc. that are needed to solve the
 * exercise in this file. Do not forget to export the entities
 * you defined so they are available for the tests.
 */

/**
 * 
 * @param {Number} width 
 * @param {Number} height 
 */
export function Size(width = 80, height = 60){
    this.width = width
    this.height = height
    /**
     * 
     * @param {Number} w 
     * @param {Number} h 
     */
    this.resize = function (w, h){
        this.height = h
        this.width = w
    }
}

export class Position {
    constructor (xpos = 0, ypos = 0){
        this.x = xpos
        this.y = ypos
    }
    /**
     * 
     * @param {Number} newx 
     * @param {Number} newy 
     */
    move (newx, newy){
        this.x = newx
        this.y = newy
    }

}

export class ProgramWindow{
    constructor(){
        this.screenSize = new Size(800, 600)
        this.size = new Size()
        this.position = new Position()
    }
    /**
     * 
     * @param {Size} newSize 
     */
    resize (newSize){
        if (newSize.height < 1){newSize.height = 1}
        if (newSize.width < 1){newSize.width = 1}
        this.size = newSize
        if (newSize.height + this.size.height > this.screenSize.height){
            newSize.height = this.screenSize.height - this.position.y
        }
        if (newSize.width + this.size.width > this.screenSize.width){
            newSize.width = this.screenSize.width - this.position.x
        }
    }
    /**
     * 
     * @param {Position} newPosition 
     */
    move (newPosition){
        if (newPosition.x < 0){newPosition.x = 0}
        if (newPosition.y < 0){newPosition.y = 0}
        if (newPosition.x + this.size.width > this.screenSize.width){
            newPosition.x = this.screenSize.width - this.size.width
        }
        if (newPosition.y + this.size.height > this.screenSize.height){
            newPosition.y = this.screenSize.height - this.size.height
        }
        this.position = newPosition
    }
}
/**
 * 
 * @param {ProgramWindow} programWindow 
 */
export function changeWindow(programWindow){
    let newSize = new Size(400, 300)
    let newPosition = new Position(100, 150)
    programWindow.resize(newSize)
    programWindow.move(newPosition)
    return programWindow
    


}