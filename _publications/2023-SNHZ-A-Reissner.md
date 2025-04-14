---
title: "A Reissner--Mindlin Plate Formulation Using Symmetric Hu-Zhang Elements via Polytopal Transformations"
authors: 'Sky, Neunteufel, Hale, Zilian'
collection: publications
category: manuscripts
permalink: /publication/2023-SNHZ-A-Reissner
date: 2023-11-01
venue: 'Computer Methods in Applied Mechanics and Engineering'
paperurl: 'https://doi.org/10.1016/j.cma.2023.116291'
bibtexurl: 'http://michaelneunteufel.github.io/files/bibtex/SNHZ2023.bib'
---
In this work we develop new finite element discretisations of the shear-deformable Reissner--Mindlin plate problem based on the Hellinger--Reissner principle of symmetric stresses. Specifically, we use conforming Hu-Zhang elements to discretise the bending moments in the space of symmetric square integrable fields with a square integrable divergence $$M \in \mathrm{HZ} \subset H_{\mathrm{sym}}(\mathrm{Div})$$. The latter results in highly accurate approximations of the bending moments M and in the rotation field being in the Lebesgue space $$\phi\in [L^2]^2$$, such that the Kirchhoff--Love constraint can be satisfied for $$t\rightarrow0$$. In order to preserve optimal convergence rates across all variables for the case $$t\rightarrow0$$, we present an extension of the formulation using Raviart--Thomas elements for the shear stress $$q\in \mathrm{RT} \subset H(\mathrm{div})$$. We prove existence and uniqueness in the continuous setting and rely on exact complexes for inheritance of well-posedness in the discrete setting. This work introduces an efficient construction of the Hu-Zhang base functions on the reference element via the polytopal template methodology and Legendre polynomials, making it applicable to hp-FEM. The base functions on the reference element are then mapped to the physical element using novel polytopal transformations, which are suitable also for curved geometries. The robustness of the formulations and the construction of the Hu-Zhang element are tested for shear-locking, curved geometries and an L-shaped domain with a singularity in the bending moments M. Further, we compare the performance of the novel formulations with the primal-, MITC- and recently introduced TDNNS methods.