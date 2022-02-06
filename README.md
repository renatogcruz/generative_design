[![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/Arquitetura-Aberta/info)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

# generative_design_mecom
Generative design in the design development of metallic constructions

### About

Repository of documents, experiments, codes and thesis carried out during the Master's Degree in Metallic Construction of the Department of Civil Engineering of the School of Mines of the Federal University of Ouro Preto, Brazil, as an integral part of the requirements to obtain the title of Master in Construction Metallic.

#### Abstrat

The architectural design is composed of innumerable variables, some of them contradictory, that need to be negotiated constantly. The genetic algorithms represent a technique that contribute to the solution of this type of problem, potentializing the search for better results. For this, it is enough that these are incorporated into the generative design system. The present work describes the construction of a system that combines parametric modeling strategies and genetic algorithms to optimize the total weight of a roof in metallic structure and of its surface as a potential area of photovoltaic energy generation. By means of a reformulation of the evolutionary Darwinian process, a systematization of a project process that allowed the architect to act in the parametrization of the problems, going beyond the mere formal proposition of solutions, in favor of the exploration of a greater variety of projective possibilities of what would be possible using traditional design methods. Thus, the objectives of this research are to evaluate the potential of the use of genetic algorithms as an auxiliary tool integrated to generative design as a design method. The review of the theoretical and practical content of the architecture approached the design practice in which the architect gives up the control of the specific definition of the solution to reach this greater variety of projects. As object of study, we tried to apply the studied process in an architectural design of metallic construction and its energetic potential. As a result, the project stands out as a practice in which the architect and the project dialogue in a flow of information that precedes the project itself, guided by common objectives. The experiments show that the loss of control in the final formulation of a response occurred through the mathematical modeling of the problem and the automatic search of solutions through heuristics. It also highlights a transdisciplinary approach that articulates theory and practice within thinking capable of intertwining specialties and overcoming frontiers in the production of knowledge.

**Key-words:** Generative design, Genetic algorithms, Structural optimization, Environmental optimization, Metallic construction.


### Theoretical reference

1. project as a question - [Caio Adorno Vassão](https://www.blucher.com.br/livro/detalhes/metadesign-620);

2. design and control - [Gaudí](https://en.wikipedia.org/wiki/Antoni_Gaud%C3%AD), [Otto](https://en.wikipedia.org/wiki/Frei_Otto) and [Spuybroek](https://www.nox-art-architecture.com/)

![](figures/readme_0.jpg)


3. design and nature - [Nagy](https://medium.com/generative-design/learning-from-nature-fe5b7290e3de), [Yang](https://www.researchgate.net/publication/235979455_Nature-Inspired_Metaheuristic_Algorithms), [Shiffman](https://natureofcode.com/)

4. design of the design - [Nagy](https://medium.com/generative-design/designing-measures-2c66a71b2ff3)

![](figures/readme_1.jpg)

### Tools

1. [rhinoceros](https://www.rhino3d.com/);

    - [grasshopper 3D](https://www.grasshopper3d.com/page/download-1);
    
      - [karamba 3D](https://www.karamba3d.com/);
        
      - [ladybug](https://www.ladybug.tools/);
      
2. [discover](https://github.com/danilnagy/discover_legacy).

### Strategy

1. construction of the design space;

2. development of measures to assess structural and environmental performance;

3. the application of evolutionary algorithms to search the design space and find high performance projects.

![](figures/readme_2.jpg)

### Implementation, experiments and applying the generative algorithm - the evolutionary solver [Discover](https://github.com/danilnagy/discover_legacy)

![](figures/readme_3.jpg)

![](figures/GA.gif)

### Analysis 

![](figures/readme_4.jpg)

![](figures/readme_5.jpg)

![](figures/readme_6.jpg)

![](figures/readme_7.jpg)

### Results

![](figures/readme_8.jpg)

### Suggestions for future work

The main suggestions for future work are the following suggestions:

1. The methodological development of this work through practical workshops as a reflection on the method adopted, in which it could be tested and discussed with students and professionals, in order to gauge how it would be received by the designers.

2. A deepening of the questions about who defines what is the problem, or what goes into that definition. This issue is important because when a problem is poorly formulated, the project does not solve the problem situation;

3. A greater opening of the design process. In addition to the other agents involved in the design (design partners), the project as a question also opens space to incorporate future users into the process. One of the ways would be to provide this system, more and more, of repertoires that direct it to the metadesign;

4. Finally, to approach, discuss and test this method adopting non-monetary criteria and parameters for choosing the optimal project. This would be an interesting challenge, since this work only adopted criteria (weight of the structure and energy generation potential) as objectives of the optimization procedures tested.

### Appendix

Click [here](https://github.com/renatogcruz/generative_design/blob/master/appendx.py).

### Research articles

[![DOI: 10.5151/sigradi2018-1631](https://zenodo.org/badge/DOI/10.5151/sigradi2018-1631.svg)](https://www.proceedings.blucher.com.br/article-details/29707) [Generative design in the design development of metallic constructions](http://www.proceedings.blucher.com.br/article-details/29707). Nov, 2018

Published in the XXII International Congress of the Ibero-American Society of Digital Graphics.


[![http://dx.doi.org/10.1590/s1678-86212021000400569](https://zenodo.org/badge/DOI/10.1590/s1678-86212021000400569.svg)][Generative design: information flow between genetic algorithm and parametric design in a steel structure construction](https://www.scielo.br/j/ac/a/f5dkBmGvDYV8hDNgxHRXxYz/abstract/?format=html&lang=en). Out./Dec. 2021

Published in Associação Nacional de Tecnologia do Ambiente Construído, ISSN 1678-8621, Porto Alegre, v. 21, n. 4, p. 271-289.


