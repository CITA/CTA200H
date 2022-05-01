# CTA200 2021 Computing Information Sheet

Welcome to the CITA Computing Course (CTA200) for 2022! If you have signed up for the course or let us know that you want to audit, you should have received an email with information about a computer account and related instructions (including a Secret; if not, please let Norm or Fergus know. This Information sheet provides some information to get you started with the CITA computing resources.

For more information, please visit the CITA Wiki at [http://wiki.cita.utoronto.ca](https://wiki.cita.utoronto.ca/index.php/Welcome_to_the_CITA_Wiki).

You will need your CITA or CTA200 login credentials to access the wiki.

For the ses of this course, most laptops will provide sufficient compute power, but for your research projects over the summer you will probably require more. This may be in the form of a server (like lobster on the CITA network), a cluster (like CITA's Sunnyvale) or a national-scale machine like SciNet's Niagara.

To access any of these you will need a secure login facility; all the machines just named, and most large systems, use ssh for logins, often with some form of Two-factor Authentication. Here we describe the CITA setup, but other systems are similar.

## Remote Access with Two-factor Authentication
Remote ssh logins must go through the CITA gateway machine `gw.cita.utoronto.ca`. The gateway
requires your username and password along with a 6-digit verication code to login. The Google Authenticator (GAuth) app provides a code that changes every 30 seconds. You will need to install GAuth in a
browser or on your smartphone to generate these codes.

**Browser Instructions**
1. Open a browser at this URL: `https://gauth.cita.utoronto.ca`
2. Click on the pencil icon in the upper right and then the `+Add` button. Enter CITA Account name and type in or cut and paste your Secret key. Your Secret key can be found in the Account info sheet that has been emailed to you.
3. You can delete the EXAMPLE key if you wish---we recommend that you do so.

**Smartphone Instructions**
1. Install the Google Authenticator app on your smartphone (search Google Play or the App Store).
2. Add your Secret key by taking a picture of the QR code or type it in.

Once you have logged into the gateway, you can then ssh login from there to other CITA servers and the cluster to conduct your research. Servers include lobster, homard, kingcrab, and mussel, in addition to cosmo1 to cosmo4.


## Password Change
Open a terminal to log in to the CITA gateway `gw.cita.utoronto.ca` and change your password to something private immediately following these steps:

```
ssh username@gw.cita.utoronto.ca
/cita/local/bin/passwd
# enter old password
# enter new password and confirm
exit
```
On Windows computers, the PowerShell includes an ssh client so use that for your terminal. On Linux and Mac computers, open a terminal app.

## Remote Access with CITA VPN
CITA provides a virtual private network (VPN) connection which simplies remote access to CITA computers and services. Once set up on your remote computer, you can login directly to CITA computers without using the gateway, copy data with scp, sftp or rsync and access the software license server. It is the best way to gain access to CITA remotely.

Read here to learn how to set it up: [http://wiki.cita.utoronto.ca/index.php/CITA_Remote_Access](http://wiki.cita.utoronto.ca/index.php/CITA_Remote_Access).


## Access CITA Computing System remotely from your home computer

A server is assigned to you based on your birthday:
```
cosmo1.cita.utoronto.ca:6 (Jan, Feb, Mar)
cosmo2.cita.utoronto.ca:6 (Apr, May, Jun)
cosmo3.cita.utoronto.ca:6 (Jul, Aug, Sep)
cosmo4.cita.utoronto.ca:6 (Oct, Nov, Dec)
```
1. You will need to set up a Virtual Network Computing (VNC) connecting to cosmo servers. VNC works with Windows, Macs and Linux computers or laptops. The detailed instructions for setting up a VNC desktop are available here: [http://wiki.cita.utoronto.ca/index.php/VNC_Remote_Desktop](http://wiki.cita.utoronto.ca/index.php/VNC_Remote_Desktop).


2. After setting up VNC, you can connect to the remote desktop on one of the cosmo servers from your home computer. You will have to install a VNC client, for example TigerVNC or RealVNC for Mac and OpenVNC for Linux.


**Please destroy the sheet of paper with username and password after password change.**

## Course Material

The course homepage is [https://github.com/CITA/CTA200H].  
Material for the first lecture, Scientific computing workflow in Linux, can be accessed from the folder [lecture_1_linux_git](https://github.com/CITA/CTA200H/tree/master/lecture_1_linux_git). Material for the rest of the course is available online at [https://github.com/CITA/CTA200H](). To follow the exercises you should copy the material to your computer with

`git clone https://github.com/CITA/CTA200H.git`

## Software Environment

CITA servers run Linux CentOS 6 and 7 and come with the usual compilers (gcc, gfortran, icc, ifort), python, scientific software including Matlab, Mathematica (limited number of licenses), IDL, and libraries such as OpenMPI, fftw, gsl and much more. Multiple versions of most libraries exist according to need and are activated using the **modules** environment. For example, to view the available modules type:

`module avail`

and to load a particular set of modules type e.g.,

`module load gcc/11.2.0 python/3.10.2`

This would load version 11.2.0 of the gnu compilers along with version 3.10.2 of Python. You can see which modules are currently loaded by typing:

`module list`

Type `module` alone to see the various options available with the module command.

Please refer to article [the CITA Computing Wiki](https://wiki.cita.utoronto.ca) for more instrcutions on using the computer system.