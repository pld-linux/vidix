
%define		_snap	20040221

Summary:	VIDIX is VIDeo Interface for *niX.
Name:		vidix
Version:	0.%{_snap}.1
Release:	1
Epoch:		1
License:	GPL v2
Group:		Libraries
Source0:	%{name}-snap%{_snap}.tar.bz2
# Source0-md5:	91939633ec7390529817def44c541d91
Patch0:		%{name}-Makefile.patch
Patch1:		%{name}-sources.patch
URL:		http://vidix.sourceforge.net/
BuildRequires:	mawk
Provides:	libdha.so
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libdha.so

%description
VIDIX is portable interface which was designed and introduced as
interface to userspace drivers to provide DGA everywhere where it's
possible.

%package devel
Summary:	Headers files for libvidix.
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
This package contains header files you can use to incorporate libvidix
into applications.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

%build
./configure \
    --prefix=%{_prefix} \
    --datadir=%{_datadir}
sed -i -e "s:OPTFLAGS =.*:OPTFLAGS=%{rpmcflags}:" config.mak
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d \
    $RPM_BUILD_ROOT{%{_includedir},%{_includedir}/vidix} \
    $RPM_BUILD_ROOT{%{_libdir},%{_libdir}/vidix}
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc vidix/README
%attr(755,root,root) %{_libdir}/*.so
%attr(755,root,root) %{_libdir}/vidix/*.so

%files devel
%defattr(644,root,root,755)
%doc vidix/vidix.txt
%{_includedir}/vidix/*.h
