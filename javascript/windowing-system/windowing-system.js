// @ts-check

/**
 * Implement the classes etc. that are needed to solve the
 * exercise in this file. Do not forget to export the entities
 * you defined so they are available for the tests.
 */
export function Size(width=80,height=60){
    this.width=width;
    this.height=height;
  }
Size.prototype.resize=function(newWidth,newHeight){
    this.width=newWidth;
    this.height=newHeight;
  };
export function Position(x=0,y=0) {
  this.x=x;
  this.y=y;
}
Position.prototype.move= function (newX,newY) {
   this.x=newX;
   this.y=newY;
}
export class ProgramWindow {
  constructor() {
    this.screenSize=new Size(800,600)
    this.size=new Size()
    this.position=new Position()
  }
  resize(newSize){
    newSize.height=newSize.height<1?1:newSize.height;
    newSize.width=newSize.width<1?1:newSize.width;
    
    let availableWidth=this.screenSize.width-this.position.x;
    let availableHeight=this.screenSize.height-this.position.y;

    newSize.width=(newSize.width>availableWidth)?availableWidth:(newSize.width);
    newSize.height=(newSize.height>availableHeight)?availableHeight:(newSize.height);
    
    this.size.resize(newSize.width,newSize.height);
  };
  move(Position){
    Position.x=Position.x<0?0:Position.x;
    Position.y=Position.y<0?0:Position.y;
    let x=this.screenSize.width-this.size.width;
    let y=this.screenSize.height-this.size.height;
    Position.x=Position.x>x?x:Position.x;
    Position.y=Position.y>y?y:Position.y;
    this.position.move(Position.x,Position.y)
  }
}
  export function changeWindow(programWindow){
    programWindow.resize(new Size(400,300));
    programWindow.move(new Position(100,150));
    return programWindow
  }
