# Evidence and Knowledge

This document includes instructions and knowledge questions that must be completed to receive a *Competent* grade on this portfolio task.

## 1. Required evidence

### 1.1. Answer all questions in this document

- Each answer should be complete, well-articulated, and within the specified word count limits (if added) for each question.
- Please make sure **all** external sources are properly cited.
- You must **use your own words**. Please include your full chat transcripts if you use generative AI in any way.
- Generative AI hallucinates, is not an authoritative source

### 1.2. Make all the required modifications to the code

- Please follow the instructions in this document to make the changes needed to the code.

- When requested to upload evidence, upload all screenshots to `screenshots/` and embed them in this document. For example:

```markdown
![Example Running Code](screenshots/screenshot1.png)
```

![Sample](screenshots/sample.png)
> Note the `!`, and the use of a relative path.

- You must upload the code into your GitHub repository.
- While you can use a branch, your code should be in main when you submit.
- Upload a zip of this repository to Blackboard when you are ready to submit.
- You will be notified of your result via Blackboard
- However, if using GitHub classrooms, you may also receive additional feedback on GitHub directly

### 1.3. Optional: Use of Raspberry Pi and SenseHat

Raspberry Pi or SenseHat is **optional** for this activity. You can use the included `sense_hat.py` file to simulate the SenseHat on your computer.

If you use a Pi, please **delete** the `sense_hat.py` file.

### 1.4. Accessible version of the code

This project relies on visual patterns that appear on an LED matrix. If you have any accessibility requirements, you can use the `udl/accessible` branch to complete the project. This branch provides an accessible code version that uses text-based patterns instead of visual ones.

Please discuss this with your lecturer before using that branch.

## 2. Specific Tasks & Questions

Address the following tasks and questions based on the code provided in this repository.

### 2.1. Set up the project locally

1. Fork this repository (if not using GitHub Classrooms)
2. Clone your repository locally
3. Run the project locally by executing the `main.py` file
4. Evidence this by providing screenshots of the project directory structure and the output of the `main.py` file

![output-mainpy.png](screenshots%2Foutput-mainpy.png)

If you are running on a Raspberry Pi, you can use the following command to run the project and then screenshot the result:

```bash
ls
python3 main.py
```

### 2.2. Fundamental code comprehension

 Answer each of the following questions **as they relate to that code** supplied by in this repository (ignore `sense_hat.py`):

1. Examine the code for the `smiley.py` file and provide  an example of a variable of each of the following types and their corresponding values (`_` should be replaced with the appropriate values):

   | Type                    | name   | value                       |
   | ----------              |--------|-----------------------------|
   | built-in primitive type | dimmed | True                        |
   | built-in composite type | pixels | (0, 0, 0), (255, 255, 0)... |
   | user-defined type       | Smiley | Class                       |

>>REFERENCE 
> 
> Python Software Foundation. (2024). Built-in types. Python 3.13.3 documentation. https://docs.python.org/3/library/stdtypes.html


2. Fill in (`_`) the following table based on the code in `smiley.py`:

   | Object                   | Type   |
   | ------------             |--------|
   | self.pixels              | List   |
   | A member of self.pixels  | Tuple  |
   | self                     | Object |

>>REFERENCE
> 
> Python Software Foundation. (2024). Built-in types. In Python 3.13.3 
> documentation. https://docs.python.org/3/library/stdtypes.html

3. Examine the code for `smiley.py`, `sad.py`, and `happy.py`. Give an example of each of the following control structures using an example from **each** of these files. Include the first line and the line range:

   | Control Flow | File      | First line | Line range |
   | ------------ |-----------|------------|------------|
   |  sequence    | smiley.py | 13         | 21         |
   |  selection   | happy.py  | 31         | 31         |
   |  iteration   | sad.py    | 15         | 17         |



4. Though everything in Python is an object, it is sometimes said to have four "primitive" types. Examining the three files `smiley.py`, `sad.py`, and `happy.py`, identify which of the following types are used in any of these files, and give an example of each (use an example from the code, if applicable, otherwise provide an example of your own):

   | Type                    | Used?     | Example                 |
   | ----------------------- |-----------|-------------------------|
   | int                     | smiley.py | 255 (inside the tuples) |
   | float                   | happy.py  | delay                   |
   | str                     | sad.py    | "draws" (in doc string) |
   | bool                    | happy.py  | wide_open               |

5. Examining `smiley.py`, provide an example of a class variable and an instance variable (attribute). Explain **why** one is defined as a class variable and the other as an instance variable.

