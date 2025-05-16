---
title: "Intrinsic and extrinsic curvature approximation with distributional finite elements"
collection: portfolio
---

In several applications, such as shells, general relativity, geometric flows, and cell membranes, the curvature of surfaces and Riemannian manifolds plays a fundamental role. In discrete differential geometry (DDG), algorithms to approximate curvature quantities of discretized domains have been intensively investigated. Many of these procedures rely on computing angles, such as the dihedral angle to approximate the shape operator on polyhedral surfaces or the angle defect for the Gauss curvature of surfaces and two-dimensional Riemannian manifolds. Rigorous convergence analysis and extension to high-order methods can be difficult or unfeasible in this setting. By embedding DDG into a FEM context, rigorous numerical analysis tools become available to investigate and extend those algorithms. To this end, so-called distributional finite elements are essential. They entail weak regularity such that differential operators must be understood in the sense of distributions.

For intrinsic curvatures of (pseudo-)Riemannian manifolds with corresponding metric tensor, the question arises for a given approximation of a metric tensor, how close is the discrete curvature to the exact one? Moreover, how to define the nonlinear curvature on such a discrete metric, which is, in general, non-smooth. It turned out that Regge finite elements are the appropriate space to approximate metrics. They are symmetric, matrix-valued, and only their tangential-tangential components are continuous over element interfaces. We were able to define and analyze the Gauss curvature for 2D manifolds [[2023](https://michaelneunteufel.github.io/publication/2023-GNSW-Analysis-o), [2024](https://michaelneunteufel.github.io/publication/2024-GNSW-On-the-Imp)], the scalar curvature for arbitrary dimensional manifolds [[2024](https://michaelneunteufel.github.io/publication/2024-GN-Finite-Ele)], the Einstein tensor [[2025](https://michaelneunteufel.github.io/publication/2025-GN-Finite-Ele)] (for arbitrary dimension), and recently the full Riemann curvature tensor in any dimension [[2024](https://michaelneunteufel.github.io/publication/2024-GNSW-Generalizi)], which is a fourth-order tensor encoding all intrinsic curvature information of a (pseudo-)Riemannian manifold. Future applications include geometric flows and especially numerical relativity, solving the Einstein field equations of general relativity. We successfully used the Regge elements to construct a simple and general method to avoid membrane locking in nonlinear shells.

NGSolve add-on package for differential geometry support, especially for Riemannian manifolds: [NGSDiffGeo](https://github.com/MichaelNeunteufel/NGSDiffGeo).

<table style="border-collapse: collapse; border: none;">
<tr style="border: none;">
<td style="border: none;">
<center>
<img width="50%" src='/images/portfolio/lin_curv.png'>
</center>
</td>
<td style="border: none;">
<center>
<img width="50%" src='/images/portfolio/quad_curv.png'>
</center>
</td>
</tr>
<tr style="border: none;">
 <td colspan="2" class="cap foot" style="border: none;">
 Approximated Gauss curvature on a polyhedral surface and a surface with quadratically curved elements.
 </td>
 </tr>
</table>

We extended the concept of the dihedral angle from DDG to approximate the shape operator (Weingarten tensor) on an arbitrarily approximated surface embedded in $$\mathbb{R}^3$$. The distributional shape operator acts on Hellan--Herrmann--Johnson finite elements as test functions. We successfully applied the distributional shape operator to compute the curvature of cell membranes and for the bending term of nonlinear shells. A rigorous numerical analysis and convergence is a work in progress.

<table style="border-collapse: collapse; border: none;">
<tr style="border: none;">
<td style="border: none;">
<div style="position: relative; left: 0; top: 0;">
<img width="90%" src='/images/portfolio/rbc_nu_0_55.png'> 
</div>
</td>
<td style="border: none;">
<div style="position: relative; left: 0; top: 0;">
<img width="100%" src='/images/portfolio/oblate_12_045.jpg'>
</div>
</td>
<td style="border: none;">
<div style="position: relative; left: 0; top: 0;">
<img width="100%" src='/images/portfolio/prolate_12_055.jpg'>
</div>
</td>
</tr>
<tr style="border: none;">
 <td colspan="3" class="cap foot" style="border: none;">
 Mean curvature on quadratically curved surfaces.
 </td>
 </tr>
</table>