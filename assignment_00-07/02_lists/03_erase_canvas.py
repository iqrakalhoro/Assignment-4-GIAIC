from graphics import Canvas
import time

CANVAS_WIDTH: int = 400
CANVAS_HEIGHT: int = 400

CELL_SIZE: int = 40
ERASER_SIZE: int = 20

def erase_objects(canvas, eraser):
    """🩹 Erase blue cells that are under the eraser by turning them white."""
    mouse_x = canvas.get_mouse_x()
    mouse_y = canvas.get_mouse_y()

    left_x = mouse_x
    top_y = mouse_y
    right_x = left_x + ERASER_SIZE
    bottom_y = top_y + ERASER_SIZE

    overlapping_objects = canvas.find_overlapping(left_x, top_y, right_x, bottom_y)

    for obj in overlapping_objects:
        if obj != eraser:
            canvas.set_color(obj, 'white')  # Erase by changing color to white

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    # 🟦 Create grid of blue cells
    num_rows = CANVAS_HEIGHT // CELL_SIZE
    num_cols = CANVAS_WIDTH // CELL_SIZE

    for row in range(num_rows):
        for col in range(num_cols):
            left_x = col * CELL_SIZE
            top_y = row * CELL_SIZE
            right_x = left_x + CELL_SIZE
            bottom_y = top_y + CELL_SIZE

            canvas.create_rectangle(left_x, top_y, right_x, bottom_y, 'blue')

    canvas.wait_for_click()  # ⏳ Wait for user to click to position eraser

    last_click_x, last_click_y = canvas.get_last_click()

    # 🎨 Create eraser rectangle (pink)
    eraser = canvas.create_rectangle(
        last_click_x,
        last_click_y,
        last_click_x + ERASER_SIZE,
        last_click_y + ERASER_SIZE,
        'pink'
    )

    # 🔄 Move eraser with mouse and erase blue cells
    while True:
        mouse_x = canvas.get_mouse_x()
        mouse_y = canvas.get_mouse_y()
        canvas.moveto(eraser, mouse_x, mouse_y)

        erase_objects(canvas, eraser)

        time.sleep(0.05)  # ⏱️ Small delay for smooth interaction

if __name__ == '__main__':
    main()