> YELLOW is a class variable while self.pixels is a instance variable
> YELLOW is a class variable because it is shared by all Smiley objects,
> while every object can have its own set of pixels.

6. Examine `happy.py`, and identify the constructor (initializer) for the `Happy` class:
   1. What is the purpose of a constructor (in general) and this one (in particular)?

> A constructor is a special method that runs when an object is created.
>In general, it sets up the object with initial values or actions.
> Specifically In happy.py, the constructor (__init__) calls the parent 
> constructor using super().__init__() to set the background for the happy 
> face.
   >

   2. What statement(s) does it execute (consider the `super` call), and what is the result?

   >super().__init__() creates the Sense Hat object and sets the pixels for 
   > the smiley background using different colors for each pixel, 
   > based on the class’s properties.

### 2.3. Code style

1. What code style is used in the code? Is it likely to be the same as the code style used in the SenseHat? Give to reasons as to why/why not:

> The code uses the PEP8 style, and It's likely to be the same used in the 
> SenseHat
> Frist because it's a public library and most public libraries follow this 
> style
> Second to stay consistent and readable
>>>REFERENCE
>van Rossum, G., Warsaw, B., & Coghlan, N. (2001). PEP 8 – Style Guide for 
> Python Code. Python Software Foundation. Retrieved May 23, 2025, from 
>https://peps.python.org/pep-0008/
> 
> Answered translated from portuguese:
> O código utiliza o estilo PEP8, que é o padrão para escrever códigos Python
> de forma limpa e organizada.
>É provável que a biblioteca SenseHat também siga o PEP8, pois é uma biblioteca
> oficial do Python e a maioria das bibliotecas públicas segue esse estilo 
> para manter consistência e legibilidade.

2. List three aspects of this convention you see applied in the code.

> 1 - Indentation with 4 spaces is used in method and loop blocks
> 
> 2 - Variable and method names use snake case, like draw_mouth and self.pixel
> 
>3 - Spaces are used around assignment and comparison operators, like in self.sense_hat = SenseHat()

3. Give two examples of organizational documentation in the code.
>Docstrings
> 
> Comments

### 2.4. Identifying and understanding classes

> Note: Ignore the `sense_hat.py` file when answering the questions below

1. List all the classes you identified in the project. Indicate which classes are base classes and which are subclasses. For subclasses, identify all direct base classes.
  
  Use the following table for your answers:

| Class Name  | Super or Sub? | Direct parent(s) |
|-------------|---------------|------------------|
| Smiley      | Super         | none             |
| Sad         | Sub           | Smiley           |
| Happy       | Sub           | Smiley, Blinkable|  
 |Blinkable   | Super         | Not yet created  |

2. Explain the concept of abstraction, giving an example from the project (note "implementing an ABC" is **not** in itself an example of abstraction). (Max 150 words)

> Abstraction means exposing only the essential features of an object 
> while hiding the internal complexity
>In methods, abstraction helps the user by hiding multiple small steps 
> inside a clean and simple function 
>so they don’t have to understand how it works internally.
> In classes abstraction allows developers to define high-level structures that represent concepts in the real world, 
> without revealing the complex implementation behind them, making systems 
> easier to design, extend, and maintain.
> 
>>>REFERENCE
> 
> Kramer, J. (2007). Is abstraction the key to computing? Communications of the ACM, 50(4), 36–42. https://doi.org/10.1145/1232743.1232764)

3. What is the name of the process of deriving from base classes? What is its purpose in this project? (Max 150 words)

> Inheritance
> 
> Purpose of using inheritance in this project:
> 
> PORTUGUESE:
> Neste projeto, a herança tem o propósito de criar novas versões do Smiley 
> com diferentes características visuais (como olhos e boca) e comportamentos como o método blink. As subclasses Sad e Happy herdam atributos e métodos da superclasse Smiley, o que evita repetição de código e permite reaproveitar a estrutura básica do rosto. Além disso, a integração com o SenseHat é centralizada na superclasse, servindo como base para que todas as expressões funcionem corretamente no dispositivo.
> 
> ENGLISH:
> In this project, inheritance is used to create new versions of the Smiley with different visual features such as eyes and mouth and behaviors such as the blink method. The subclasses Sad and Happy inherit attributes and methods from the Smiley superclass, which helps avoid code repetition and allows reusing the base structure of the face. In addition, the integration with the SenseHat is handled in the superclass, serving as a foundation that ensures all expressions work properly on the device.



### 2.5. Compare and contrast classes

Compare and contrast the classes Happy and Sad.

