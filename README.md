# Robotics 2 Laboratory 1: Forward and Inverse Kinematics of a Spherical Manipulator

## Abstract:

## Introduction:

## Degrees of Freedom of the Spherical Mechanical Manipulator:

## Kinematic Diagram and DH-Frame Assignments of Spherical Mechanical Manipulator

## Denavit-Hartenberg Parametric Table of Spherical Mechanical Manipulator
  Jacques Denavit and Richard Hartenberg created a standardized set of parameters to be able to shorthand the computation of the spatial linkages
  These are known to be as the Denavit Hartenberg Notation:

  This is noted by the following steps:
 <ol>
  <li>Assigning the Joint Variables and Links of the Mechanical Manipulator ($\theta_{n}$ for Revolute, $d_{n}$ for prismatic joint, $a_{n}$ for links)</li>
   <li><ul>Assigning the Framees of the Mechanical Manipulator
       <li>Define the $z_n$ as the axis of rotation of the revolute joint of the line of translation of prismatic joint</li>
       <li>Define the $x_n$ as orthogonal to $z_n$ and $z_{n-1}$</li>
       <li>The $x_n$ must be perpendicular to $z_{n-1}$, if not, it must be rotated across $z_n$ or translated across $z_n$</li>
       <li>$y_n$ is followed via Right Hand Rule </li>
   </ul></li>
   <li><ul> Assigning the following DH Parameters 
     <li>$/theta$ is the rotation of the frame n-1 across $z_{n-1}$ to match from $x_n$ to $x_{n-1}$, plus the joint variable $/theta_n$ if it has revolute joint. This is known as the Joint Angle</li>
     <li>$/alpha$ is the rotation of the frame n-1 across $x_{n}$ to match from $z_n$ to $z_{n-1}$, This is known as the Twist Angle.</li>
     <li>$r$ is the distance between frame n-1 and n across $x_n$. This is known as the Joint Offset </li>
     <li>$d$ is the distance between frame n-1 and n across $z_{n-1}$, plus the joint variable $d_n$ if it has a prismatic joint. This is known as the Link Length (Do not confuse with Link Length of the Mechanical Manipulator)</li>
   </ul></li>
   <li> Creating the following DH Homogenous Transformation Matrix defined as 
   $$\begin{bmatrix}
   cos(\theta_{n}) & -sin(\theta_{n})*cos(\alpha_{n}) & sin(\theta_{n})*sin(\alpha_{n}) & r_{n}*cos(\theta_{n}) \\
   sin(\theta_{n}) & cos(\theta_{n})*cos(\alpha_{n}) & -cos(\theta_{n})*sin(\alpha_{n}) & r_{n}*sin(\theta_{n}) \\
   0 & sin(\alpha_{n}) & cos(\alpha_{n}) & d_{n} \\
   0 & 0 & 0 & 1
   \end{bmatrix}$$
   </li>
   <li> Getting the Dot Product of all Homogenous Transformation Matrix together </li>
</ol>

## Homogenous Transformation Matrix of Spherical Mechanical Manipulator

## Inverse Kinematics of Spherical Mechanical Manipulator
If the following Forward Kinematics focuses on the joint variables to find the position vector. The following Inverse Kinematics is the opposite, where we find the joint variables of the system via the use of position vector.
 The most effective method of solving the Inverse Kinematics is Numerical Methods, however this is accurate however this is compicated to compute. Graphical Method is the best method of solving Serial Manipulators, however, One must consider the implications of having
 a undefined Solutions. 
#### Inverse Kinematics Graphical Method
 When solving the Inverse Kinematics of the Serial manipulator, we are using the foundations of Trignometry. The following approaches are the following:
 <ul>
  <li>Trigonometric Ratios</li>
  <li>Law of Cosines</li>
  <li>Pythagorean Theorem</li>
 </ul>

## Procedure Inverse Kinematics:
<ol>
<li>Derive the Spherical Manipulator inverse kinematics solution using graphical method.</li>
<li>Program the Inverse Kinematics in Python.</li>
<li>Perform the experimentation of comparing the position vector and joint variables from the Python program to the MATLAB program.</li>
<li><ol>Provide the following as output of the experiment:
<li>Written derivation of the inverse kinematics using graphical method.</li>
<li>Python Code</li>
<li>5 trials in table for the comparison of Inverse Kinematics in MATLAB and Python</li>
</ol></li>

## Forward and Inverse Kinematics Graphical User Interface (GUI) Calculator of Spherical Manipulator:

## References
 
## D-H Parametric table of Spherical Manipulator
</ol>

![421668234_403017508989038_658074442315959319_n](https://github.com/leandawnleandawn/Robotics2_FK-IK_Group12_Spherical_2024/assets/157699815/008f5e5c-eb10-42e5-ae67-f461739e19a0)

 
</ol>

## Inverse Kinematics of Spherical Manipulator
<ol>
 
![421995649_1149281762738087_6404656819298399393_n](https://github.com/leandawnleandawn/Robotics2_FK-IK_Group12_Spherical_2024/assets/157699815/811c303b-9367-422e-a1a8-efcbe1089e5e)

</ol>
 
## Proponents:

 Dianne Mae Ortega
 
 Ivan Russ Oxillo
 
 Jancen Mendoza
 
 Lyndon Allen Sales
