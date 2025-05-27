import matplotlib.pyplot as plt
import numpy as np
import random
from PIL import Image

def draw_hex_grid_on_image(image_path, rows, cols, hex_size, num_circles, output_path,
                           x_offset_global=0, y_offset_global=0, circle_size=0.4):
    # Load image
    img = Image.open(image_path)
    img_width, img_height = img.size
    dpi = 100
    fig_size = (img_width / dpi, img_height / dpi)

    # Create figure
    fig, ax = plt.subplots(figsize=fig_size, dpi=dpi)
    ax.imshow(img)
    ax.set_xlim(0, img_width)
    ax.set_ylim(img_height, 0)  # Flip y-axis
    ax.axis('off')
    ax.set_aspect('equal')

    hex_height = np.sqrt(3) * hex_size
    circle_map = {}

    # Draw hex grid
    for row in range(rows):
        for col in range(cols):
            x = col * 1.5 * hex_size + x_offset_global
            y = row * hex_height + (col % 2) * (hex_height / 2) + y_offset_global

            if 0 <= x <= img_width and 0 <= y <= img_height:
                hexagon = create_hexagon(x, y, hex_size)
                ax.plot(*zip(*hexagon), color='black', linewidth=0.5)

    # Add random circles
    colors = ['red', 'blue', 'green', 'purple', 'orange']
    for _ in range(num_circles):
        col = random.randint(0, cols - 1)
        row = random.randint(0, rows - 1)
        x = col * 1.5 * hex_size + x_offset_global
        y = row * hex_height + (col % 2) * (hex_height / 2) + y_offset_global

        if 0 <= x <= img_width and 0 <= y <= img_height:
            ax.add_patch(plt.Circle((x, y), hex_size * circle_size,
                                    color=random.choice(colors), alpha=0.6))

    # Save final image
    plt.show()
    #plt.savefig(output_path, bbox_inches='tight', pad_inches=0)
    plt.close()

def create_hexagon(x_center, y_center, size):
    angles = np.linspace(0, 2*np.pi, 7)
    x_hex = x_center + size * np.cos(angles)
    y_hex = y_center + size * np.sin(angles)
    return list(zip(x_hex, y_hex))


# === Example usage ===
image_path = '001-map-sc.jpg'
output_path = 'map_with_hexes.png'
draw_hex_grid_on_image(
    image_path=image_path,
    rows=30,
    cols=30,
    hex_size=55,          # In pixels
    num_circles=600,
    output_path=output_path,
    x_offset_global=15,
    y_offset_global=14,
    circle_size=0.7
)


# draw_hex_grid_on_image(
#     image_path=image_path,
#     rows=18,
#     cols=18,
#     hex_size=55,          # In pixels
#     num_circles=200,
#     output_path=output_path,
#     x_offset_global=55,
#     y_offset_global=16,
#     circle_size=0.7
# )