1. What is the key difference between the two classes?
   > Happy inherits both form Smiley and blinkable, while sad only inherits 
   > from Smiley class
2. What are the key similarities?
   > Both inherit from Smiley Class
   > 
   >Both use the same method to customize the face
   > 
   > Both set the pixel colors using the same class variables like self.
   > blank e self.yellow

3. What difference stands out the most to you and why?
   > For me the difference that stands out the most is the fact that the 
   > Happy class uses time to add motion to the happy face
   >
4. How does this difference affect the functionality of these classes
   > Its difference affects functionality by giving Happy dynamic behavior 
   > through the blink method, making it more interactive
   >

### 2.6. Where is the Sense(Hat) in the code?

1. Which class(es) utilize the functionality of the SenseHat?
   >  Smiley, Sad, and Happy all utilize the functionality of the SenseHat.
   >
2. Which of these classes directly interact with the SenseHat functionalities?
   > Only the Smiley class directly interacts with the SenseHat by creating the object and calling its methods.
   >
3. Discuss the hiding of the SenseHAT in terms of encapsulation (100-200 Words)
   > In object-oriented programming, encapsulation is used to hide the internal details of how something works and only expose what is necessary. In this project, the SenseHat object is created and managed inside the Smiley class. This means other classes like Happy and Sad don’t need to know how the SenseHat works or how it is set up. They simply use the methods from Smiley, such as show or setting pixels, without directly accessing the hardware. This protects the code from bugs and makes it easier to change or improve the SenseHat integration later, without needing to modify every class. It also keeps the responsibilities clear: Smiley handles the hardware, while subclasses focus on the face expression logic.
   > 
   >PORTUGUESE: Na programação orientada a objetos, o encapsulamento é 
   > usado para esconder os detalhes internos de como algo funciona e expor 
   > apenas o que é necessário. Neste projeto, o objeto SenseHat é criado e 
   > controlado dentro da classe Smiley. Isso significa que outras classes, 
   > como Happy e Sad, não precisam saber como o SenseHat funciona ou como 
   > ele é configurado. Elas apenas utilizam os métodos herdados de Smiley, 
   > como exibir a imagem ou definir os pixels, sem interagir diretamente 
   > com o hardware. Isso protege o código contra erros e torna mais fácil 
   > modificar ou melhorar a integração com o SenseHat no futuro, sem 
   > precisar alterar cada classe individualmente e tambem mantém as 
   > responsabilidades bem definidas por exemplo Smiley cuida da interação 
   > com o hardware, enquanto as subclasses focam na lógica da expressão facial

### 2.7. Sad Smileys Can’t Blink (Or Can They?)

Unlike the `Happy` smiley, the current implementation of the `Sad` smiley does not possess the ability to blink. Let's first explore how blinking has been implemented in the Happy Smiley by examining the blink() method, which takes one argument that determines the duration of the blink.

**Understanding Blink Mechanism:**

1. Does the code's author believe that every `Smiley` should be able to blink? Explain.

> No, the author does not believe that every Smiley should be able to blink.
>This is shown by the fact that only the Happy class includes the blink 
> method, and not the Smiley or Sad classes.
>If blinking were meant for all smileys, the blink method would likely be 
> placed in the Smiley class instead.
>

2. For those smileys that blink, does the author expect them to blink in the same way? Explain.

> Yes, the author expects all smileys that blink to do it in the same way.
>This is because the blink method is written once in the Happy class and 
> uses a single delay value with the time module.
>

3. Referring to the implementation of blink in the Happy and Sad Smiley classes, give a brief explanation of what polymorphism is.

> Polymorphism is the ability of different classes to use the same method name 
> but perform different actions.
>In this project, if both Happy and Sad had a method called blink, each 
> could define it in their own way.
>This allows us to call blink on any smiley object, and it would behave 
> according to the class it belongs to
>

4. How is inheritance used in the blink method, and why is it important for polymorphism?

> Inheritance is used in the blink method because the Happy class inherits from Smiley, 
> which provides the pixel data, color constants, and the show method.
>The blink method itself is written in Happy, but it relies on the 
> structure and behavior inherited from Smiley to work.
>This is important for polymorphism because other smiley classes could also 
> define their own blink method, using the same base from Smiley but with different behaviors.
>
1. **Implement Blink in Sad Class:**

   - Create a new method called `blink` within the Sad class. Ensure you use the same method signature as in the Happy class:
   
