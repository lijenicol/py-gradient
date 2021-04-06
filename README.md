# py-gradient
### A program for generating colourful gradients

py-gradient is a program that generates a gradient image based off a list of points and colours. At the moment, images are exported in the .PPM file format (you may require a special image viewer to view these images).

#### Note: py-gradient requires Python 2.7, it cannot be executed with Python 3

## Using the software:
Points, colours and image information are supplied to the program via a JSON file as a command line argument. An example JSON file is supplied in the repository as config.json - it will also be shown here:
```
{
    "image-width" : 1000,
    "image-height" : 1000,
    "falloff" : 1.15,
    "colors" : [
        [1,0,0],
        [0,1,0],
        [0,0,1],
        [1,0,1],
        [1,0,0]
    ],
    "positions" : [
        [0,0],
        [1,0],
        [1,1],
        [0,1],
        [0.6,0.6]
    ]
}
```
Here `image-width` and `image-height` specify the width and height of the outputted image. `colors` is a list of `[r,g,b]` colour tuples (note: the maximum value for each colour channel is 1). `positions` is a list of `[x,y]` positions (note: positions need to be supplied in the range [0,0] x [1,1]). When specifying positions and colours, remember to pair them together - that is, each colour should have a corresponding position. `falloff` is the amount that each colour decreases the further away it is from a specific point. 

By default, images are output to a file named `"out.ppm"`, however you can change this by supplying another argument in the command line (the .ppm suffix is automatically added so you do not need to add it in the argument).

### Example py-config execution:
`python color.py config.json gradient`
