---
title: "Direct Coupling of Continuum and Shell Elements in Large Deformation Problems"
authors: 'Pechstein, Neunteufel'
collection: publications
category: preprints
permalink: /publication/2025-PN-Direct-Cou
date: 2025-01-01
venue: '2501.05251'
arxivurl: 'https://doi.org/10.48550/arXiv.2501.05251'
bibtexurl: 'http://michaelneunteufel.github.io/files/bibtex/pechsteinDirectCouplingContinuum2025.bib'
---
In many applications, thin shell-like structures are integrated within or attached to volumetric bodies. This includes reinforcements placed in soft matrix material in lightweight structure design, or hollow structures that are partially or completely filled. Finite element simulations of such setups are highly challenging. A brute force discretization of structural as well as volumetric parts using well-shaped three-dimensional elements may be accurate, but leads to problems of enormous computational complexity even for simple models. One desired alternative is the use of shell elements for thin-walled parts, as such a discretization greatly alleviates size restrictions on the underlying finite element mesh. However, the coupling of different formulations within a single framework is often not straightforward and may lead to locking if not done carefully. Neunteufel and Sch&ouml;berl proposed a mixed shell element where, apart from displacements of the center surface, bending moments are used as independent unknowns. These elements were not only shown to be locking free and highly accurate in large-deformation regime, but also do not require differentiability of the shell surface. They can directly be coupled to classical volume elements of arbitrary order by sharing displacement degrees of freedom at the center surface, thus achieving the desired coupled discretization. As the elements can be used on unstructured meshes, adaptive mesh refinement based on local stress and bending moments can be used. We present computational results that confirm exceptional accuracy for problems where thin-walled structures are embedded as reinforcements within soft matrix material.