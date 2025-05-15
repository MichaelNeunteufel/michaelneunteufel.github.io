---
title: "Primal and Mixed Finite Element Formulations for the Relaxed Micromorphic Model"
authors: 'Sky, Neunteufel, Muench, Sch&ouml;berl, Neff'
collection: publications
category: manuscripts
permalink: /publication/2022-SNMSN-Primal-and
date: 2022-09-01
venue: 'Computer Methods in Applied Mechanics and Engineering'
paperurl: 'https://doi.org/10.1016/j.cma.2022.115298'
bibtexurl: 'http://michaelneunteufel.github.io/files/bibtex/SNMSN2022.bib'
arxivurl: 'https://arxiv.org/abs/2202.08715'
---
The classical Cauchy continuum theory is suitable to model highly homogeneous materials. However, many materials, such as porous media or metamaterials, exhibit a pronounced microstructure. As a result, the classical continuum theory cannot capture their mechanical behaviour without fully resolving the underlying microstructure. In terms of finite element computations, this can be done by modelling the entire body, including every interior cell. The relaxed micromorphic continuum offers an alternative method by instead enriching the kinematics of the mathematical model. The theory introduces a microdistortion field, encompassing nine extra degrees of freedom for each material point. The corresponding elastic energy functional contains the gradient of the displacement field, the microdistortion field and its Curl (the micro-dislocation). Therefore, the natural spaces of the fields are $$[H^1]^3$$ for the displacement and $$[H(\mathrm{curl})]^3$$ for the microdistortion, leading to unusual finite element formulations. In this work we describe the construction of appropriate finite elements using N&eacute;d&eacute;lec and Raviart--Thomas subspaces, encompassing solutions to the orientation problem and the discrete consistent coupling condition. Further, we explore the numerical behaviour of the relaxed micromorphic model for both a primal and a mixed formulation. The focus of our benchmarks lies in the influence of the characteristic length $$L_c$$ and the correlation to the classical Cauchy continuum theory.