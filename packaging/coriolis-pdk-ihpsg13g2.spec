%define debug_package %{nil}

%global python3_pkgversion 3.11
%if 0%{?rhel} >= 9 || 0%{?fedora} >= 39
%global python3_pkgversion 3
%endif
%if 0%{?is_opensuse}
%global python3_pkgversion 311
%endif

Name:           coriolis-pdk-ihpsg13g2
Version:        2024.10.15
Release:        <CI_CNT>.<B_CNT>.bfa7190
Summary:        IHP Open PDK SG13G2
License:        Apache-2.0
%if 0%{?is_opensuse}
Group:          Productivity/Scientific/Electronics
%endif
URL:            https://github.com/IHP-GmbH/IHP-Open-PDK
Source0:        coriolis-pdk-ihpsg13g2-2024.10.15.tar.gz
Source1:        venv-al9-2.5.5.tar.gz
Source2:        patchvenv.sh
Source10:       %{name}-rpmlintrc

BuildArch:      x86_64
Requires:       coriolis-eda
BuildRequires:  openvaf
%if 0%{?rhel} || 0%{?fedora}
BuildRequires:  ninja-build
BuildRequires:  pyproject-rpm-macros
%endif
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  python3-wheel
%if "%{python3_pkgversion}" != "3"
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-wheel
%endif

%if 0%{?is_opensuse}
%global _pyproject_wheeldir %{_builddir}/coriolis-pdk-ihpsg13g2-%{version}/build
%global python3_sitearch /usr/lib64/python3.11/site-packages

BuildRequires:  meson
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
%endif

# ALmaLinux 8
%if 0%{?rhel} == 8
%global python3_sitearch /usr/lib64/python3.11/site-packages

BuildRequires:  python%{python3_pkgversion}-rpm-macros
%endif

# ALmaLinux 9
%if 0%{?rhel} >= 9 || 0%{?fedora} >= 39
BuildRequires:  python-unversioned-command
BuildRequires:  python3-build
%endif


%global _description %{expand:
130nm  BiCMOS Open  Source PDK,  dedicated for  Analog/Digital, Mixed
Signal and RF Design

IHP Open  Source PDK project  goal is to  provide a fully  open source
Process  Design Kit  and related  data, which  can be  used to  create
manufacturable  designs at  IHP’s facility.   As of  March 2023,  this
repository is targeting the SG13G2 process node}


%description
%_description


%package -n python%{python3_pkgversion}-coriolis-pdk-ihpsg13g2
Summary:        %{summary}


%description -n python%{python3_pkgversion}-coriolis-pdk-ihpsg13g2
%_description


%prep
%autosetup -p1 -n coriolis-pdk-ihpsg13g2-%{version} -a 1


%build
 cp $RPM_SOURCE_DIR/patchvenv.sh .
 chmod u+x patchvenv.sh
 patchVEnvArgs="--use-system-packages --remove-pip"
 if [    \( 0%{?fedora} -ge 39 \) \
      -o \( 0%{?rhel}   -eq  8 \) \
      -o \( 0%{?suse_version}%{?sle_version} -ne 0 \) ]; then
   patchVEnvArgs="${patchVEnvArgs} --remove-venv-watchfiles"
 fi
 ./patchvenv.sh ${patchVEnvArgs}
 source .venv/bin/activate
 #pip list
 %__mkdir_p %{_pyproject_wheeldir}
 python3 -m pip wheel --no-deps --no-cache-dir \
	 --disable-pip-version-check --progress-bar off --verbose \
         --no-build-isolation --no-clean \
         --wheel-dir=%{_pyproject_wheeldir} \
	 .
 echo "Current (build)"
 ls -alh .
 echo "build (build)"
 ls -alh %{_pyproject_wheeldir}


%install
 source .venv/bin/activate
 echo "Current (install)"
 ls -alh .
 echo "build (install)"
 ls -alh %{_pyproject_wheeldir}
%if 0%{?is_opensuse}
 python3 -m pip install --root %{buildroot} --prefix %{_prefix} --no-deps \
	 --disable-pip-version-check --progress-bar off --verbose \
	 --ignore-installed --no-warn-script-location \
	 --no-index --no-cache-dir %{_pyproject_wheeldir}/`ls %{_pyproject_wheeldir}`
%else
%{pyproject_install}
%endif
 find %{buildroot} -type d


%files -n python%{python3_pkgversion}-coriolis-pdk-ihpsg13g2
%doc AUTHORS CHANGELOG.md README.md CODE_OF_CONDUCT.md CONTRIBUTING.md
%license LICENSE
%dir %{python3_sitearch}/pdks
%{python3_sitearch}/pdks/ihpsg13g2
%{python3_sitearch}/coriolis_pdk_ihpsg13g2*dist-info


%changelog
* Wed Nov  6 2024 Jean-Paul Chaput <Jean-Paul.Chaput@lip6.fr> - 2024.10.15-1
- Initial packaging.
