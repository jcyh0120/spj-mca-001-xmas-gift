def on_on_overlap(sprite, otherSprite):
    info.change_score_by(1)
    pizza.set_position(randint(10, 160), randint(10, 120))
    info.start_countdown(10)
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap)

pizza: Sprite = None
scene.set_background_color(15)
mySprite = sprites.create(img("""
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
    """),
    SpriteKind.player)
controller.move_sprite(mySprite)
pizza = sprites.create(img("""
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
    """),
    SpriteKind.food)