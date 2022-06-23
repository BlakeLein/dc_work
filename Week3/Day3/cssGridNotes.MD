# CSS Notes

## General Points

- Like Flexbox, CSS grid is designed to help with page layout.
- Start by creating a container and typing "display: grid". Everything inside is a child element.

## Specific Uses

- 'grid-template-columns' will create your columns. This property can accept multiple arguments:
  - Ex: grid-template-columns: 100px 100px 100px creates three columns that are 100px each.
  - You can also use repeat(x, 100px) where x is the number of columns and 100px is the size of each.
  - Instead of px for column sizes, you can use 'fr' which will allow each column to more evenly fill the grid.
  - **You can mix and match these methods of spacing!**
  - Columns will wrap to a new row if you have too many of them.
- 'grid-template-rows' will define rows if there are none already on the page.
  - Ex. grid-template-rows: 50px 50px 50px will create three rows that are 50px high each.
  - You can use 'grid-auto-rows' to set the height of the rows automatically
- When a grid is generated, the lines that divide each column and row are assigned to a number from left-to-right (columns) and top-to-bottom (rows). You can size grid items by defining the start and end positions by row and column on the grid item.

```
.grid-item-1 {
  grid-column-start: 1;
  grid-column-end: 4;
  grid-row-start: 1;
  grid-row-end: 2;
}

.grid-item-2 {
  grid-column-start: 1;
  grid-column-end: 3;
  grid-row-start: 2;
  grid-row-end: 4;
}
```

- This will create a grid that allows the boxes to end in the desired place.
