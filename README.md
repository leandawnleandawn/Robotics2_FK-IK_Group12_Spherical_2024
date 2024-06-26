# Robotics 2 Midterm Project: Forward and Inverse Kinematics Grpahical User Interface of a Spherical Manipulator
#### Take note if the pictures are cannot be accessed, [click here](https://www.youtube.com/playlist?list=PLhWn3nOiDEfsU8u1udOJn3WJYmZ6HJU1k)
## Abstract:
  In this Industry 4.0, one must be expert on knowing the design, control, and planning the following
  Industrial Robots to make efficient and productive manufacturing processses in the Semiconductor, Logistics
  and other Fields. One must know the difficulty of integrating the different fields on creating such mechanical
  manipulator. In this repository, the members of the Company created a Graphical User Interface to give ease to
  operators and technician controlling the Industrial Robot. 
## Introduction:

  The challenges of robotics design are indeed formidable to engineers, especially those in mechatronics 
  and related fields who have an aim of creating autonomous systems for various uses notably in manufacturing 
  (Almurib et al., 2011). Nonetheless, Balestrino (1984) showed that it was not easy to control robots given 
  some roadblocks such as non-linearities, parametrizations and inaccuracies. 

  A major landmark in robotics was the work done by Victor Shiemann at Stanford University with the creation 
  of the Stanford Arm in 1969 (Moran, 2007). Originally meant for educational purposes, its configuration as 
  a spherical manipulator with three primary movements explains why it is considered a pioneering model. 

  In response to practical difficulties associated with manipulation of such systems, This repository presents 
  a project on developing a graphical user interface (GUI) for a spherical mechanical manipulator. 
  The objective of this interface is to facilitate calibration and control procedures so as to improve 
  efficiency and accuracy while using robotic manipulation. 

# TAKE NOTE: CLICK THE FOLLOWING IMAGE TO WATCH THE FOLLOWING VIDEO. MOST OF THE VIDEO FILES EXCEEDED GITHUB'S UPLOAD SIZE.

## Degrees of Freedom of the Spherical Mechanical Manipulator:

