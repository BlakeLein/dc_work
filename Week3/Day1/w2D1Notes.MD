# HTML/CSS/JS

### HTML

- The skeleton layout of a page. The underlying structure.

### CSS

- The design of the page. The visual layout.

### JavaScript

- The underlying operation of a website. Considered 'front-end' operations.

Together these languages make a Front End application.

## Web Page Operations

#### Front End

- The client and what the client sees and interacts with.

#### Back End

- The server and database.

A Full-Stack application utilizes both interaction with the client and manipulating data with a database. Developers work in these different realms.

**Boiler Plate for HTML - In VS Code type a ! and hit enter. The guts of the document auto populate!**

## HTML Notes

- Hyper Text Markup Language
- 'Creates' the site. The logic of HTML is to mimic a document.
- The 'DOM' (Document Object Model) is the in-memory representation of an HTML Document. We will interact with this A LOT.
- Everything in tags (Called 'Elements')
  - Some tags need an open and closing tag.
  - Some tags are self-closing (input)
- All tags have attributes.
- URL stands for 'Uniform Resourace Locator'

#### Atributes

- Attributes go in a tag to provide additional information.
- Examples include: src, alt, class, id, height, width, style, and many more.

#### Specific Examples

- "a" tags store links.
- "img" is for adding images. It is a self-closing tag. You will put the file path or image in the 'src=""' part of the tag.
- Everything lives between "htm""tags
- "Head" tags contain website information. The only tag in this section the viewer sees is "title", which contains the name of the page (for the tab or window)
- "Body" is what the user sees. Various tags.
- "Div"
  - Divides the body into divisions (sections).
  - Divs are containers - you can put many things inside of them. They wrap around other elements.
  - No predefined space - we can assign that. They take up as much space as we let them; we have to contain them.
- "iframe" tags allow you to put pages inside of pages. They can contain media!
- "br" tags provide a line break
- "h1, h2, h3, etc" provide different layers of headings, with 1 being the largest and stepping down.
- "button" creates a clickable button
- "strong" and "b" creates a bolded text
- "emphasis" creates an italicized view
- "input" receives user input
- "marquee" tag creates a text that moves across the screen.

### What makes HTML Complex

- Making sure your app and website runs on multiple devices. Unlike Python running on Python, our websites have to show up on multiple devices that operate on multiple operating systems.
- Making sure your website is optimized for search engines and features that those engines provide (text-to-speech, etc)

### Points to Emphasize

- **Depricated Tags are no longer used or supported! Do not use them in your pages.**

- **Breaking HTML is very difficult. Every mistake with show up.**

- **Our apps will be mobile-responsive. We will typically program mobile-first**

## CSS Notes

- CSS is "Cascading Style Sheets"
- CSS is used to modify the way a webpage looks.
- You can target an element with attributes. A few of these attributes include "class" and "id".

### Adding CSS to a page

- You can add CSS to a page three ways:

  1. Inline style format:

  - Adds CSS to a **specific** element
  - Include the CSS code in the 'style=""' attribute.
  - You can add multiple CSS elements to a HTML tag.
  - This is considered not good practice in most situations.

  2. You can use the "style" tag in the "head" seciton of the HTML.

  - You can make all of one kind of element a certain style (like "paragraph").

  3. You can create a class in the style section and apply that class to any tag using the "class = '' " attribute.

  4. You can link a CSS styling sheet to your html page by using the "link" tag in the "head" section of the HTML document.

### Points to Emphasize

- Styles in CSS will apply top down (hence "cascading")
- You can override a style by typing "!important" on the style you want to apply.
- If you have the CSS loaded in the head, it will populate before the elements. If you load it in the body, it will populate after the elements and "differ"
- Study more here, possible interview question: https://medium.com/@schizdazzle/whats-with-putting-the-css-in-the-head-24888fbbd2e2#:~:text=So%20the%20point%20of%20putting,than%20later%20in%20the%20process.
