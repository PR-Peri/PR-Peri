import svgwrite

def generate_snake_svg():
    dwg = svgwrite.Drawing('snake.svg', profile='tiny')

    # Create snake path
    path = dwg.path(d="M10 80 C 40 10, 65 10, 95 80 S 150 150, 180 80", class_="snake")
    path['style'] = "fill: #FFFFFF;"

    # Create background rectangle
    background = dwg.rect(insert=(0, 0), size=("100%", "100%"), class_="background")
    background['style'] = "fill: #000000;"

    # Add elements to the drawing
    dwg.add(background)
    dwg.add(path)

    # Save the SVG file
    dwg.save()

if __name__ == "__main__":
    generate_snake_svg()
