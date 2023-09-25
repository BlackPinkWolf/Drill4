from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

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
    character.clip_draw(frame * 100,100,100,100,x,y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    x += dir1 * 5
    y += dir2 * 5
    delay(0.05)


close_canvas()
