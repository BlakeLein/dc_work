# Class Notes - Laying Out a Website

- **Everything in an element is a box!**
- They don't always look like boxes, that's just how they're treated.
- The box is content, padding, border, and margin.
- You can use the inspect tools in google to see what part of the box you're working with.
- You can use border properties to help identify where things are.

### Basic Adjustments

1. Margin, border, padding using the 'px' unit of measurement.
2. You can adjust any side! Topr, right, bottom, left. If you just say 'margin' it will do that value for all.

- Ex:
  - top-margin: 10px
  - margin: 10px 5px (top and bottom 10, left and right 5)
  - margin: 5px 5px 10px 10px (top, right, bottom, left)

3. Sometimes margin and padding are defaulted, and we need to override that.

## Layout

- You will typically begin the layout process by making div elements. These will serve as containers.
- DIV CONTAINERS ARE ALWAYS THE SIZE OF THEIR CONTENTS UNLESS SPECIFIED OTHERWISE.

## Flex Box

- Make a class called "container" to apply to the flex container.
- Used to organize an layout our web page.
- Handles a lot of the problems that plagued early front end development, specifically with layout.
- To use flexbox, you put 'display: flex' into the container class. This makes any element assigned that class a flex containers.
- Flex defaults to a row layout unless you change it.
- Flex elements WILL go outside the container they are in if they are bigger than the parent element.
- If you don't want a row, you have to tell flexbox otherwise.
- Flexbox stength is not in making a grid. CSS is the best tool for grid work.

### Specific Examples

- Use 'justify-content: center' to make the items stay in the center. This centers up and down (vertical)
  - You can also justify 'end' and 'start'
  - space-around, space-between, space-evenly are all a little different.
- Use 'align-items: center' to center things left and right (horizontal)
- Use 'flex-direction: column' to make the items in a colum instead of a row.
  - You can also use 'column-reverse' and 'row-reverse'
- When you use the 'flex-wrap: wrap' property, the items will fit inside of the container, no matter how big or small it works.
  - You can also wrap reverse
- You can include 'gap: 20px' to make a gap between the child items. This was built to create a short solution for margin.

### Things to Remember

- If you put another div element inside of a container element, it will treat that div element as one item.
- If content is very small, a lot of the flex properties may not show up.
- Don't put plain text in a div, make sure it's in a paragraph tag.
- Items on top of each other are columns; items next to each other are rows.

## Random Points

- Differ the stylesheet in the link if you want it to load after the page loads.
