%define	major	0
%define	libname	%mklibname lettertree %major

Name:		liblettertree
Version:	0.1
Release:	8
Summary:	A letter tree data structure
License:	LGPL
Group:		System/Libraries
Source0:	ftp://ftp.inria.fr/INRIA/Atoll/Guillaume.Rousse/%{name}-%{version}.tar.bz2

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
Provides:	%{name}-devel = %{EVRD}

%description -n	%libname-devel
This package contains development files for %{name}.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%files -n %libname
%doc AUTHORS ChangeLog INSTALL README
%{_libdir}/*.so.*

%files -n %libname-devel
%{_libdir}/*.so
%{_libdir}/*.a
%{_includedir}/lettertree.h



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1-6mdv2011.0
+ Revision: 620147
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.1-5mdv2010.0
+ Revision: 429787
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 0.1-4mdv2009.0
+ Revision: 248939
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.1-2mdv2008.1
+ Revision: 140925
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import liblettertree


* Tue Aug 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.1-2mdv2007.0
- Rebuild

* Tue Dec 06 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.1-1mdk
- first mdk release
