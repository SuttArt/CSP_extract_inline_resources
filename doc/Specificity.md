# Specificity

Specificity is the algorithm used by browsers to determine the CSS declaration that is the most relevant to an element, which in turn, determines the property value to apply to the element. The specificity algorithm calculates the weight of a CSS selector to determine which rule from competing CSS declarations gets applied to an element. [MDN Web Docs - Specificity](https://developer.mozilla.org/en-US/docs/Web/CSS/Specificity)

| **Selector** | **Examples** | **Weight** |
|--------------|--------------|------------|
| ID selectors **(= a)** | `#example` | 1-0-0 |
| Class selectors, attributes selectors, and pseudo-classes **(= b)** | `.myClass`, `[type="radio"]`, `[lang="fr"]`, `:hover`, `:nth-of-type(3n)`, `:required` | 0-1-0 |
| Type selectors and pseudo-elements **(= c)** | `p`, `h1`, `td`, `::before`, `::placeholder` | 0-0-1 |
| Universal selector | `*`, `:where()` | 0-0-0 |

### Additional tools
| **Tool** | **Examples** | **Weight** |
|----------|--------------|------------|
| Inline styles | `style="font-weight: bold;"` | 1-0-0-0 |
| !important | `p { color: red !important;}` | The only way to override inline styles is by using !important |

Examples:
```css
*               /* a=0 b=0 c=0 -> specificity =   0 */
li              /* a=0 b=0 c=1 -> specificity =   1 */
ul li           /* a=0 b=0 c=2 -> specificity =   2 */
ul ol+li        /* a=0 b=0 c=3 -> specificity =   3 */
h1 + *[rel=up]  /* a=0 b=1 c=1 -> specificity =  11 */
ul ol li.red    /* a=0 b=1 c=3 -> specificity =  13 */
li.red.level    /* a=0 b=2 c=1 -> specificity =  21 */
#x34y           /* a=1 b=0 c=0 -> specificity = 100 */
#s12:not(FOO)   /* a=1 b=0 c=1 -> specificity = 101 */
```

**Note:**  
Combinators, such as `+`, `>`, `~`, `" "`, and `||`, may make a selector more specific in what is selected but they don't add any value to the specificity weight.  
The negation pseudo-class, `:not()`, itself has no weight. Neither do the `:is()` or the `:has()` pseudo-classes.

### More Specific = Greater Precedence
If the selectors are the same, then the last one will always take precedence.

```css
/* myStyle.css */

p { color: red }
p { color: blue }
```

The text in the box of `p` elements would be colored blue because that rule came last. [HTML Dog - Specificity](https://www.htmldog.com/guides/css/intermediate/specificity/)

### Inline styles:
Inline styles added to an element (e.g., `style="font-weight: bold;"`) always overwrite any normal styles in author stylesheets, and therefore, can be thought of as having the highest specificity. Think of inline styles as having a specificity weight of 1-0-0-0. [MDN Web Docs - Specificity - Inline Styles](https://developer.mozilla.org/en-US/docs/Web/CSS/Specificity#inline_styles)

### !important:
Using `!important` to override specificity is considered a **bad practice** and should be avoided for this purpose. Understanding and effectively using specificity and the cascade can remove any need for the `!important` flag. [MDN Web Docs - Specificity - !important](https://developer.mozilla.org/en-US/docs/Web/CSS/Specificity#the_!important_exception)

### Sources:
- https://www.w3schools.com/css/css_specificity.asp
- https://developer.mozilla.org/en-US/docs/Web/CSS/Specificity
- https://www.htmldog.com/guides/css/intermediate/specificity/
- https://www.w3.org/TR/selectors-3/#specificity
