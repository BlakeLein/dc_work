# CSS Notes

## General Points

- The items used to style an element are called "declarations." Declarations have a property (like background-color) and a value (like blue).
- Block elements fill the screen. Inline elements fill the space of their content.
- EVERY HTML element utilizes the box model. This means that from inner to outermost space is labeled: content, padding, border, margin.

## Linking a CSS to an HTML

1. You can include all CSS styles in a style tag in the head section of the document.
2. You can link an external CSS document to your HTML with a link tag in the head section of the document.

## How to Select and Style Specific Elements

1. Style by the type of element (h1, p, body, etc).

   - You can select multiple elements if you separate them with a comma.

2. Style with classes

   - Can be declared on the CSS sheet with a "." in front of the class name.
   - Apply the class to an HTML element by putting 'class=""' in the element's opening tag.
   - This is helpful when you don't want to apply styles to every type of element.

3. Style with IDs

   - Can be declared on the CSS sheet with a "#" in front of the ID name.

4. Descendant selector

   - Selects all of one type of element that are inside of another type of an element.
   - 'p strong' selects all bolded elements that are nested inside of paragraph elements in the HTML.
   - This can also be mixed with ID and classes (an emphasized element inside of an ID)
     - EX. "#fancy em'
   - For classes:
     - EX. "element.class"

5. Universal Selector

   - You can select everything with \*
   - You can select all of a specific type by typing 'element \*' (Don't forget the space!)

6. Adjacent Sibling Selector

   - Elements that follow one another on the same level are called 'siblings' in HTML.
   - "A + B" selects every B element that directly follows A.
   - You can use the ~ sign to select ALL the elements following another instead of just one. (Think A~ selects everything that follows A)

7. Child Element Selector

- You can select all elements nested inside of a larger element with the child selector tool (>)
- A > B selects all the B children inside of parent A.

8. Pseudo Selectors

- 'First Child Pseudo Selector' selects the first child inside of an element using ':first-child'.
  - EX. p:first-child selects the first child element in the p class.
- 'Only Child Pseudo Selector' selects the only child element in an element.
  - EX. p:only-child selects the paragraph elements that are the only child of a larger element.
- 'Last Child Pseudo Selector' selects the last element inside of another element.
- 'nth Child Super Selector' selects the nth number in a parent element.
  - Ex. ":nth-child(8)" selects the 8th child element of the parent.
-