>>>def blink(self, delay=0.25):
> 
    """
    Blinks the eyes of the sad smiley twice.

    :param delay: Delay between closing and opening the eyes
    """
    for blink in range(2):
        self.draw_eyes(wide_open=False)
        self.show()
        time.sleep(delay)

        self.draw_eyes(wide_open=True)
        self.show()
        time.sleep(delay)



2. **Code Implementation:** Implement the code that allows the Sad smiley to blink. Use the implementation from the Happy Smiley as a reference. Ensure your new method functions similarly by controlling the blink duration through the `delay` argument.

3. **Testing the Implementation:**

- Test the new blink functionality on your Raspberry Pi or within the Python classes provided. You might need to adjust the `main.py` script to incorporate Sad Smiley's new blinking capability.

Include a screenshot of the sad smiley or the modified `main.py`:

!![img.png](screenshots%2Fimg.png)[img.png](img.png)

- Observe and document the Sad smiley as it blinks its eyes. Describe any adjustments or issues encountered during implementation.

> When I made the blink method for the Sad smiley, I made it blink two times using the same method name and structure as in the Happy class.
>At first, the eyes did not work right because the draw_eyes method was 
> changing the list of eye positions by mistake.
>To fix it, I rewrote draw_eyes to keep the eye positions and the eye color 
> separate, which made the code easier to read and worked better.
>After the fix, the Sad smiley blinked just like expected, closing and 
> opening both eyes two times with a small delay between.
>Even though the method name is the same as in Happy, the behavior is 
> different, which shows how polymorphism works.

  ### 2.8. If It Walks Like a Duck…

  Previously, you implemented the blink functionality for the Sad smiley without utilizing the class `Blinkable`. Assuming you did not use `Blinkable` (even if you actually did), consider how the Sad smiley could blink similarly to the Happy smiley without this specific class.

  1. **Class Type Analysis:** What kind of class is `Blinkable`? Inspect its superclass for clues about its classification.

> Blinkable is an abstract class because it inherits from ABC and has an abstract method called blink.
>This means it does not have real code for blinking, but it tells other 
> classes that if they want to be blinkable, they must create their own blink method.
>It is like a rule or a contract that other classes must follow.

  2. **Class Implementation:** `Blinkable` is a class intended to be implemented by other classes. What generic term describes this kind of class, which is designed for implementation by others? **Clue**: Notice the lack of any concrete implementation and the naming convention.



  3. **OO Principle Identification:** Regarding your answer to question (2), which Object-Oriented (OO) principle does this represent? Choose from the following and justify your answer in 1-2 sentences: Abstraction, Polymorphism, Inheritance, Encapsulation.

> The Blinkable class represents abstraction because it defines what a blinkable object should do, 
> without providing the actual code.
> It hides the implementation details and only shows the required behavior.

  4. **Implementation Flexibility:** Explain why you could grant the Sad Smiley a blinking feature similar to the Happy Smiley's implementation, even without directly using `Blinkable`.

>The generic term for this kind of class is interface.
>It defines a set of methods that other classes must implement, without 
> giving any real code.
>Blinkable works like an interface because it tells other classes that if they 
> want to be blinkable, they MUST have a blink method.

  5. **Concept and Language Specificity:** In relation to your response to question (4), what is this capability known as, and why is it feasible in Python and many other dynamically typed languages but not in most statically typed programming languages like C#? **Clue** This concept is hinted at in the title of this section.

>>In Python, a class does not need to say it uses another class like Blinkable.
>If it has a method called blink, that is enough.
>Python checks this when the program is running, not before.
>This works because Python is a dynamic language.
>But in languages like C Sharp, the class must say clearly that it uses an 
> interface, or the code will not work.
>>>REFERENCE
>>>
>>>Python Software Foundation. (n.d.). Typing — Type hints. Python 3 
>>> documentation. Retrieved May 23, 2025, from https://docs.python.
> org/3/library/typing.html#duck-typing

  ***

  ## 3. Refactoring

  ### 3.1. Does a Smiley Have to Be Yellow?

  While our current implementation predominantly features yellow smileys, emotional expressions like sickness or anger typically utilize colors like green, red, or orange. We'll explore the feasibility of integrating these colors into our smileys.

  1. **Defined Colors and Their Location:**

     1. Which colors are defined and in which class(s)?
        > The colors WHITE, GREEN, RED, YELLOW, BLANK are defined in the Smiley class.
No other class (Happy or Sad) defines any new colors.
They all reuse the colors inherited from Smiley.
     2. What type of variables hold these colors? Are the values expected to change during the program's execution? Explain your answer.
        > These colors are class variables, also known as constants.
