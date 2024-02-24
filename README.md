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

