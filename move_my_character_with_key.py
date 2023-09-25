from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('MapleStory_JrBalrog.png')

running = True

def handle_events():
    global running, dir1, dir2
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir1 += 1
            elif event.key == SDLK_LEFT:
                dir1 -= 1
            elif event.key == SDLK_UP:
                dir2 += 1
            elif event.key == SDLK_DOWN:
                dir2 -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir1 = 0
            elif event.key == SDLK_LEFT:
                dir1 = 0
            elif event.key == SDLK_UP:
                dir2 = 0
            elif event.key == SDLK_DOWN:
                dir2 = 0


frame = 0
x,y = TUK_WIDTH // 2 , TUK_HEIGHT // 2
dir1 = 0
dir2 = 0

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2 , TUK_HEIGHT // 2)
    if frame < 3:
        character.clip_draw(frame * 180,200,180,200,x,y)
    elif frame < 5:
        character.clip_draw(540 + (frame-3) * 250, 200, 250, 200, x, y)
    elif frame < 6:
        character.clip_draw(0, 0, 500, 200, x, y)
    elif frame < 7:
        character.clip_draw(550 ,200,230,200,x,y)

    update_canvas()
    handle_events()
    frame = (frame + 1) % 7
    if x > 0 and x < TUK_WIDTH:
        x += dir1 * 5
    elif x == 0:
        x = 5
    elif x == TUK_WIDTH:
        x = TUK_WIDTH - 5

    if y > 0 and y < TUK_HEIGHT:
        y += dir2 * 5
    elif y <= 0:
        y = 5
    elif y >= TUK_HEIGHT:
        y = TUK_HEIGHT - 5

    delay(0.1)


close_canvas()
