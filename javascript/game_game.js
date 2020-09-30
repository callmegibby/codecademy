/** @format */

document.addEventlismter("DOMContentLoaded", () => {
  const grid = document.queryselector("grid");
  const doodler = document.createElement("div");
  let doodlerBottomSpace = 150;
  let doodlerBottomSpace = 150;
  let isgameOver = false;
  let platform = 5;

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
      platform.push(newPlatform);
    }
  }

  function start() {
    if (!isGameover) {
      createDoodler();
      createPlatforms();
    }
  }

  //attach to button
  start();
});
