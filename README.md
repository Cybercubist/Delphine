# Delphine
**The task**: Create a small lightweighted platform for fast 1-page texts analysis. Texts are going to be on financial topic. It should be handy for everyday use.

**The solution**: We've created a simple platform based on spaCy library / API. There are few features:

**1. Input module.** Allows you copy and paste text into platform.<br> 
**2. Data extraction module.** Returns following data as dict:<br>
&nbsp;&nbsp;&nbsp;&nbsp;a) Noun counting. Extracts all nouns from text and rank them by their frequency.<br>
&nbsp;&nbsp;&nbsp;&nbsp;b) Entities exctraction. Finds all the enteties in text (dates, organizations, money, percents).<br>
&nbsp;&nbsp;&nbsp;&nbsp;c) Chunks. Finds all word chunks.<br>
**3. Visualization module.** Returns entered text with some spaCy-based visualization (with highlighted entities).<br>
**4. Text analysis module.** Allows you to find sentences in text cointaining information you are interested in.<br>

All the modules are made in MVP style, and may be significantly improved later. We've created a clear and simple architecture for future feature improvement.

**Current version:** <ins>Delphine 1.0.0.</ins> Delphine has it's own version number since 27.11.2023.

**Updates:**

<ins>17.11.2023:</ins>
1. Added "find sentence" function. Now you can find a sentence which contains words, entities, numbers or chunks you are interested in.
2. Small architecture improvements. Data extraction part and visualization part are now in separated cells. Lists (for example trash token list) are now in a separated file.  
