import sys
import json

# Position refers to pixel value
# Color is between 0 and 1
class PointColor(object):
    def __init__(self, pos, color):
        self.pos = pos
        self.color = color

# Linearlly interpolate between two points
def lerp(start, end, t):
    return start + (end-start)*float(t)

# Clamp between [0,1]
def clamp(t):
    return max(0, min(1, t))

# Generates gradients based on different colors and points
def generate_gradient(colors, falloff, width, height, fname):
    with open(fname + '.ppm', 'w') as file:
        file.write('P3\n')
        file.write('%d %d\n' % (width, height))
        file.write('255\n')

        total_pixels = width * height
        pixel_count = 0
        for i in range(height):
            for j in range(width):
                # Store x and y for normalized coords
                x = i / float(height)
                y = j / float(width)

                # Calculate t for color lerp (initial values are background color)
                color_r_list = []
                color_g_list = []
                color_b_list = []
                for color in colors:
                    dist_2 = (x - color.pos[0])**2 + (y - color.pos[1])**2
                    if dist_2 == 0:
                        interpolation = 1.0
                    else:
                        falloff = 1.25
                        interpolation = clamp(1 - falloff * dist_2**0.5)
                    color_r_list.append(color.color[0] * interpolation)
                    color_g_list.append(color.color[1] * interpolation)
                    color_b_list.append(color.color[2] * interpolation)

                # Calculate additive sum of colors (produces better results than
                # taking the average)
                color_r = clamp(sum(color_r_list))
                color_g = clamp(sum(color_g_list))
                color_b = clamp(sum(color_b_list))

                # Write color
                file.write("%d %d %d\n" % (color_r * 255, color_g * 255, color_b * 255))

                # Output status of program
                pixel_count += 1
                if (pixel_count/float(total_pixels))*100 % 10 == 0:
                    print '\r%d percent done' % ((pixel_count/float(total_pixels))*100),

if __name__ == '__main__':
    # Load JSON file
    with open(sys.argv[1]) as file:
        data = json.load(file)
    
    # Generate colors from JSON
    colors = []
    for index,color in enumerate(data["colors"]):
        new_point_color = PointColor(data["positions"][index], color)
        colors.append(new_point_color)
    
    # Generate gradient
    if len(sys.argv) == 2:
        generate_gradient(colors, data["falloff"], data["image-width"], data["image-height"], 'out')
    else:
        generate_gradient(colors, data["falloff"], data["image-width"], data["image-height"], sys.argv[2])