Name:           ros-jade-orocos-kinematics-dynamics
Version:        1.3.1
Release:        0%{?dist}
Summary:        ROS orocos_kinematics_dynamics package

Group:          Development/Libraries
License:        LGPL
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-orocos-kdl
Requires:       ros-jade-python-orocos-kdl
BuildRequires:  ros-jade-catkin

%description
This package depends on a recent version of the Kinematics and Dynamics Library
(KDL), distributed by the Orocos Project. It is a meta-package that depends on
kdl which contains the c++ version and pykdl which contains the generated python
bindings.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Tue Apr 05 2016 Orocos Developers <orocos-dev@lists.mech.kuleuven.be> - 1.3.1-0
- Autogenerated by Bloom

* Tue Jan 13 2015 Orocos Developers <orocos-dev@lists.mech.kuleuven.be> - 1.3.0-0
- Autogenerated by Bloom

