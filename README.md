# stereocam 

Install requirements:
```
python3 -m pip install numpy
python3 -m pip install opencv-python
python3 -m pip install mediapipe
```

## Quick Guide
1. Install two Logitech C615 webcams into the 3D-printed housing at this link: https://www.thingiverse.com/thing:6290545.
2. Follow this link for the math behind triangulation used in this code: https://medium.com/@acerruto/simple-depth-sensing-with-a-dyi-stereo-camera-d4f42627f7e7

## Example
Run example with two webcams connected via USB.  
This example tracks hand coordinates in three dimensions.  
Real-world (x, y, z) coordinates for the index finger tip are returned in millimeters.
```
python3 example.py
```

## Using Triangulator
To convert between pixel coordinates and real-world (x, y, z) coordinates:
```
from triangulator import Triangulator
tr = Triangulator(inter_axial_distance=120, viewing_angle=70.3)
```
For a certain point in space, find pixel coordinates on left and right cameras and use the following function to return real-world (x, y, z) coordinates in millimeters:
```
coords_left = (x_left, y_left)
coords_right = (x_right, y_right)
(x, y, z) = tr.pix2mm(coords_left, coords_right)
```

## Test Hand Detection with one webcam
```
python3 hands.py
```