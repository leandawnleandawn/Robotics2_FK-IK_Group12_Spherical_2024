# Robotics 2 Laboratory 1: Forward and Inverse Kinematics of a Spherical Manipulator
## Proponents:

 Dianne Mae Ortega
 Ivan Russ Oxillo
 Jancen Mendoza
 Lyndon Allen Sales

 ## Objectives:
   To perform the Forward and Inverse Kinematics of the Spherical Manipulator

## Theory:
  When dealing with Mechanical Manipulators (Arm-Type Robots/ Leg-Type Robots), the main objective of the Robotics Engineer is to 
  design the following robot with its dinstinctive joints and the position on the following space. One method to know about that is
  the use of **Forward and Inverse Kinematics**
### Forward Kinematics
  It is defined forward because we tend to assign joint variables to know where the following robot is in the given space (SE(3)). It is
  known by the following formmula:

  $$\begin{bmatrix}
  Rot & Pos \\
  0 & 1
  \end{bmatrix}$$

  Where the $Rot$ is the rotation matrix of the frame of the end effector to its world frame, and the $Pos$ is the position of the two frames
  between the end effector and its world frame. The row vector [0  1] act as a scoping on the following manipualtor itself

#### DH-Parameters
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

### Inverse Kinematics
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

## Procedure Forward Kinematics:
 <ol>
 <li>Draw the kinematic diagram with labels of the Spherical Manipulator.	</li>
 <li>Assign frames using D-H Frame Rules.</li>
 <li>Obtain the Parametric Table.</li>
 <li>Program the Forward Kinematics in Python and MATLAB.</li>
 <li>Perform the experimentation of comparing the position vector from the Python program to the MATLAB program.</li>
 <li><ol>Provide the following as output of the experiment:
 <li>Kinematic Diagram with labels and frames.</li>
 <li>Parametric Table</li>
 <li>MATLAB and Python</li>
 <li>5 trials in table for the comparison of Forward Kinematics in MATLAB and Python</li>
 </ol></li>
 </ol>

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
 
</ol>

 
</ol>
 
