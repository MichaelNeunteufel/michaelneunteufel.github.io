---
title: "Shape optimization"
collection: portfolio
---

In several problems in industry and medicine, including the optimal design of aircraft, electric motors, or electric impedance tomography, an optimal shape with respect to a given objective function under constraints is searched for. Shape optimization problems involve the shape derivative
of possibly lengthy and complicated expressions. We implemented an automated shape differentiation tool in the open-source finite element software [NGSolve](https://www.ngsolve.org), enabling shape gradient and shape Newton methods without the need to compute the shape derivative by hand [[2021](https://michaelneunteufel.github.io/publication/2021-GSNS-Fully-and-)]. In addition, this makes using non-Lagrangian finite elements in shape optimization problems more attractive, where additional space-dependent transformation rules have to be differentiated.

<table style="border-collapse: collapse; border: none;">
<tr style="border: none;">
<td style="border: none;">
<center>
<img width="90%" src='/images/portfolio/canti_w2p5_f200_iter00.jpg'>
</center>
</td>
<td style="border: none;">
<center>
<img width="90%" src='/images/portfolio/canti_w2p5_f200_iter15.jpg'>
</center>
</td>
</tr>
<tr style="border: none;">
 <td colspan="2" class="cap foot" style="border: none;">
Initial and optimized geometry of a cantilever under vertical force on the right side using a St. Venant–Kirchhoff model in nonlinear elasticity.
 </td>
 </tr>
</table>


We have successfully applied this framework to minimize the Canham--Helfrich--Evans (CHE) bending energy in the context of cell membranes [[2023](https://michaelneunteufel.github.io/publication/2023-NSS-Numerical-)]. The method used to reduce the fourth-order problem to a mixed second-order problem turned out to be fruitful in combination with the theory of shape optimization.


<table style="border-collapse: collapse; border: none;">
<tr style="border: none;">
<td style="border: none;">
<center>
<img width="80%" src='/images/portfolio/spont_curv1_2.png'>
</center>
</td>
<td style="border: none;">
<center>
<img width="80%" src='/images/portfolio/spont_curv2_2.png'>
</center>
</td>
</tr>
<tr style="border: none;">
 <td colspan="2" class="cap foot" style="border: none;">
Two solutions of the CHE energy with different nonzero spontaneous curvatures. Colors indicate the modulus of the mean curvature of the shapes.
 </td>
 </tr>
</table>