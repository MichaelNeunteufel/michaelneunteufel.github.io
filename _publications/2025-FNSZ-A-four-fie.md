---
title: "A four-field mixed formulation for incompressible finite elasticity"
authors: 'Fu, Neunteufel, Sch&ouml;berl, Zdunek'
collection: publications
category: manuscripts
permalink: /publication/2025-FNSZ-A-four-fie
date: 2025-09-01
venue: 'Computer Methods in Applied Mechanics and Engineering'
paperurl: 'https://doi.org/10.1016/j.cma.2025.118082'
bibtexurl: 'http://michaelneunteufel.github.io/files/bibtex/fu2025fourfieldmixedformulationincompressible.bib'
arxivurl: 'https://arxiv.org/abs/2503.00989'
---
In this work, we generalize the mass-conserving mixed stress (MCS) finite element method for Stokes equations [Gopalakrishnan J., Lederer P., and Sch&ouml;berl J., A mass conserving mixed stress formulation for the Stokes equations, IMA Journal of Numerical Analysis 40(3), 1838-1874 (2019)], involving normal velocity and tangential-normal stress continuous fields, to incompressible finite elasticity. By means of the three-field Hu-Washizu principle, introducing the displacement gradient and 1st Piola-Kirchhoff stress tensor as additional fields, we circumvent the inversion of the constitutive law. We lift the arising distributional derivatives of the displacement gradient to a regular auxiliary displacement gradient field. Static condensation can be applied at the element level, providing a global pure displacement problem to be solved. We present a stabilization motivated by Hybrid Discontinuous Galerkin methods. A solving algorithm is discussed, which asserts the solvability of the arising linearized subproblems for problems with physically positive eigenvalues. The excellent performance of the proposed method is corroborated by several numerical experiments.

[Supplementary code](https://doi.org/10.5281/zenodo.14927329)