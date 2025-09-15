---
title: "Intrinsic Mixed Finite Element Methods for Linear Cosserat Elasticity"
authors: 'Dziubek, Hu, Karow, Neunteufel'
collection: publications
category: manuscripts
permalink: /publication/2025-DHKN-Intrinsic-
date: 2025-08-01
venue: 'SIAM Journal on Numerical Analysis'
paperurl: 'https://doi.org/10.1137/24M1706578'
bibtexurl: 'http://michaelneunteufel.github.io/files/bibtex/dziubekIntrinsicMixedFinite2025.bib'
arxivurl: 'https://arxiv.org/abs/2410.14176'
---
We propose two parameter-robust mixed finite element methods for linear Cosserat elasticity. The Cosserat coupling constant $$\mu_c$$, connecting the displacement $$u$$ and rotation vector $$\omega$$, leads to possible locking phenomena in finite element methods. The formal limit of $$\mu_c\to\infty$$ enforces the constraint $$\frac{1}{2}\operatorname{curl}u = \omega$$ and leads to the fourth order couple stress problem. Viewing the linear Cosserat model as the Hodge-Laplacian problem of a twisted de Rham complex, we derive structure-preserving distributional finite element spaces, where the limit constraint is fulfilled in the discrete setting. Applying the mass conserving mixed stress (MCS) method for the rotations, the resulting scheme is robust in $$\mu_c$$. Combining it with the tangential-displacement normal-normal-stress (TDNNS) method for the displacement part we obtain additional robustness in the nearly incompressible regime and for anisotropic structures. Using a post-processing scheme for the rotations, we prove optimal convergence rates independent of the Cosserat coupling constant $$\mu_c$$. Further, we propose a mixed method for the couple stress problem based on the MCS scheme. We demonstrate the performance of the proposed methods in several numerical benchmark examples.