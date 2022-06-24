# Wes Bos Flexbox Notes

### Flex Container

- display: flex makes every nested element a flexbox item
- default layout is row
- default, flex container will be the size of the container it's in. Use inline-flex to make it as wide as the items inside.

### Flex Direction

- Default flex-direction is row (main axis is left-to-right).
- Row reverse is row with the items backward.
- flex direction:column puts things on top of each other (main axis is top to bottom).
- Column reverse is column with the items backward.

### Flex Wrap

- If the items are larger that the container they are in, the items need to know what to do.
- By default, the items will not wrap.
- If you set flex-wrap:wrap, the items will go to the next row. This is typically the case when the items are a set width or the content inside is large enough.
- wrap: reverse will display the items in a row format from bottom to top.
- If there is left-over space between the items and the outer container, you can adjust the items' width to percentages to fix.
- If the flex container size is set to viewport height (vh) and viewport width (vw), the items will always be on the screen, but if they get long enough the scrolling function will kick in.
- If you set the height to min-height: vh, this will allow the container to accept items that grow beyond the container. The container will grow.

### Flexbox Ordering

- An argument given to a flexbox item. Default is order 0.
- This will manually set the order of each item. If every item is 0 and you set something to 1, it will show up first after everthing else.
- Negative values will work the same but in reverse.
- Something to be cautious of: The mouse selector will still copy the next item, even if it is out of order. So if you copy 1, 2, and 3 - with 3 being ordered at the end - it will still select 3 instead of 4.

## Alignment and Centering

### Justify-Content

- Justify-content is what we use to center all items along the main axis.
- center, flex-end, flex-start are pretty self-explanatory
  - sspace-between (first and last items start at the beginning and end and everything else is centered between)
  - space-around (puts a little bit of space before the first and after the last element)
  - **Size of items will be taken into account with spacing!!**

### Align-Items

- Used to align items along the cross-axis (not the main axis).
- The default value is 'stretch'
- Other possible arguments are flex-start, flex-end, and center.
  - Baseline: Will look at the text and align the items based on the baseline of the font, no matter how big or small the items are.

### Align Content

- Takes the same parameters that justify-content takes.
- Justify content works with the items and how they interact with the space on the main axis.
- Align content works with the items and how they interact with the space on the cross axis.
- Default is stretch.
- If they don't behave the way you want them to, you may need to adjust the other properties (wrap, width, height, etc.)
- Often you will need to set the flex-wrap to wrap.

### Align self

- An argument given to an individual item to override the alignment properties of the container.
- Takes same arguments as align-items.

### Flex Property

- Property for the individual flex items to distribute extra space.
- This answers the question with extra space in container or not enough space in the container.
- The default width of the flex item is however big it's content is.
- 'flex: 1' will evenly take up the extra space in the row on the main axis (however big the container is.)
- 'flex: 2' will give an item twice as much of the extra space as the other items. It works like a fraction and is proportional.
- It can take fractions, percentages, pixels, etc.
- flex is a shorthand for using flex-shrink, flex-grow, and flex-basis. Three properties in one.

### Flex-grow, flex-shrink, and flex-basis

- All of these are properties for items in the container.

- Flex grow: When we have extra space, how should we divide it amongst all items on the same line.

  - Defaults for these is zero.

- Flex-basis: Defines the default size of an element before the remaining space is distributed.
  - Values can be a percentage, pixel, or rem amount.
  - Default is size of the content.
- Flex-shrink:
  - When the screen size doesn't allow for the items to have their set flex-basis and there is no wrap on, they will shrink.
  - This controls how the slimming down will work.
  - Default value is 1. All room is evenly divided amongst the items.
  - Whatever item you put the flex-shrink property on, you are telling that item to shrink that many times more than other items. You are telling that item to give up that much more space.
    - Ex. If an item has the 'flex-shrink: 10' property, it will give up 10 times more of the available space and will shrink more than the other items.

**All of these proerties are wrapped up in the single flex property - i.e. flex: 1 1 400px (grow, shrink, basis)**

### Flex-Basis and Wrapping Working Together

## Handy Tricks

- The 'calc' function allows you to subtract a pixel value from a percentage based width or height.
  - Ex. width: calc(33.3333333% - 20px). This sets the width to a percentage for fitting inside a box but then takes it in 20 px to account for space between without breaking the layout using margins.
- You can set the flex items to flex: 1 so the will evenly distribute throughout the view port.
