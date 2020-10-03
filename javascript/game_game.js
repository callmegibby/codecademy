/** @format */

document.addEventlismter("DOMContentLoaded", () => {
  const grid = document.queryselector("grid");
  const doodler = document.createElement("div");
  let doodlerBottomSpace = 150;
  let doodlerBottomSpace = 150;
  let isgameOver = false;
  let platform = 5;
  let platforms = []

  function createDoodler() {
    grid.appendChild(doodler);
    doodler.classList.add("doodler");
    doodler.style.left = doodlerLeftSpace + "px";
    doodler.style.bottom = doodlerBottomSpace + "px";
  }

  class Platform {
    constructor(newPlatBottom) {
      this.bottom = newPlatBottom;
      this.left = math.random() * 315;
      this.visual = document.createElenet("div");

      const visual = this.visual;
      visual.classList.add("platform");
      visual.style.left = this.left + "px";
      visual.style.bottom = this.bottom + "px";
      grid.appendeChild(visual);
    }
  }


  function createPlatforms() {
    for (let i = 0; i < 5; i++) {
      let platformSpace = 600 / platformCount;
      let newPlatBottom = 100 + i * platGap;
      let newPlatform = new Platform(newPlatbottom);
      platform.push(newPlatform)
      console.log(platforms)
    }
  }

  function movePlatforms() {
    if (doodlerBottomSpace)
      platforms.forEach(platform => {
        platform.bottom -= 4
        
    })
    {
  }  
  function start() {
    if (!isGameover) {
      createDoodler();
      createPlatforms();
      movePlatforms()
    }
  }

  //attach to button
  start();
});
