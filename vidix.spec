
%define		_snap	20040221

Summary:	VIDIX is VIDeo Interface for *niX
Summary(pl):	VIDIX - VIDeo Interface for *niX - interfejs video dla uniksów
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
BuildRequires:	sed >= 4.0
Provides:	libdha.so
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libdha.so

%description
VIDIX is portable interface which was designed and introduced as
interface to userspace drivers to provide DGA everywhere where it's
possible.

%description -l pl
VIDIX (VIDeo Interface for *niX) to przeno¶ny interfejs zaprojektowany
i wprowadzony jako interfejs do dzia³aj±cych w przestrzeni u¿ytkownika
sterowników udostêpniaj±cych DGA wszêdzie gdzie jest to mo¿liwe.

%package devel
Summary:	Headers files for libvidix
Summary(pl):	Pliki nag³ówkowe libvidix
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
This package contains header files you can use to incorporate libvidix
into applications.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe, których mo¿na u¿yæ do tworzenia
aplikacji korzystaj±cych z libvidix.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

%build
# configure doesn't accept --libdir, but takes _libdir from env
# (and it's modules path, not system wide libdir)
_libdir="%{_libdir}/vidix" \
./configure \
	--prefix=%{_prefix} \
	--datadir=%{_datadir}
sed -i -e "s:OPTFLAGS =.*:OPTFLAGS=%{rpmcflags}:" config.mak
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/vidix,%{_includedir}/vidix}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	libdir=%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc vidix/README
%attr(755,root,root) %{_libdir}/*.so
%dir %{_libdir}/vidix
%attr(755,root,root) %{_libdir}/vidix/*.so

%files devel
%defattr(644,root,root,755)
%doc vidix/vidix.txt
%{_includedir}/vidix
