# labcolorpicker
Simple visual Color Picker with a modern UI created with qtpy to easily get color input from the user.

![colorpicker](dark.png)


## Installation

1. Install using pip:

   ```
   pip install labcolorpicker
   ```

   or clone the repository yourself and run:

   ```
   pip install .
   ```

## Usage

2. To ask for a color, import the `getColor` function and run it:

   ```python
   from labcolorpicker import getColor
   
   color = getColor()
   ```

## Customization

* **Showing custom last color:**

   ```python
   old_color = (100,0,0)
   picked_color = getColor(old_color)
   ```

* **Changing the UI Theme**

  ```python
  from labcolorpicker import useLightTheme
  
  useLightTheme(True)
  ```

* **Adding Alpha selection**

  ```python
  from labcolorpicker import useAlpha
  
  useAlpha(True)
  ```

  When the ColorPicker uses Alpha, you have to pass a LABa tuple
  as the last color, otherwise there wil be an error.

  ```python
  old_color = (100,0,0,100)
  picked_color = getColor(old_color)  # => (L,A,B,a)
  ```

## Color Formats and Conversion

* The default format `getColor` will give you is LAB(a),\
  but you can use labcolorpickers color conversion functions\
  if you have a different format like RGB or HEX.

   `color2rgb` **LAB** to **RGB**\
   `rgb2color` **RGB** to **HSV**\
   `rgb2hex` **RGB(A)** to **HEX**\
   `hex2rgb` **HEX** to **RGB**\
   `hex2color` **HEX** to **LAB**\
   `color2hex` **LAB** to **HEX**

* Example:
  ```python
  from labcolorpicker import getColor, color2rgb, rgb2color
  
  old_color = rgb2color((50,50,100))  # => (23.267716436315546, 14.98316950336448, -29.63294942493928)

  picked_color = color2rgb(getColor(old_color))
  ```

* **Color Formats:**

  **RGB** values range from **0** to **255**\
  **LAB** values range from **0** to **100** for L, **-128** to **128** for AB\
  **HEX** values should be in format: `"XXXXXX"` or `"xxxxxx"`\
  **Alpha** values range from **0** to **100**

## License

  This software is licensed under the **MIT License**.\
  More information is provided in the dedicated LICENSE file.
