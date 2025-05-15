---
title: "On Pressure Robustness and Independent Determination of Displacement and Pressure in Incompressible Linear Elasticity"
authors: 'Zdunek, Neunteufel, Rachowicz'
collection: publications
category: manuscripts
permalink: /publication/2023-ZNR-On-Pressur
date: 2023-01-01
venue: 'Computer Methods in Applied Mechanics and Engineering'
paperurl: 'https://doi.org/10.1016/j.cma.2022.115714'
bibtexurl: 'http://michaelneunteufel.github.io/files/bibtex/ZNR2023.bib'
arxivurl: 'https://arxiv.org/abs/2207.02615'
---
We investigate the possibility to determine the divergence-free displacement u independently from the pressure reaction p for a class of boundary-value problems in incompressible linear elasticity. If not possible, we investigate if it is possible to determine it pressure robustly, i.e. pollution free from the pressure reaction. For convex domains there is but one variational boundary value problem among the investigated that allows the independent determination. It is the one with essential no-penetration conditions combined with homogeneous tangential traction conditions. Further, for the investigated cases, the weakly divergence-free displacement can be computed pressure robustly provided the total body force is decomposed into its direct sum of divergence- and rotation-free components using the Helmholtz decomposition. The elasticity problem is solved using these components as separate right-hand sides. The total solution is obtained using the superposition principle. We employ a (u,p) higher-order finite element formulation with discontinuous pressure elements. It is inf--sup stable for polynomial degree $$p\geq2$$ but not pressure robust by itself. We propose a three step procedure to solve the elasticity problem which includes by the Helmholtz decomposition of the total body force. The extra cost for the three-step procedure is essentially the cost for the Helmholtz decomposition of the assembled total body force, and the small cost of solving the elasticity problem with one extra right-hand side. The results are corroborated by theoretical derivations as well as numerical results.