
# Python pixel game engine that uses only native python.

A simple tools to make basics shape and more in your terminal. It also give you basics controls over your terminal behaviour, like the window size.


## Demo

https://user-images.githubusercontent.com/101042422/178258748-15366975-d090-4421-b92e-b876581c85a7.mp4


## Documentation

- initialisation

```python
import nsii
nsii = nsii.Nsii()
```
- retrieve and set values of any parameter

```python
values = nsii.parameter
nsii.parameter = values
```

- available parameters

| Parameter | Type | Description |
| :-------- | :--- | :---------- |
| `name` | `str` | window name |
| `size` | `(int, int)` | window size |
| `pos` | `(int, int)` | window position |
| `fps` | `float` | current frame rate |
| `fps_target` | `int or 'max"` | frame rate target |
| `m_pos` | `(int, int)` | cursor coordinates |
| `p_size` | `int` | pixel size |

- available functions

| Function | Description |
| :------- | :---------- |
| `nsii.draw()` | displays all changes |
| `nsii.dot(x, y, f_col=(r, g, b), b_col=(r, g, b))` | draw dot |
| `nsii.line(x0, y0, x1, y1, f_col=(r, g, b), b_col=(r, g, b))` | draw line |
| `nsii.circle(x, y, radius, f_col=(r, g, b), b_col=(r, g, b))` | draw circle |
| `nsii.rect(x, y, width, height, f_col=(r, g, b), b_col=(r, g, b))` | draw rectangle |
| `nsii.input((x, y))` | retrieve user input |
| `nsii.print((x, y), text)` | print text |
| `nsii.key_pressed(key)` | retrieve status of given key code see: https://bit.ly/3RtrWua |

- image initialisation
```python
image = nsii.new_image('example.ppm')
```

- available parameters

| Parameter | Type | Description |
| :-------- | :--- | :---------- |
| `image.size` | (int, int) | image size |
| `image.pos` | (int, int) | image position |

- available functions

| Function | Description |
| :------- | :---------- |
| `image.show(hide=(r, g, b))` | displays the image |
