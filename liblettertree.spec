%define	name	liblettertree
%define	version	0.1
%define	release	%mkrel 2
%define	major	0
%define	libname	%mklibname lettertree %major

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A letter tree data structure
License:	LGPL
Group:		System/Libraries
Source:		ftp://ftp.inria.fr/INRIA/Atoll/Guillaume.Rousse/%{name}-%{version}.tar.bz2

%description
This is a simple implementation of a lettertree, an efficient data structure
for storing and indexing string sharing a common prefix.

%package -n	%libname
Summary:	A letter tree data structur
Group:		System/Libraries

%description -n	%libname
This is a simple implementation of a lettertree, an efficient data structure
for storing and indexing string sharing a common prefix.

%package -n	%libname-devel 
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%libname = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%libname-devel
This package contains development files for %{name}.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
chmod 644 %{buildroot}%{_libdir}/liblettertree.la

%clean
rm -rf %{buildroot}

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%files -n %libname
%defattr(-,root,root)
%doc AUTHORS ChangeLog INSTALL README
%{_libdir}/*.so.*

%files -n %libname-devel
%defattr(-,root,root)
%{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/*.a
%{_includedir}/lettertree.h

