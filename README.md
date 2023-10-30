# stereocam

Install requirements:
```
python3 -m pip install numpy
python3 -m pip install opencv-python
python3 -m pip install mediapipe
```

Run triangulator with two webcams connected via USB.
```
python3 triangulator.py
```
(x,y,z) coordinates for index finger tip are returned in millimeters.

To convert between pixel coordinates and real-world x,y,z coordinates:
```
from triangulator import Triangulator
tr = Triangulator(120, 70.3)
```
For a certain point in space, find pixel coordinates on left and right cameras and use the following function to return x,y,z real-world coordinates:
```
coords_left = (x_left, y_left)
coords_right = (x_right, y_right)
(x, y, z) = tr.pix2mm(coords_left, coords_right)
```