They are written in uppercase and defined outside of any method, so they belong to the class and are shared by all instances.
The values are not expected to change during the program because they represent fixed RGB values used to draw the smiley faces.
     3. Add the color blue to the appropriate class using the appropriate format and values.
     >BLUE = (0, 0, 255) - at class Smiley


  2. **Usage of Color Variables:**

     1. In which classes are the color variables used?
        > The color variables are used in the Smiley, Happy, and Sad classes.
Smiley uses them to define the pixel background, and both Happy and Sad use them to draw the eyes and mouth based on different expressions

  3. **Simple Method to Change Colors:**
  4. What is the easiest way you can think to change the smileys to green? Easiest, not necessarily the best!
     > The easiest way is to replace all uses of self.YELLOW with self.GREEN in the Smiley class.
This will change the default face color of all smileys to green without changing the structure of the code.

  Here's a revised version of the "Flexible Colors – Step 1" section for the smiley project, incorporating your specifications for formatting and content updates:

  ### 3.2. Flexible Colors – Step 1

  Changing the color of the smileys once is straightforward, but it isn't very flexible. To facilitate various colors for smileys, it is advisable not to hardcode values in any class. This approach was identified earlier as a necessary change. Let's start by removing the built-in assumptions about color in our classes.

  1. **Add a method called `complexion` to the `Smiley` class:** Implement this instance method to return `self.YELLOW`. Using the term "complexion" instead of "color" provides a more abstract terminology that focuses on the meaning rather than implementation.

  2. **Refactor subclasses to use the `complexion` method:** Modify any subclass that directly accesses the color variable to instead utilize the new `complexion` method. This ensures that color handling is centralized and can be easily modified in the future.

  3. **Determine the applicable Object-Oriented principle:** Consider whether Abstraction, Polymorphism, Inheritance, or Encapsulation best applies to the modifications made in this step.
>I believe this change shows Abstraction.
Instead of writing the color directly like self.YELLOW, we use the complexion() method to return it.
This hides the real color and just says "this is the face color", which makes it easier to change later.
Each smiley can have its own color by changing the method, not the whole code.
  4. **Verify the implementation:** Ensure that the modifications function as expected. The smileys should still display in yellow, confirming that the new method correctly replaces the direct color references.
![img_1.png](screenshots%2Fimg_1.png)
  This step is crucial for setting up a more flexible system for color management in the smiley display logic, allowing for easy adjustments and extensions in the future.

  ### 3.3. Flexible Colors – Step 2

  Having removed the hardcoded color values, we now enhance the base class to support dynamic color assignments more effectively.

  1. **Modify the `__init__()` method in the `Smiley` class:** Introduce a default argument named `complexion` and assign `YELLOW` as its default value. This allows the instantiation of smileys with customizable colors.

  2. **Introduce a new instance variable:** Create a variable called `my_complexion` and assign the `complexion` parameter to it. This step ensures that each smiley instance can maintain its own color state.

  3. **Rationale for `my_complexion`:** Using a distinct instance variable like `my_complexion` avoids potential conflicts with the method parameter names and clarifies that it is an attribute specific to the object.

  4. **Bulk rename:** We want to update our grid to use the value of complexion, but we have so many `Y`'s in the grid. Use your IDE's refactoring tool to rename all instances of the **symbol** `Y` to `X`. Where `X` is the value of the `complexion` variable. Include a screenshot evidencing you have found the correct refactor tool and the changes made.

  ![Bulk Rename](screenshots/bulk_rename.png)

  5. **Update the `complexion` method:** Adjust this method to return `self.my_complexion`, ensuring that whatever color is assigned during instantiation is what the smiley displays.

  6. **Verification:** Run the updated code to confirm that Smileys still defaults to yellow unless specified otherwise.

  ### 3.4. Flexible Colors – Step 3

  With the foundational changes in place, it's now possible to implement varied smiley colors for different emotional expressions.

  1. **Adjust the `Sad` class initialization:** In the `Sad` class's initializer method, change the superclass call to include the `complexion` argument with the value `self.BLUE`, as shown:

     ```python
     super().__init__(complexion=self.BLUE)
     ```

  2. **Test color functionality for the Sad smiley:** Execute the program to verify that the Sad smiley now appears blue.

  3. **Ensure the Happy smiley remains yellow:** Confirm that changes to the Sad smiley do not affect the default color of the Happy smiley, which should still display in yellow.

  4. **Design and Implement An Angry Smiley:** Create an Angry smiley class that inherits from the `Smiley` class. Set the color of the Angry smiley to red by passing `self.RED` as the `complexion` argument in the superclass call.

  ***
