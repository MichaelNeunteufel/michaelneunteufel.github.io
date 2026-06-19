---
title: "Locking-free mixed finite element methods for thin-walled and nearly incompressible nonlinear continuum mechanics"
collection: talks
type: "Talk"
permalink: /talks/2026-07-21-WCCM-ECCOMAS
venue: "WCCM-ECCOMAS 2026"
date: 2026-07-21
location: "Munich, Germany"
---

Upcoming: The slides will be provided soon.

<h2>Abstract:</h2>
In continuum mechanics, locking effects may arise when anisotropic elements are used to discretize thin-walled structures (shear locking) or when simulating nearly incompressible materials such as rubber (volumetric locking). In the small-strain regime, mixed two-field finite element formulations that introduce the stress tensor as an additional unknown have been successfully developed to alleviate locking. The tangential-displacement normal-normal-stress (TDNNS) method [1] was proven to be robust with respect to anisotropic structures and, when combined with a stabilization term, also with respect to volumetric locking. The mass-conserving mixed stress (MCS) method [2], frequently used for the (Navier-)Stokes equations, is robust in the incompressible limit. A key ingredient of both approaches is the use of displacement and stress finite elements with reduced inter-element continuity compared to nodal finite elements. The reduced regularity, however, poses severe challenges for extending these methods to the nonlinear regime, as gradients must be interpreted in the sense of distributions.

In this talk, we present novel extensions of the TDNNS and MCS methods to the finite-strain regime using a Hu-Washizu three-field formulation, adding the strain as an additional unknown [3,4]. We demonstrate through several benchmark problems that the robustness of these methods with respect to anisotropic structures and nearly incompressible materials is preserved in the nonlinear setting. All methods are implemented in the open-source finite element library NGSolve (www.ngsolve.org).

[1] Pechstein, A. and Schöberl, J., Tangential-displacement and normal-normal-stress continuous mixed finite elements for elasticity, Mathematical Models and Methods in Applied Sciences, 21(8), 1761-1782, 2011.
[2] Gopalakrishnan, J., Lederer, P. L., and Schöberl, J., A mass conserving mixed stress formulation for the Stokes equations, IMA Journal of Numerical Analysis, 40(3), 1838-1874, 2020.
[3] Neunteufel, M., Pechstein, A. S., and Schöberl, J., Three-field mixed finite element methods for nonlinear elasticity, Computer Methods in Applied Mechanics and Engineering, 382, 113857, 2021.
[4] Fu, G., Neunteufel, M., Schöberl, J., and Zdunek, A., A four-field mixed formulation for incompressible finite elasticity, Computer Methods in Applied Mechanics and Engineering, 444, 118082, 2025.