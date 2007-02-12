Summary:	VIDIX is VIDeo Interface for *niX
Summary(pl.UTF-8):   VIDIX - VIDeo Interface for *niX - interfejs video dla Uniksów
Name:		vidix
Version:	0.9.9.3
Release:	1
Epoch:		1
License:	GPL v2
Group:		Libraries
Source0:	http://dl.sourceforge.net/vidix/%{name}-%{version}.tar.bz2
# Source0-md5:	bd204dd734c06451cda66e2eee620196
Patch0:		%{name}-Makefile.patch
Patch1:		%{name}-ppc.patch
Patch2:		%{name}-soname.patch
URL:		http://vidix.sourceforge.net/
BuildRequires:	mawk
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VIDIX is portable interface which was designed and introduced as
interface to userspace drivers to provide DGA everywhere where it's
possible.

%description -l pl.UTF-8
VIDIX (VIDeo Interface for *niX) to przenośny interfejs zaprojektowany
i wprowadzony jako interfejs do działających w przestrzeni użytkownika
sterowników udostępniających DGA wszędzie gdzie jest to możliwe.

%package devel
Summary:	Header files for libvidix
Summary(pl.UTF-8):   Pliki nagłówkowe libvidix
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
This package contains header files you can use to incorporate libvidix
into applications.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe, których można użyć do tworzenia
aplikacji korzystających z libvidix.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
# configure doesn't accept --libdir, but takes _libdir from env
# (and it's modules path, not system wide libdir)
_libdir="%{_libdir}/vidix" \
./configure \
	--prefix=%{_prefix} \
	--datadir=%{_datadir}
sed -i -e "s:OPTFLAGS =.*:OPTFLAGS=%{rpmcflags}:" config.mak
%{__make} \
	CC="%{__cc}"

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
%doc NEWS vidix/README
%attr(755,root,root) %{_libdir}/libdha-*.so
%attr(755,root,root) %{_libdir}/libvidix.so
%dir %{_libdir}/vidix
%attr(755,root,root) %{_libdir}/vidix/*.so

%files devel
%defattr(644,root,root,755)
%doc vidix/vidix.txt
%attr(755,root,root) %{_libdir}/libdha.so
%{_includedir}/vidix
