sprites.onOverlap(SpriteKind.Player, SpriteKind.Food, function (sprite, otherSprite) {
    info.changeScoreBy(1)
    pizza.setPosition(randint(10, 160), randint(10, 120))
    info.startCountdown(10)
})
let pizza: Sprite = null
scene.setBackgroundColor(15)
let mySprite = sprites.create(img`
    . . . . . 2 2 . . 2 2 . . . . . 
    . . . . 2 . . 2 2 . . 2 . . . . 
    . . . . . 2 . 2 2 . 2 . . . . . 
    . . . . . . 2 2 2 2 . . . . . . 
    . . . f f f f 2 2 f f f f . . . 
    . . f 1 1 1 2 2 2 2 1 1 1 f . . 
    . . f 1 1 2 1 2 2 1 2 1 1 f . . 
    . . f f 2 f f 2 2 f f 2 f f . . 
    . . f 1 1 1 1 2 2 1 1 1 1 f . . 
    . . . f 1 1 1 2 2 1 1 1 f . . . 
    . . . f 1 1 1 2 2 1 1 1 f . . . 
    . . . f 1 1 1 2 2 1 1 1 f . . . 
    . . . f 1 1 1 2 2 1 1 1 f . . . 
    . . . f 1 1 1 2 2 1 1 1 f . . . 
    . . . f f f f f f f f f f . . . 
    . . . . . . . . . . . . . . . . 
    `, SpriteKind.Player)
controller.moveSprite(mySprite)
pizza = sprites.create(img`
    . . . . . . . . . . . . . . . . 
    . . . . . . . 5 5 . . . . . . . 
    . . . . . . 5 5 5 5 . . . . . . 
    . . . . . . . 5 5 . . . . . . . 
    . . . . . . 5 7 7 5 . . . . . . 
    . . . . . 7 7 7 7 7 7 . . . . . 
    . . . . 7 7 7 7 7 7 7 7 . . . . 
    . . . . 7 7 7 7 7 9 7 7 . . . . 
    . . . . . 7 8 7 7 7 7 . . . . . 
    . . . . 7 7 7 7 7 7 7 7 . . . . 
    . . 7 7 7 7 7 7 7 7 7 7 7 . . . 
    . 7 7 7 7 2 7 7 7 7 7 7 a 7 . . 
    . 7 7 7 7 7 7 7 7 a 7 7 7 7 7 . 
    . . . . . . e e e e . . . . . . 
    . . . . . . e e e e . . . . . . 
    . . . . . . e e e e . . . . . . 
    `, SpriteKind.Food)
