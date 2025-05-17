---
title: "Nonlinear shell analysis"
collection: portfolio
---

To simulate thin-walled structures, where one direction is significantly smaller than the others, a dimension reduction leads to surface shell equations. Shells have a wide range of industrial applications and are an active research field. Their numerical solution with the finite element method is essential. Motivated by discrete differential geometry we used a distributional Weingarten tensor acting on Hellan--Herrmann--Johnson finite elements, we developed locking-free mixed finite element methods for nonlinear Koiter shells [[2019](https://michaelneunteufel.github.io/publication/2019-NS-The-Hellan), [2021](https://michaelneunteufel.github.io/publication/2021-N-Mixed-Fini), [2024](https://michaelneunteufel.github.io/publication/2024-NS-The-Hellan)] and extended the tangential-displacement and normal-normal stress continuous (TDNNS) method from linear Reissner--Mindlin plates to nonlinear Naghdi shells [[2024](https://michaelneunteufel.github.io/publication/2024-NS-The-Hellan)]. With the structure-preserving finite elements, our methods can handle non-smooth shell structures such as kinked and branched shells. 



<table style="border-collapse: collapse; border: none;">
<tr style="border: none;">
<td style="border: none;">
<center>
<img width="80%" src='/images/portfolio/shell_2.png'>
</center>
</td>
<td style="border: none;">
<center>
<img width="80%" src='/images/portfolio/kink_2.png'>
</center>
</td>
</tr>
<tr style="border: none;">
 <td colspan="2" class="cap foot" style="border: none;">
A cantilever beam under a bending moment rolling up and a T-cantilever under a shear force (modulus of the bending tensor displayed).
 </td>
 </tr>
</table>


Interpolating the membrane strain fields into so-called Regge finite elements led to a generally applicable method to avoid membrane locking [[2021](https://michaelneunteufel.github.io/publication/2021-NS-Avoiding-M)].

<table style="border-collapse: collapse; border: none;">
<tr style="border: none;">
<td style="border: none;">
<center>
<img width="70%" src='/images/portfolio/plot_hyperboloid2_p1_lin.pdf'>
</center>
</td>
<td style="border: none;">
<center>
<img width="70%" src='/images/portfolio/plot_hyperboloid2_p1_lin_reg.pdf'>
</center>
</td>
</tr>
<tr style="border: none;">
 <td colspan="2" class="cap foot" style="border: none;">
Displacement error with respect to the number of elements of a shell for different thicknesses. Left: Locking. Right: No locking with Regge interpolation.
 </td>
 </tr>
</table>

Recently, we investigated the Babu&scaron;ka or plate paradox, where convergence fails when a domain with curved boundary is approximated by polygonal domains in linear bending problems with simple support boundary conditions. We showed that the paradox also occurs for a nonlinear bending-folding model which enforces vanishing Gaussian curvature, and it can be cured by cutting the interface edges [[2025](https://michaelneunteufel.github.io/publication/2025-BBHN-Babuvska's)]. 

<table style="border-collapse: collapse; border: none;">
<tr style="border: none;">
<td style="border: none;">
<center>
<img width="90%" src='/images/portfolio/experiment_paradox.png'>
</center>
</td>
</tr>
<tr style="border: none;">
<td style="border: none;">
<center>
<img width="90%" src='/images/portfolio/simulation_paradox.png'>
</center>
</td>
</tr>
<tr style="border: none;">
 <td colspan="2" class="cap foot" style="border: none;">
Babu&scaron;ka paradox in an experiment (top) and simulation (bottom, the modulus of the bending stress is displayed).
 </td>
 </tr>
</table>


In many applications, thin shell-like structures are integrated within or attached to volumetric bodies. This includes reinforcements placed in soft matrix material in lightweight structure design, or hollow structures partially or completely filled. We successfully coupled our shell method with nonlinear solid mechanics to simulate such structures in an efficient and locking-free manner [[2025](https://michaelneunteufel.github.io/publication/2025-PN-Direct-Cou)].