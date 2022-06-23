# Class Notes - CSS Grid and Media Queries

## Media Queries

- Optimizing content for different size screens (computer, tablet, phone)
- Conditional statements that change the layout of a website depending on the size of the screen.
- "Media Query" is detecting a device that you are using.
- It is native to CSS and simple to use.
- You can set display to none when things reach a certain size. You can have code in different containers to trigger when the screen size gets to a certain point

### Using Media Queries

- Start by creating a media queries class in the CSS:

```
@media screen and (min-width: 480px) {
    CSS code here
}
```

- This sets the CSS code for a screen bigger than 480 px. If you put "max-width: 480px" it would be any screen smaller than 480px.
-

## CSS Grid

- When you add grid, it does change the way the content is laid out. It may or may not be a huge visible change. It does affect the way the margins interact.
- Default layout is columns.
- When dealing with rows and columns, if the rows or columns are getting smaller than the size of the content, the content's padding/margins will be sacrificed.
- To avoid many spacing and scaling headaches, it's best to use 'fractions' or 'fr' values in place of pixels. These maintain a constant scale to screen size and items are always measured in relation to each other.
  - If windows get too much smaller than the content, the content will spill out of the grid. That is when pixels should be considered.
- You can nest a flex box inside of a grid item!

### Specific Examples:

- 'space-items: center' will center everything left and right as well as up and down.
- 'grid-template-columns: ' is a way we can define the columns all at once.
  - You can give it as many columns as you want. You can set the columns equal to a pixel value (same size regardless of window size) or a 'fr' (ratio) value.
- 'grid-template-rows: ' is a way to manipulate the rows all at once. A good use is to set it to "auto". Auto will make the row as tall as it needs to be for what content is inside of it.
  - If you have a lot of rows you can use repeat(x, 25px) where x is the number of rows and 25 px is the desired size.
    - You can enter multiple sizes so the rows alternate.
    - You can set the first argument to "auto" so it just does that for every row.
- 'gap: 20px' will put 20 pixels around every side of each element. It takes 1, 2, or 4 arguments.
- 'grid-template-columns and 'grid-template-rows' can specifically target how many columns for row and item will take up.
- 'grid-template-area: ' will replace the template row and template column properties. They cannot co-exist.
  - You can determine the size of each element using strings!
  ```
  grid-template-ares:
  "grid1 grid1 grid1"
  "grid2 grid2 grid2"
  "grid3 grid3 grid3"
  ```
  - Then assign the 'gridx' to each element you want to apply it to as a variable!
    - Ex: `grid-area: grid1` in the class applied to each individual element.
