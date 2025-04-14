---
title: "Advanced Numerical Methods for Fluid Structure Interaction"
authors: 'Neunteufel'
collection: publications
category: thesis
permalink: /publication/2017-N-Advanced-N
date: 2017-01-01
venue: 'TU Wien'
thesisurl: 'https://doi.org/10.34726/hss.2017.47691'
bibtexurl: 'http://michaelneunteufel.github.io/files/bibtex/neunteufelAdvancedNumericalMethods2017.bib'
---
This thesis deals with the coupling of fluid dynamics with elastic solid structure, namely the Navier-Stokes equations and the nonlinear elastic wave equation, which is due to the different types of these PDEs a challenging problem. Two different discretizations for the Navier-Stokes equations are discussed: the popular Taylor-Hood elements and the H(div)-conforming Hybrid Discontinuous Galerkin method, which ensures exact divergence-freeness. For the elastic wave equation a standard Newmark method is used and a new H(curl)-conforming method is introduced. Therefore, an additional variable is needed: the time derivative of the momentum, which is in the dual space of H(curl). The Arbitrary Lagrangian Eulerian description is well understood for H1-conforming methods, where the mesh velocity appears in the Navier-Stokes equations. For H(div)-conforming schemes, however, the ALE method is more involved and an additional term appears, which plays a crucial role. The methods are implemented in NGS-Py, which is based on the finite element library Netgen/NGSolve and tested with proper examples.