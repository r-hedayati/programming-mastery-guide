## Basic Syntax
These are the elements outlined in John Gruber’s original design document. All Markdown applications support these elements. Find some examples in [basic examples](#basic-examples) section. 



| **Element**     | **Markdown Syntax**                        |
|-----------------|--------------------------------------------|
| Heading         | # H1 ## H2 ### H3                          |
| Bold            | **bold text**                              |
| Italic          | *italicized text*                          |
| Blockquote      | > blockquote                               |
| Ordered List    | 1. First item 2. Second item 3. Third item |
| Unordered List  | - First item - Second item - Third item    |
| Code            | `code`                                     |
| Horizontal Rule | ---                                        |
| Link            | [sample website](https://www.example.com)  |
| Image           | ![caption](image.jpg)                      |

## Extended Syntax 
These elements extend the basic syntax by adding additional features. Not all Markdown applications support these elements. Find some examples in [extended examples](#extended-examples) section.

| **Element**                                    | **Markdown Syntax**                                                                                           |
|--------------------------------------------|------------------------------------------------------------------------------------------------------------|
| Table                                      | \| Syntax \| Description \| \| ----------- \| ----------- \| \| Header \| Title \| \| Paragraph \| Text \| |
| Fenced Code Block                          | ``` {   "firstName": "John",   "lastName": "Smith",   "age": 25 } ```                                      |
| Footnote                                   | Here's a sentence with a footnote. [^1]  [^1]: This is the footnote.                                       |
| Heading ID                                 | ### My Great Heading {#custom-id}                                                                          |
| Definition List                            | term : definition                                                                                          |
| Strikethrough                              | ~~The world is flat.~~                                                                                     |
| Task List                                  | - [x] Write the press release - [ ] Update the website - [ ] Contact the media                             |
| Emoji (see also Copying and Pasting Emoji from [emojipedia](https://emojipedia.org/)) | That is so funny! :joy:                                                                                    |
| Highlight                                  | I need to highlight these <mark>very important words</mark>.                                                        |
| Subscript                                  | H<sub>2</sub>O                                                                                                     |
| Superscript                                | X<sup>2</sup>                                                                                                      |

---

## Basic Examples

1. Headings
   1. Header 1 (H1)
      ># H1
   2. Header 2 (H2)
      >## H2
   3. Header 3 (H3)
      >### H3
2. Bold
   
   >**This is a bold text**
3. Italic 
    >*This is an italicized text*
4. Block quote
    >this is a blocked quote text
5. Ordered List / Unordered List
   1. Ordered
      1. First 
      2. Second
   2. Unordered 
       - test 1
       - test 2
6. Code
   
   `print("Hello World")`  
7. Horizontal Rule
   >---
8. Link
    >please click on this [link](https://www.example.com) 
9.  Image
    
    >![alt text](images/Markdown-logo.png)     

## Extended Examples

1.  Table
   
   |       | Col 1 | Col 2 |
   |:-----:|:-----:|:-----:|
   | Row 1 |   -   |   -   |
   | Row 2 |   -   |   -   |
2.  Fenced Code Block

      >``` {   "firstName": "Reza",   "lastName": "Hedayati",   "age": 28 } ```  
3.  Footnote

      >Here's a sentence with a footnote. [^1]  
      [^1]: This is the footnote.  

4.  Heading ID
   >### Sample Heading {#custom-id}
   >[Got to Sample Heading](#custom-id)

5.  Definition List
    ><dl>
    <dt><strong>Lower cost</strong></dt>
    <dd>The new version of this product costs significantly less than the previous one!</dd>
    </dl>

6.  Strikethorugh
    >~~The world is flat.~~ We now know that the world is round.
7.  Task List
    >- [x] Write the press release
    >- [ ] Update the website
    >- [x] Contact the media
8.  Emoji
    > :joy: 🎹
9.  Highlight
    >I need to highlight these <mark>very important words</mark>.
10. Subscript
    >H<sub>2</sub>O
11. Superscript
    >X<sup>2</sup> 



   