Video (Please Click the Image Below):
[![Degrees of Freedom](https://i.ytimg.com/vi/J21eMrKu4F8/maxresdefault.jpg)](https://youtu.be/J21eMrKu4F8)

Degrees of Freedom is defined as the number of the independent variables moving in a given system. Reminder that the Degrees
of Freedom is different based on what field is under with. In the subject of Robotics, it is the independent numbers of joints
that are independently moving in a given robotic system. 

We can usually classify it by the following joints (reference to Lynch and Park (2017)):

![image](https://github.com/leandawnleandawn/Robotics2_FK-IK_Group12_Spherical_2024/assets/83767299/918d7f1e-3161-4ae2-b9a7-545ca3b511f5)

We have Revolute, Prismatic and Helical Joint moving in one independent axis, while more complex joints such as Cylindrical and Unverisal having 
two independent motion, and Spherical 3 independent motions. These "Indepedent Motion" are what we call as "Degrees of Freedom". It is necessary
to find the DOF of the Manipulator as if it describes the mobility and verstality of the robot under certain environment conditions.

Grubler's Criterion is of the famous formula on finding the number of DOF of the given manipulator:

$$M = 6n - \Sigma^{m}_{i=1}(6-C_i)$$

Where $M$ is the Mobility of the System, $n$ is the number of links and $m$ is the number of joints. $C_i$ is the connectivity of the given joint itself.
The video explains how do we get the Degrees of Freedom of the System using the Grublers Formula.

## Kinematic Diagram and DH-Frame Assignments of Spherical Mechanical Manipulator
Video (Please Click the Image Below):
[![Kinematic Diagram](https://i.ytimg.com/vi/7ie01cTN80Y/maxresdefault.jpg)](https://youtu.be/7ie01cTN80Y)

The First Step on finding the Forward Kinematics of the System is by assigning the Frame of the following manipulator. We have 4 basic rules to follow for that:

<ol>
  <li>Assign the following Link Lengths and Joint Variables. $a_n$ is the convention for link length. $\Theta_n$ is for the Revolute joint. and $d$ is for the Prismatic Joint.</li>
  <li>$z_n$ must be the axis of rotation (if it is a revolute joint) or line of translation (if it is a prismatic joint).</li>
  <li>$x_n$ must be orthogonal to the $z_n$ and $z_{n-1}$</li>
  <li>For checking, $x_n$ must be intersect with $z_{n-1}$. If it wasn't<ul>
    <li>First, Rotate the current frame to match both axes.</li>
    <li>Last, Translate the current frame to its previous frame.</li>
  </ul></li>
</ol>

The Following Video shows how this Spherical Manipulator gets assigned its own frames.

## Denavit-Hartenberg Parametric Table of Spherical Mechanical Manipulator
Video (Please Click the Image Below):
[![Denavit-Hartenberg Parametric Table](https://i.ytimg.com/vi/AdVCETLDfT8/maxresdefault.jpg)](https://youtu.be/AdVCETLDfT8)

The Second step on finding the Forward Kinematics of the Given Manipulator is to find the Homogeneous Transformation Matrix
of the given system. HTM is mathematically defined as the following:

![image](https://github.com/leandawnleandawn/Robotics2_FK-IK_Group12_Spherical_2024/assets/83767299/4b47744e-e6ee-484a-8960-ab094259ce2e)

Where $R$ and $d$ are Rotation Matrix and Displacement Vector concatenate together into a single matrix. This defines the following.
To get more in-depth into the HTM, [you can watch it here](https://www.youtube.com/watch?v=4Y1_y9DI_Hw). To get things short, we can use the 
Denavit Hartenberg Convention of finding the HTM of a Manipulator.

The Origin of the Denvait Hartenberg Parameters is based on the two frame assumptions - Rule Number 2 and Rule Number 3. In this case, we 
can generalize the Homogeneous Transformation Matrix as described in Spong (2005):

$$A = Rot_{z,\Theta}Trans_{z,d}Rot_{x,\alpha}Trans_{x,\alpha}$$

Which has the following notation:
<ul>
  <li>$r$ (in other textbooks, this is $a$) is the link length. This describes the distance of the two frames across $x_n$</li>
  <li>$\alpha$ is the link twist. This describes the rotation of the $x_n$ to match $z_{n-1}$ to $z_n$</li>
  <li>$d$ is the link offset. This describes the distance of the two frames across $z_{n-1}$</li>
  <li>$\Theta$ is the joint angle. This describes the rotation of the $z_{n-1}$ to match $x_{n-1}$ to $x_n$</li>
</ul>

The Video above shows how can we find the DH Parameters of a Spherical Manipulator.

The Image below shows the Frame Assignement and the DH Parameters of the Spherical Manipulator.
![421668234_403017508989038_658074442315959319_n](https://github.com/leandawnleandawn/Robotics2_FK-IK_Group12_Spherical_2024/assets/157699815/008f5e5c-eb10-42e5-ae67-f461739e19a0)

## Homogeneous Transformation Matrix of Spherical Mechanical Manipulator
Video:
[![HTM](https://i.ytimg.com/vi/a2cQWwoLQ5U/maxresdefault.jpg)](https://youtu.be/a2cQWwoLQ5U)
From the original definition of the Homogeneous Transformation Matrix under the Denavit Hartenberg Convention, the set of parameters can be subsitute
in this matrix:

![image](https://github.com/leandawnleandawn/Robotics2_FK-IK_Group12_Spherical_2024/assets/83767299/4badcfc0-a7f2-469d-aea8-d40275d1b1e9)

In this Video the following parameters are being substituted on the video itself.
It is a 4x4 matrix that combines rotation and translation of an object in 3D space.

## Inverse Kinematics of Spherical Mechanical Manipulator
Video (Please Click the Image Below):
[![IKinGraphical](https://i.ytimg.com/vi/VUPBvH8MFUk/maxresdefault.jpg)](https://youtu.be/VUPBvH8MFUk)

While the Forward Kinematics focuses on finding the coordinates of the systems based on its end effectors. The Inverse Kinematics, verbosely, does the oppposite.
If the Forward Kinematics is mainly purpose is to simulate a mechanical manipulator. The Inverse Kinematics involves the control and manipulation of the end effector
and outputs the certain joint angles to move so. There are two different methods on solving Inverse Kinematics (1) Numerical Solution which involves Euler's Method,
and (2) Graphical Solution which uses Trigonometry on solving these videos.

The Video shows how can you solve the Inverse Kinematics Problem using the Graphical Method.

The Image below shows the computation of the Spherical Manipulator Inverse Kinematics via Graphical Method. 
![421995649_1149281762738087_6404656819298399393_n](https://github.com/leandawnleandawn/Robotics2_FK-IK_Group12_Spherical_2024/assets/157699815/811c303b-9367-422e-a1a8-efcbe1089e5e)

## Forward and Inverse Kinematics Graphical User Interface (GUI) Calculator of Spherical Manipulator:
Video (Please Click the Image Below):
[![Programming](https://i.ytimg.com/vi/ImiuId-Wszk/maxresdefault.jpg)](https://youtu.be/ImiuId-Wszk)

This video is explained by the programmer is to explain comprehensively how the Forward Kinematics, Inverse Kinematics, the Model created via Robotics Toolbox and the GUI using TKinter and TTKBootstrap.

### Additional Instructions (from your Programmer)

Hi! Your Programmer here. You might be interested on running `improved_main.py` however it raises some errors. I am here to cover all of that

#### Prerequisites

The following libraries needed for this are `numpy`, `roboticstoolbox-python`, `scipy`, `tkinter`, and `ttkbootstrap`. You need to run it on your terminal 
(Make sure Python is installed)
```
pip install rvc3python
pip install numpy
pip install scipy
pip install tkinter
pip install ttkbootstrap
```

### FAQs

Q: I am having a library error. What should I do?

A: run `pip uninstall <library_name>` and `pip install <library_name>` itself. 

Q: I do have python installed but I cannot run it on the command line

A: Check this video [here](https://www.youtube.com/watch?v=jIunQSnzs1Y). 

Q: Can I access it on other Operating Systems?

A: Yes, you can. Primarily, This program is used on Ubuntu or Debian-Based Systems, as long as you have Python on your Personal Computer.
It will run as it is

Further issues must raised using the Issues Tab of this repository so that we can see the problem and such.

Thank you.
## References:

 Moran, M. E. (2007). Evolution of robotic arms. Journal of Robotic Surgery, 1(2), 103–111. https://doi.org/10.1007/s11701-006-0002-x
 
 Balestrino, A., De Maria, G., & Sciavicco, L. (1984). Robust control of robotic manipulators. IFAC Proceedings Volumes, 17(2), 2435–2440. https://doi.org/10.1016/s1474-6670(17)61347-8
 
 Almurib, H. a. F., Al-Qrimli, H. F. A., & Kumar, N. (2012). A review of Application Industrial Robotic Design. Ninth International Conference on ICT and Knowledge Engineering. https://doi.org/10.1109/ictke.2012.6152387

 Spong, M. W., Hutchinson, S., & Vidyasagar, M. (2005). Robot modeling and control. John Wiley & Sons.

 Lynch, K. M., & Park, F. C. (2017). Modern robotics. Cambridge University Press.
 
## Proponents:

 Project Leader and Project Engineer:  Dianne Mae Ortega
 
 Project Supervisor:  Ivan Russ Oxillo
 
 Project Quality:  Jancen Mendoza
 
 Project Programmer:  Lyndon Allen Sales

